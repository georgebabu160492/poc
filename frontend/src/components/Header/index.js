// This component has only header related things of the landing page.

import { useNavigate } from "react-router-dom";
import Button from "../Button/index";
import "./styles.css";

const Header = () => {
  const navigate = useNavigate();

  const onAdd = () => {
    // Navigation to add product page when button is clicked.
    navigate("/product/add");
  };

  return (
    <header className="header">
      <h1>Projects List</h1>
      <Button onClick={onAdd} color="#61affe" text="Add Product" />
    </header>
  );
};

export default Header;
