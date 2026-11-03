import { View, Text, TouchableOpacity, Image, Alert, ActivityIndicator, Platform } from "react-native";
import React, { useState, useContext } from "react";
import * as ImagePicker from 'expo-image-picker';
import { Ionicons } from '@expo/vector-icons';
import { AuthContext } from "../../context/AuthContext";
import { API_URL } from "../../config/config";
import { styles } from "../../styles/account.styles";

export default function Account() {
  const [image, setImage] = useState<string | null>(null);
  const [prediction, setPrediction] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const { token } = useContext(AuthContext);

  const pickImage = async () => {
    let result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      allowsEditing: true,
      aspect: [4, 3],
      quality: 1,
    });

    if (!result.canceled) {
      setImage(result.assets[0].uri);
      setPrediction(null);
    }
  };

  const takePhoto = async () => {
    const permissionResult = await ImagePicker.requestCameraPermissionsAsync();

    if (permissionResult.granted === false) {
      Alert.alert("Permission Required", "You've refused to allow this app to access your camera!");
      return;
    }

    const result = await ImagePicker.launchCameraAsync({
      allowsEditing: true,
      aspect: [4, 3],
      quality: 1,
    });

    if (!result.canceled) {
      setImage(result.assets[0].uri);
      setPrediction(null);
    }
  };

  const removePhoto = () => {
    setImage(null);
    setPrediction(null);
  };

  const analyzePlant = async () => {
    if (!image) {
      console.log("No image selected");
      return;
    }
    if (!token) {
      Alert.alert("Error", "You must be logged in to analyze plants.");
      return;
    }

    setLoading(true);
    try {
      console.log("Starting analysis for image:", image);

      const formData = new FormData();
      
      if (Platform.OS === 'web') {
        // Web: Fetch the blob from the URI
        const imageResponse = await fetch(image);
        const blob = await imageResponse.blob();
        formData.append('file', blob, 'plant.jpg');
      } else {
        // Native (iOS/Android): Use the URI object structure
        formData.append('file', {
          uri: image,
          name: 'plant.jpg',
          type: 'image/jpeg',
        } as any);
      }

      console.log("Sending request to:", `${API_URL}/api/plant/predict/auto`);
      const response = await fetch(`${API_URL}/api/plant/predict/auto`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          // Do NOT set Content-Type manually for FormData
        },
        body: formData
      });

      const data = await response.json();
      console.log("Response received:", data);

      if (response.ok) {
        setPrediction(data);
      } else {
        Alert.alert("Error", data.detail || "Failed to analyze plant");
      }
    } catch (error: any) {
      console.error("Analysis Error:", error);
      Alert.alert("Connection Error", "Could not connect to the server. Check your console for details.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <View style={styles.content}>
        <Text style={styles.welcomeText}>Welcome to your account</Text>

        <View style={styles.analyseContainer}>
          <Text style={styles.analyseTitle}>Analyse your plant</Text>

          {image ? (
            <View style={styles.imagePreviewContainer}>
              <Image source={{ uri: image }} style={styles.previewImage} />

              <View style={styles.actionButtonsRow}>
                <TouchableOpacity
                  style={[styles.actionButton, styles.analyzeButton]}
                  onPress={analyzePlant}
                  disabled={loading}
                >
                  {loading ? (
                    <ActivityIndicator color="white" />
                  ) : (
                    <>
                      <Ionicons name="sparkles-outline" size={20} color="white" />
                      <Text style={styles.actionButtonText}>Analyze</Text>
                    </>
                  )}
                </TouchableOpacity>

                <TouchableOpacity
                  style={[styles.actionButton, styles.deleteButton]}
                  onPress={removePhoto}
                  disabled={loading}
                >
                  <Ionicons name="trash-outline" size={20} color="white" />
                  <Text style={styles.actionButtonText}>Delete</Text>
                </TouchableOpacity>
              </View>

              {prediction && (
                <View style={styles.predictionBox}>
                  <Text style={styles.predictionTitle}>Analysis Result:</Text>
                  <Text style={styles.predictionText}>🌱 Plant: <Text style={styles.predictionBold}>{prediction.plant_type}</Text></Text>
                  <Text style={styles.predictionText}>🦠 Disease: <Text style={styles.predictionBold}>{prediction.disease}</Text></Text>
                  <Text style={styles.predictionText}>📊 Confidence: <Text style={styles.predictionBold}>{(prediction.disease_confidence * 100).toFixed(1)}%</Text></Text>
                </View>
              )}

            </View>
          ) : (
            <View style={styles.actionBoxesContainer}>
              <TouchableOpacity style={[styles.actionBox, styles.actionBoxBlue]} onPress={pickImage}>
                <View style={styles.iconContainer}>
                  <Ionicons name="image-outline" size={32} color="#2196F3" />
                </View>
                <Text style={styles.actionTextBlue}>Upload Photo</Text>
              </TouchableOpacity>

              <TouchableOpacity style={[styles.actionBox, styles.actionBoxGreen]} onPress={takePhoto}>
                <View style={styles.iconContainer}>
                  <Ionicons name="camera-outline" size={32} color="#4CAF50" />
                </View>
                <Text style={styles.actionTextGreen}>Take Photo</Text>
              </TouchableOpacity>
            </View>
          )}
        </View>

      </View>
    </View>
  )
}