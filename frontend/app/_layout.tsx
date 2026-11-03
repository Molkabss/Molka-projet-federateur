import { Stack } from "expo-router";
import { AuthProvider } from "../context/AuthContext";

export default function RootLayout() {
  return (
    <AuthProvider>
      <Stack>

        <Stack.Screen
          name="index"
          options={{
            headerStyle: {
              backgroundColor: '#2E7D32',
            },
            headerShown: true,
            headerTitle: '',
            headerShadowVisible: false,
          }}
        />

        <Stack.Screen
          name="signin"
          options={{
            headerStyle: {
              backgroundColor: '#2E7D32',
            },
            headerTintColor: '#FFFFFF',   // White text/icons in header
            headerTitle: '',              // Remove the "index" title text
            headerShadowVisible: false,   // Clean look, no shadow line
          }}
        />

        <Stack.Screen
          name="signup"
          options={{
            headerStyle: {
              backgroundColor: '#2E7D32',
            },
            headerTintColor: '#FFFFFF',
            headerTitle: '',
            headerShadowVisible: false,
          }}
        />

        <Stack.Screen name="(tabs)" options={{ headerShown: false }} />

      </Stack>
    </AuthProvider>
  );
}