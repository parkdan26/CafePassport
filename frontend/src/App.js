import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home/Home";
import Signup from "./pages/Signup/Signup";
import Login from "./pages/Login/Login";

function App() {
  return (
    <Router>
<Routes>
  <Route path="/" element={<Home />} />       {/* default */}
  <Route path="/signup" element={<Signup />} />       {/* default */}
  <Route path="/login" element={<Login />} />       {/* default */}
</Routes>

    </Router>
  );
}

export default App;
