import { AppProvider } from "@/providers/app";
import { AppRoutes } from "@/routes";
import "antd/dist/antd.css";
import "./App.css";

function App() {
  return (
    <AppProvider>
      <AppRoutes />
    </AppProvider>
  );
}

export default App;
