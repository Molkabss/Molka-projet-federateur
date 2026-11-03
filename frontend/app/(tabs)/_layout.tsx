import { Tabs } from "expo-router";
import { Feather } from "@expo/vector-icons";
import { Image, View } from "react-native";
import ClimateAlertPopup from "../../components/ClimateAlertPopup";

export default function TabsLayout() {
  return (
    <>
      <ClimateAlertPopup />
      <Tabs
      screenOptions={{
        headerShown: true,
        headerLeft: () => (
          <Image 
            source={require('../../assets/images/green_eye.jpeg')} 
            style={{ width: 40, height: 40, marginLeft: 15, borderRadius: 8 }} 
            resizeMode="cover"
          />
        ),
        headerStyle: {
          backgroundColor: '#2E7D32',
          height: 60,  // ✅ Petite barre verte
        },
        headerTitle: '',
        headerShadowVisible: false,
        tabBarStyle: {
          backgroundColor: "#FFFFFF",
          borderTopColor: "#E0F0E0",
          paddingVertical: 8,
          height: 85,
        },
        tabBarActiveTintColor: "#2E7D32",
        tabBarInactiveTintColor: "#9CB89C",
        tabBarLabelStyle: {
          fontSize: 11,
          fontWeight: "500",
        },
      }}
    >
      <Tabs.Screen
        name="account"
        options={{
          tabBarLabel: "Home",
          tabBarIcon: ({ color }) => <Feather name="home" size={24} color={color} />,
        }}
      />
      <Tabs.Screen
        name="chat"
        options={{
          tabBarLabel: "Chat",
          tabBarIcon: ({ color }) => <Feather name="message-circle" size={24} color={color} />,
        }}
      />
      <Tabs.Screen
        name="profile"
        options={{
          tabBarLabel: "Profile",
          tabBarIcon: ({ color }) => <Feather name="user" size={24} color={color} />,
        }}
      />
    </Tabs>
    </>
  );
}