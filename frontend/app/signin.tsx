import { useState, useContext } from "react";
import { View, Text, TextInput, TouchableOpacity, StyleSheet, Image } from "react-native";
import { useRouter } from "expo-router";
import { login } from "../services/api";
import { AuthContext } from "../context/AuthContext";
import { Feather } from "@expo/vector-icons";
import AppLogo from "../components/AppLogo";

export default function SignIn() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const { loginUser } = useContext(AuthContext);
  const router = useRouter();

  const handleLogin = async () => {
    try {
      const data = await login(username, password);
      loginUser(data.access_token, username);
      router.replace("/account");
    } catch (err: any) {
      setError(err.message);
    }
  };

  return (
    <View style={styles.container}>

      {/* Header */}
      <View style={styles.logoContainer}>

        <AppLogo size={80} />
        
        <Text style={styles.appName}>Green Eye</Text>
        <Text style={styles.tagline}>Sign in to continue</Text>
      </View>

      {/* Form */}
      <View style={styles.formContainer}>

        <View style={styles.inputWrapper}>
          <Feather name="user" size={18} color="#4A7B4A" style={styles.inputIcon} />
          <TextInput
            style={styles.input}
            placeholder="Username"
            placeholderTextColor="#9CB89C"
            value={username}
            onChangeText={setUsername}
            autoCapitalize="none"
          />
        </View>

        <View style={styles.inputWrapper}>
          <Feather name="lock" size={18} color="#4A7B4A" style={styles.inputIcon} />
          <TextInput
            style={styles.input}
            placeholder="Password"
            placeholderTextColor="#9CB89C"
            value={password}
            onChangeText={setPassword}
            secureTextEntry
          />
        </View>

        {error ? <Text style={styles.error}>{error}</Text> : null}

        <TouchableOpacity style={styles.button} onPress={handleLogin} activeOpacity={0.8}>
          <Text style={styles.buttonText}>Sign In</Text>
        </TouchableOpacity>

        <Text style={styles.link} onPress={() => router.push("/signup")}>
          Don't have an account?{" "}
          <Text style={styles.linkBold}>Sign Up</Text>
        </Text>

      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingBottom: 65,
    backgroundColor: "#F5F9F5",
    paddingHorizontal: 24,
    justifyContent: "center",
  },
  logoContainer: {
    alignItems: "center",
    marginBottom: 40,
  },
  appName: {
    fontSize: 28,
    fontWeight: "bold",
    color: "#1B5E20",
    letterSpacing: 1,
    marginBottom: 4,
  },
  tagline: {
    fontSize: 14,
    color: "#4A7B4A",
    fontStyle: "italic",
  },
  formContainer: {
    gap: 14,
  },
  inputWrapper: {
    flexDirection: "row",
    alignItems: "center",
    backgroundColor: "#FFFFFF",
    borderRadius: 16,
    borderWidth: 1,
    borderColor: "#E0F0E0",
    paddingHorizontal: 16,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.06,
    shadowRadius: 6,
    elevation: 2,
  },
  inputIcon: {
    marginRight: 10,
  },
  input: {
    flex: 1,
    paddingVertical: 14,
    fontSize: 15,
    color: "#1B5E20",
  },
  error: {
    color: "#C62828",
    fontSize: 13,
    textAlign: "center",
  },
  button: {
    backgroundColor: "#2E7D32",
    paddingVertical: 16,
    borderRadius: 30,
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
    gap: 8,
    marginTop: 6,
    shadowColor: "#2E7D32",
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 5,
  },
  buttonText: {
    color: "#FFFFFF",
    fontSize: 17,
    fontWeight: "600",
    letterSpacing: 0.5,
  },
  link: {
    marginTop: 10,
    textAlign: "center",
    color: "#5E7E5E",
    fontSize: 14,
  },
  linkBold: {
    color: "#2E7D32",
    fontWeight: "600",
  },
});