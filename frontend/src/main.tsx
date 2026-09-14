import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ChatWindow from "./components/chat/ChatWindow";
import LeadsPage from "./pages/dashboard/LeadsPage";
import "./styles/theme.css";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<ChatWindow />} />
        <Route path="/leads" element={<LeadsPage />} />
      </Routes>
    </BrowserRouter>
  );
}

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
