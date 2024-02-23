import { BrowserRouter, Routes, Route } from "react-router-dom";

import './App.css'
import Dashboard from "./pages/dashboard";
function App() {

  return (
    <BrowserRouter>
      <Routes>
          <Route path="dashboard" element={<Dashboard />} />
          <Route path="*" element={<Dashboard />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App

//02/23/24 npm install react-router-dom 