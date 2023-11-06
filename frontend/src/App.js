import React from "react";
import Home from "./components/Home";
import { Routes, Route } from "react-router-dom";
import AddProduct from "./components/AddProduct";

// Routes are added here for navigation.
const App = () => {
  return (
    <Routes>
      <Route exact path="/" element={<Home />} />
      <Route
        path="/product/add"
        element={<AddProduct label={"Create Product"} />}
      />
      <Route
        path="/product/edit/:id"
        element={<AddProduct label={"Edit Product"} />}
      />
    </Routes>
  );
};

export default App;
