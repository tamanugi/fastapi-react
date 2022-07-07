import { AppProvider } from "@/providers/app";
import { AppRoutes } from "@/routes";
import "antd/dist/antd.css";
import "./App.css";
import { AuthProvider } from "./providers/auth";

function App() {
  return (
    <AuthProvider>
      <AppProvider>
        <AppRoutes />
      </AppProvider>
    </AuthProvider>
  );
}

export default App;
