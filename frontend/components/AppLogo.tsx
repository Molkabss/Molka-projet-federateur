import { View, Image, StyleSheet } from "react-native";

interface AppLogoProps {
  size?: number; // Taille configurable, défaut 100
}

export default function AppLogo({ size = 100 }: AppLogoProps) {
  return (
    <View style={[styles.logoCircle, { width: size, height: size, borderRadius: size / 2 }]}>
      <Image
        source={require('../assets/images/green_eye.jpeg')}
        style={styles.logoImage}
        resizeMode="cover"
      />
    </View>
  );
}

const styles = StyleSheet.create({
  logoCircle: {
    overflow: 'hidden',
    marginBottom: 16,
    shadowColor: '#2E7D32',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.2,
    shadowRadius: 8,
    elevation: 5,
  },
  logoImage: {
    width: '100%',
    height: '100%',
  },
});