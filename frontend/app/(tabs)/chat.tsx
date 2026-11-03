import { View, Text, TouchableOpacity, FlatList, ActivityIndicator, Image, ScrollView, Alert, Animated } from "react-native";
import React, { useState, useEffect, useContext, useRef, useCallback } from "react";
import { AuthContext } from "../../context/AuthContext";
import { API_URL } from "../../config/config";
import { Ionicons } from '@expo/vector-icons';
import { useFocusEffect } from "expo-router";
import { styles } from "../../styles/chat.styles";

interface Message {
  id: string;
  text: string;
  sender: 'user' | 'bot';
  timestamp: Date;
  isTyping?: boolean;
}

const TypingIndicator = () => {
  const dot1 = useRef(new Animated.Value(0)).current;
  const dot2 = useRef(new Animated.Value(0)).current;
  const dot3 = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    const animateDot = (dot: Animated.Value, delay: number) =>
      Animated.loop(
        Animated.sequence([
          Animated.delay(delay),
          Animated.timing(dot, {
            toValue: -6,
            duration: 300,
            useNativeDriver: true,
          }),
          Animated.timing(dot, {
            toValue: 0,
            duration: 300,
            useNativeDriver: true,
          }),
          Animated.delay(600),
        ])
      );

    const anim1 = animateDot(dot1, 0);
    const anim2 = animateDot(dot2, 150);
    const anim3 = animateDot(dot3, 300);

    anim1.start();
    anim2.start();
    anim3.start();

    return () => {
      anim1.stop();
      anim2.stop();
      anim3.stop();
    };
  }, []);

  const dotStyle = {
    width: 8,
    height: 8,
    borderRadius: 4,
    backgroundColor: '#2E7D32',
    marginHorizontal: 3,
  };

  return (
    <View style={[
      styles.messageBubble,
      styles.botBubble,
      { flexDirection: 'row', alignItems: 'center', paddingVertical: 12, paddingHorizontal: 16 }
    ]}>
      <Animated.View style={[dotStyle, { transform: [{ translateY: dot1 }] }]} />
      <Animated.View style={[dotStyle, { transform: [{ translateY: dot2 }] }]} />
      <Animated.View style={[dotStyle, { transform: [{ translateY: dot3 }] }]} />
    </View>
  );
};

export default function Chat() {
  const { token } = useContext(AuthContext);
  const [messages, setMessages] = useState<Message[]>([]);
  const [questions, setQuestions] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [lastPrediction, setLastPrediction] = useState<any>(null);
  const [isTyping, setIsTyping] = useState(false);
  const flatListRef = useRef<FlatList>(null);

  useFocusEffect(
    useCallback(() => {
      startChat();
    }, [token])
  );

  const startChat = async () => {
    if (!token) return;
    setLoading(true);
    try {
      console.log("Fetching chatbot start from:", `${API_URL}/api/plant/chatbot/start`);
      const response = await fetch(`${API_URL}/api/plant/chatbot/start`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await response.json();
      console.log("Chatbot start data:", data);

      if (response.ok && data.success) {
        setLastPrediction(data.last_prediction);
        setQuestions(data.questions);

        const welcomeMsg: Message = {
          id: 'welcome',
          text: `Hello! I see we recently analyzed your ${data.last_prediction.plant}. How can I help you with the ${data.last_prediction.disease.replace(/_/g, ' ')}?`,
          sender: 'bot',
          timestamp: new Date()
        };
        setMessages([welcomeMsg]);
      } else {
        const errorMsg = data.detail || data.message || "Please analyze a plant first to start the conversation!";
        setMessages([{
          id: 'error',
          text: errorMsg,
          sender: 'bot',
          timestamp: new Date()
        }]);
      }
    } catch (error) {
      console.error("Chat Start Error:", error);
      Alert.alert("Connection Error", "Could not connect to the chatbot.");
    } finally {
      setLoading(false);
    }
  };

  const askQuestion = async (questionId: string, questionText: string) => {
    if (loading) return;

    // Add user message
    const userMsg: Message = {
      id: Date.now().toString(),
      text: questionText,
      sender: 'user',
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMsg]);
    setLoading(true);

    // Show typing indicator after a short delay
    setTimeout(() => {
      setIsTyping(true);
      setTimeout(() => flatListRef.current?.scrollToEnd({ animated: true }), 100);
    }, 300);

    // Random delay between 2000ms and 3000ms
    const typingDelay = Math.floor(Math.random() * 1000) + 2000;

    try {
      console.log("Fetching answer for:", questionId);

      // Run API call and minimum delay in parallel
      const [response] = await Promise.all([
        fetch(`${API_URL}/api/plant/chatbot/answer`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
          },
          body: JSON.stringify({
            question_type: questionId,
            plant: lastPrediction?.plant,
            disease: lastPrediction?.disease
          })
        }),
        new Promise(resolve => setTimeout(resolve, typingDelay))
      ]);

      const data = await response.json();
      console.log("Chatbot answer data:", data);

      setIsTyping(false);

      if (response.ok && data.success) {
        const botMsg: Message = {
          id: (Date.now() + 1).toString(),
          text: data.answer,
          sender: 'bot',
          timestamp: new Date()
        };
        setMessages(prev => [...prev, botMsg]);
      } else {
        const errorMsg = data.detail || "I'm sorry, I couldn't find an answer for that.";
        setMessages(prev => [...prev, {
          id: (Date.now() + 1).toString(),
          text: errorMsg,
          sender: 'bot',
          timestamp: new Date()
        }]);
      }
    } catch (error) {
      console.error("Chat Answer Error:", error);
      setIsTyping(false);
    } finally {
      setLoading(false);
      setTimeout(() => flatListRef.current?.scrollToEnd({ animated: true }), 100);
    }
  };

  const renderMessage = ({ item }: { item: Message }) => (
    <View style={[
      styles.messageBubble,
      item.sender === 'user' ? styles.userBubble : styles.botBubble
    ]}>
      <Text style={[
        styles.messageText,
        item.sender === 'user' ? styles.userText : styles.botText
      ]}>
        {item.text}
      </Text>
    </View>
  );

  return (
    <View style={styles.container}>
      {/* Header Info */}
      {lastPrediction && (
        <View style={styles.chatHeader}>
          <Ionicons name="leaf" size={20} color="#2E7D32" />
          <Text style={styles.headerText}>
            Discussing: <Text style={{ fontWeight: 'bold' }}>{lastPrediction.plant} - {lastPrediction.disease.replace(/_/g, ' ')}</Text>
          </Text>
        </View>
      )}

      <FlatList
        ref={flatListRef}
        data={messages}
        keyExtractor={item => item.id}
        renderItem={renderMessage}
        contentContainerStyle={styles.messageList}
        onContentSizeChange={() => flatListRef.current?.scrollToEnd({ animated: true })}
        ListFooterComponent={isTyping ? <TypingIndicator /> : null}
      />

      {/* Dynamic Question Buttons */}
      <View style={styles.inputContainer}>
        {questions.length > 0 && !loading && (
          <ScrollView horizontal showsHorizontalScrollIndicator={false} style={styles.questionsScroll}>
            {questions.map((q) => (
              <TouchableOpacity
                key={q.id}
                style={styles.questionButton}
                onPress={() => askQuestion(q.id, q.question)}
              >
                <Text style={styles.questionButtonText}>{q.question}</Text>
              </TouchableOpacity>
            ))}
          </ScrollView>
        )}
      </View>
    </View>
  );
}