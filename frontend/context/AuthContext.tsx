import React, { createContext, useState } from "react";

export const AuthContext = createContext<any>(null);

export function AuthProvider({ children }: any) {
  const [token, setToken] = useState<string | null>(null);
  const [username, setUsername] = useState<string | null>(null);

  const loginUser = (t: string, u: string) => {
    setToken(t);
    setUsername(u);
  };
  const logoutUser = () => {
    setToken(null);
    setUsername(null); 
  };

  return (
    <AuthContext.Provider value={{ token, username, loginUser, logoutUser }}>
      {children}
    </AuthContext.Provider>
  );
}