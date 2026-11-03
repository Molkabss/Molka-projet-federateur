import React, { useState, useEffect, useContext } from 'react';
import { Modal, View, Text, TouchableOpacity, ActivityIndicator } from 'react-native';
import * as Location from 'expo-location';
import { AuthContext } from '../context/AuthContext';
import { API_URL } from '../config/config';
import { Ionicons, Feather } from '@expo/vector-icons';
import { styles } from './ClimateAlertPopup.styles';

export default function ClimateAlertPopup() {
  const { token } = useContext(AuthContext);
  const [modalVisible, setModalVisible] = useState(false);
  const [loading, setLoading] = useState(false);
  const [alertData, setAlertData] = useState<any>(null);

  useEffect(() => {
    if (token) {
      checkClimateAlerts();
      // Refresh every 10 minutes
      const interval = setInterval(checkClimateAlerts, 10 * 60 * 1000);
      return () => clearInterval(interval);
    }
  }, [token]);

  const checkClimateAlerts = async () => {
    try {
      let { status } = await Location.requestForegroundPermissionsAsync();
      if (status !== 'granted') return;

      let location = await Location.getCurrentPositionAsync({});
      const { latitude, longitude } = location.coords;

      const response = await fetch(`${API_URL}/api/plant/alerts?lat=${latitude}&lon=${longitude}`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await response.json();

      if (data.success) {
        setAlertData(data);
      }
    } catch (error) {
      console.log("Climate Alert Check failed:", error);
    }
  };

  if (!alertData) return null;

  return (
    <>
      {/* Floating Notification Button */}
      <TouchableOpacity 
        style={styles.floatingButton} 
        onPress={() => setModalVisible(true)}
        activeOpacity={0.8}
      >
        <Ionicons name="notifications" size={24} color="white" />
        {alertData.high_risk_count > 0 && (
          <View style={styles.badge}>
            <Text style={styles.badgeText}>{alertData.high_risk_count}</Text>
          </View>
        )}
      </TouchableOpacity>

      <Modal
      animationType="fade"
      transparent={true}
      visible={modalVisible}
      onRequestClose={() => setModalVisible(false)}
    >
      <View style={styles.centeredView}>
        <View style={styles.modalView}>
          <View style={styles.iconContainer}>
            <Feather name="alert-triangle" size={40} color="#D32F2F" />
          </View>
          
          <Text style={styles.title}>Climate Alert! ⚠️</Text>
          <Text style={styles.subtitle}>
            Weather conditions in {alertData?.location?.city || "your area"} are high risk for your plants.
          </Text>

          {/* Weather Snapshot */}
          <View style={styles.weatherInfo}>
            <View style={{flexDirection: 'row', alignItems: 'center', gap: 5}}>
              <Ionicons name="thermometer-outline" size={16} color="#333" />
              <Text style={styles.weatherText}>{alertData.weather.temperature}°C</Text>
            </View>
            <View style={{flexDirection: 'row', alignItems: 'center', gap: 5}}>
              <Ionicons name="water-outline" size={16} color="#333" />
              <Text style={styles.weatherText}>{alertData.weather.humidity}% Humidity</Text>
            </View>
          </View>

          {/* Alert details */}
          {alertData.high_risk_count > 0 ? (
            alertData.alerts.slice(0, 2).map((alert: any, index: number) => (
              <View key={index} style={styles.alertCard}>
                <Text style={styles.alertPlant}>{alert.plant_type} - {alert.disease}</Text>
                <Text style={styles.alertMessage}>{alert.message}</Text>
              </View>
            ))
          ) : (
            <View style={[styles.alertCard, { borderLeftColor: '#4CAF50', backgroundColor: '#F1F8E9' }]}>
              <Text style={[styles.alertPlant, { color: '#2E7D32' }]}>All Good! ✨</Text>
              <Text style={[styles.alertMessage, { color: '#4A7B4A' }]}>
                No high-risk climate conditions detected for your plants right now.
              </Text>
            </View>
          )}

          <TouchableOpacity
            style={styles.button}
            onPress={() => setModalVisible(false)}
          >
            <Text style={styles.buttonText}>I'll take care of it!</Text>
          </TouchableOpacity>
        </View>
      </View>
    </Modal>
    </>
  );
}
