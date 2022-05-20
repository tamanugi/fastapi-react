import * as React from "react";
import { BrowserRouter } from "react-router-dom";

type AppProviderProps = {
  children: React.ReactNode;
};

export const AppProvider = ({ children }: AppProviderProps) => {
  return (
    <React.Suspense fallback={<div>Loading Now...</div>}>
      <BrowserRouter>{children}</BrowserRouter>
    </React.Suspense>
  );
};
