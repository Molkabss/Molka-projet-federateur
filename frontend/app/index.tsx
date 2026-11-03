import { View, Text, TouchableOpacity, StyleSheet, Image } from "react-native";
import { useRouter } from "expo-router";
import { Feather } from '@expo/vector-icons';
import AppLogo from "../components/AppLogo";

type FeatherIconName = React.ComponentProps<typeof Feather>['name'];

export default function Home() {
  const router = useRouter();

  const features: { icon: FeatherIconName; title: string; description: string }[] = [
    {
      icon: "camera",
      title: "Plant Identification",
      description: "Identify plant species instantly from photos"
    },
    {
      icon: "alert-triangle",
      title: "Disease Diagnosis",
      description: "Precise detection of plant diseases"
    },
    {
      icon: "droplet",
      title: "Treatment Solutions",
      description: "Eco-friendly and accessible treatment options"
    }
  ];

  return (
    <View style={styles.container}>

      <View style={styles.logoContainer}>

        <AppLogo />
        
        <Text style={styles.appName}>Green Eye</Text>
        <Text style={styles.tagline}>Your AI Plant Assistant</Text>
      </View>

      <View style={styles.featuresContainer}>
        {features.map((feature, index) => (
          <View key={index} style={styles.featureCard}>
            <View style={styles.iconContainer}>
              <Feather name={feature.icon} size={24} color="#2E7D32" />
            </View>
            <View style={styles.featureTextContainer}>
              <Text style={styles.featureTitle}>{feature.title}</Text>
              <Text style={styles.featureDescription}>{feature.description}</Text>
            </View>
          </View>
        ))}
      </View>

      <TouchableOpacity
        style={styles.button}
        onPress={() => router.push("/signin")}
        activeOpacity={0.8}
      >
        <Text style={styles.buttonText}>Get Started</Text>
        <Feather name="arrow-right" size={20} color="#FFFFFF" />
      </TouchableOpacity>

    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F9F5',
    paddingHorizontal: 24,
    justifyContent: 'space-between',
    paddingVertical: 60,
  },
  logoContainer: {
    alignItems: 'center',
    marginTop: 20,
  },
  appName: {
    fontSize: 36,
    fontWeight: 'bold',
    color: '#1B5E20',
    letterSpacing: 1,
    marginBottom: 8,
  },
  tagline: {
    fontSize: 16,
    color: '#4A7B4A',
    fontStyle: 'italic',
  },
  featuresContainer: {
    flex: 1,
    justifyContent: 'center',
    marginVertical: 30,  
  },
  featureCard: {
    flexDirection: 'row',
    backgroundColor: '#FFFFFF',
    padding: 20,
    borderRadius: 16,
    alignItems: 'center',
    marginBottom: 16,    
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 3,
    borderWidth: 1,
    borderColor: '#E0F0E0',
  },
  iconContainer: {
    width: 48,
    height: 48,
    borderRadius: 12,
    backgroundColor: '#E8F5E8',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 16,
  },
  featureTextContainer: {
    flex: 1,
  },
  featureTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#1B5E20',
    marginBottom: 4,
  },
  featureDescription: {
    fontSize: 14,
    color: '#5E7E5E',
    lineHeight: 20,
  },
  button: {
    backgroundColor: '#2E7D32',
    paddingVertical: 16,
    paddingHorizontal: 24,
    borderRadius: 30,
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',   
    shadowColor: '#2E7D32',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 5,
  },
  buttonText: {
    color: '#FFFFFF',
    fontSize: 18,
    fontWeight: '600',
    letterSpacing: 0.5,
    marginRight: 8,         
  },
});