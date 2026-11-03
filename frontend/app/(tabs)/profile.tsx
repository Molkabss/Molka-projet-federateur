import { View, Text, TouchableOpacity, ScrollView, ActivityIndicator, Alert } from "react-native";
import { useContext, useEffect, useState, useCallback } from "react";
import { AuthContext } from "../../context/AuthContext";
import { useRouter, useFocusEffect } from "expo-router";
import { Feather } from "@expo/vector-icons";
import { API_URL } from "../../config/config";
import { styles } from "../../styles/profile.styles";

const faqs = [
  {
    question: "What is Green Eye?",
    answer: "Green Eye is an AI-powered app that helps you identify plants and diagnose diseases from photos."
  },
  {
    question: "How do I identify a plant?",
    answer: "Go to the Home tab, tap the camera button, and take or upload a photo of your plant."
  },
  {
    question: "Is Green Eye free to use?",
    answer: "Yes, the core features are free. Premium features may be available in future updates."
  },
  {
    question: "How accurate is the diagnosis?",
    answer: "Our AI model achieves high accuracy, but we recommend consulting an expert for critical decisions."
  },
];

export default function Profile() {
  const { logoutUser, username, token } = useContext(AuthContext);
  const router = useRouter();

  const [history, setHistory] = useState<any[]>([]);
  const [loadingHistory, setLoadingHistory] = useState(true);

  useFocusEffect(
    useCallback(() => {
      fetchHistory();
    }, [token])
  );

  const fetchHistory = async () => {
    if (!token) {
      setLoadingHistory(false);
      return;
    }
    try {
      const res = await fetch(`${API_URL}/api/plant/history`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      const data = await res.json();
      if (data.success) {
        setHistory(data.history);
      }
    } catch (err) {
      console.error("Failed to fetch history", err);
    } finally {
      setLoadingHistory(false);
    }
  };

  const clearHistory = () => {
    Alert.alert(
      "Clear History",
      "Are you sure you want to clear all your plant history?",
      [
        { text: "Cancel", style: "cancel" },
        {
          text: "Clear",
          style: "destructive",
          onPress: () => setHistory([]),
        },
      ]
    );
  };

  const logout = () => {
    logoutUser();
    router.replace("/");
  };

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>

      {/* Avatar + Username */}
      <View style={styles.profileHeader}>
        <View style={styles.avatar}>
          <Feather name="user" size={40} color="#2E7D32" />
        </View>
        <Text style={styles.username}>{username ?? "Username"}</Text>
        <Text style={styles.subtitle}>Plant Enthusiast 🌿</Text>
      </View>

      {/* Prediction History */}
      <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', marginBottom: 8 }}>
        <Text style={styles.sectionTitle}>Your Plant History</Text>
        {history.length > 0 && (
          <TouchableOpacity
            onPress={clearHistory}
            style={{
              flexDirection: 'row',
              alignItems: 'center',
              gap: 4,
              paddingHorizontal: 10,
              paddingVertical: 5,
              borderRadius: 8,
              borderWidth: 1,
              borderColor: '#E53935',
            }}
          >
            <Feather name="trash-2" size={13} color="#E53935" />
            <Text style={{ color: '#E53935', fontSize: 12, fontWeight: '500' }}>Clear</Text>
          </TouchableOpacity>
        )}
      </View>

      {loadingHistory ? (
        <ActivityIndicator size="small" color="#2E7D32" style={{ marginBottom: 20 }} />
      ) : history.length > 0 ? (
        <View style={styles.historyContainer}>
          {history.map((item, index) => (
            <View key={item.id || index} style={styles.historyCard}>
              <View style={styles.historyIconBox}>
                <Feather name="image" size={20} color="#4CAF50" />
              </View>
              <View style={styles.historyInfo}>
                <Text style={styles.historyPlant}>{item.plant_type}</Text>
                <Text style={styles.historyDisease}>{item.disease}</Text>
              </View>
              <View style={styles.historyMeta}>
                <Text style={styles.historyConfidence}>{(item.confidence * 100).toFixed(0)}%</Text>
                <Text style={styles.historyDate}>{new Date(item.created_at).toLocaleDateString()}</Text>
              </View>
            </View>
          ))}
        </View>
      ) : (
        <Text style={styles.emptyText}>No predictions saved yet.</Text>
      )}

      {/* FAQ */}
      <Text style={styles.sectionTitle}>Frequently Asked Questions</Text>
      {faqs.map((faq, index) => (
        <View key={index} style={styles.faqCard}>
          <View style={styles.faqQuestion}>
            <Feather name="help-circle" size={18} color="#2E7D32" />
            <Text style={styles.questionText}>{faq.question}</Text>
          </View>
          <Text style={styles.answerText}>{faq.answer}</Text>
        </View>
      ))}

      {/* Logout */}
      <TouchableOpacity style={styles.logoutButton} onPress={logout} activeOpacity={0.8}>
        <Feather name="log-out" size={20} color="#FFFFFF" />
        <Text style={styles.logoutText}>Logout</Text>
      </TouchableOpacity>

    </ScrollView>
  );
}