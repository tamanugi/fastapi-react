import * as React from "react";

interface AuthContextType {
  user: string | null;
  signin: (user: string, callback: VoidFunction) => void;
  signout: (callback: VoidFunction) => void;
}

const AuthContext = React.createContext<AuthContextType>(null!);

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const [user, setUser] = React.useState<string | null>(null);

  const signin = (newUser: string, callback: VoidFunction) => {
    setUser(newUser);
    callback();
  };

  const signout = (callback: VoidFunction) => {
    setUser(null);
    callback();
  };

  const value = { user, signin, signout };
  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = () => {
  return React.useContext(AuthContext);
};
