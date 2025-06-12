import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import FormPage from "./pages/FormPage";
import { GlobalProvider } from "./context/GlobalContext";
import Layout from "./components/Layout/Layout"; // make sure you import default, not named

const AppRoutes = () => {
  return (
    <GlobalProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<HomePage />} /> {/* Default route at "/" */}
            <Route path="form" element={<FormPage />} /> {/* Route at "/form" */}
          </Route>
        </Routes>
      </BrowserRouter>
    </GlobalProvider>
  );
};

export default AppRoutes;
