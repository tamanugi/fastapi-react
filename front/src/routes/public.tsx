import { useAuth } from "@/providers/auth";
import { Button, Input, Space } from "antd";
import { useState } from "react";
import { Navigate, useNavigate } from "react-router-dom";

const LoginPage = () => {
  const [userId, setUserId] = useState("");
  const { signin } = useAuth();
  const navigate = useNavigate();
  return (
    <div className="mx-auto flex h-screen w-[320px] flex-col justify-center gap-6">
      <Space direction="vertical">
        <Input
          placeholder="input ID"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
        />
        <Input.Password placeholder="input password" />
        <Button
          onClick={() => {
            signin(userId, () => {
              navigate("/");
            });
          }}
        >
          ログイン
        </Button>
      </Space>
    </div>
  );
};

export const publicRoutes = [
  { path: "/login", element: <LoginPage /> },
  { path: "/*", element: <Navigate to="/login"></Navigate> },
];
