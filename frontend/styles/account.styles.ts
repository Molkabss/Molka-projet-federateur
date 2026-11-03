import { StyleSheet } from "react-native";

export const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#F5F9F5"
  },
  content: {
    flex: 1,
    padding: 20,
    alignItems: "center"
  },
  welcomeText: {
    fontSize: 20,
    fontWeight: "bold",
    color: "#333",
    marginTop: 40,
    marginBottom: 30,
  },
  analyseContainer: {
    backgroundColor: "white",
    width: "100%",
    borderRadius: 20,
    padding: 20,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.1,
    shadowRadius: 10,
    elevation: 5,
  },
  analyseTitle: {
    fontSize: 18,
    fontWeight: "600",
    color: "#2E7D32",
    marginBottom: 20,
    textAlign: "center",
  },
  actionBoxesContainer: {
    flexDirection: "column",
    gap: 15,
  },
  actionBox: {
    backgroundColor: "#F1F8E9",
    borderRadius: 15,
    padding: 15,
    alignItems: "center",
    justifyContent: "center",
    borderWidth: 1,
    borderStyle: "dashed",
    minHeight: 120,
  },
  actionBoxBlue: {
    backgroundColor: "#E3F2FD",
    borderColor: "#90CAF9",
  },
  actionBoxGreen: {
    backgroundColor: "#E8F5E9",
    borderColor: "#A5D6A7",
  },
  iconContainer: {
    backgroundColor: "white",
    padding: 10,
    borderRadius: 50,
    marginBottom: 10,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.05,
    shadowRadius: 5,
    elevation: 2,
  },
  actionTextBlue: {
    color: "#2196F3",
    fontWeight: "500",
    fontSize: 14,
  },
  actionTextGreen: {
    color: "#4CAF50",
    fontWeight: "500",
    fontSize: 14,
  },
  imagePreviewContainer: {
    alignItems: "center",
    width: "100%",
  },
  previewImage: {
    width: "100%",
    height: 250,
    borderRadius: 15,
    marginBottom: 15,
  },
  actionButtonsRow: {
    flexDirection: "row",
    gap: 10,
    width: "100%",
    marginBottom: 15,
  },
  actionButton: {
    flex: 1,
    flexDirection: "row",
    paddingVertical: 12,
    borderRadius: 10,
    alignItems: "center",
    justifyContent: "center",
    gap: 8,
  },
  analyzeButton: {
    backgroundColor: "#2196F3",
  },
  deleteButton: {
    backgroundColor: "#ef4444",
  },
  actionButtonText: {
    color: "white",
    fontWeight: "bold",
    fontSize: 16,
  },
  predictionBox: {
    width: "100%",
    backgroundColor: "#F1F8E9",
    borderRadius: 12,
    padding: 15,
    borderWidth: 1,
    borderColor: "#C8E6C9",
  },
  predictionTitle: {
    fontSize: 16,
    fontWeight: "bold",
    color: "#2E7D32",
    marginBottom: 10,
    textAlign: "center",
  },
  predictionText: {
    fontSize: 15,
    color: "#333",
    marginBottom: 5,
  },
  predictionBold: {
    fontWeight: "bold",
    color: "#1B5E20",
  }
});
