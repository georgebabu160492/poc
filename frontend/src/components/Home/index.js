// This is the component for listing page

import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Header from "../Header/index";
import Button from "../Button/index";
import "./styles.css";
import beUrl from "../../constants";

const Home = () => {
  const [products, setProducts] = useState([]);
  const [isDeleted, setIsDeleted] = useState(false);
  const navigate = useNavigate();

  const onUpdate = (product) => {
    // Navigation when an edit button is pressed.
    navigate(`/product/edit/:${product.id}`, { state: product });
  };

  const onDelete = (id) => {
    // Delete functionality.
    if (window.confirm("Do you want to continue with this deletion?")) {
      setIsDeleted(true);
      fetch(`${beUrl}/api/project/${id}`, {
        method: "DELETE",
        mode: "cors",
        headers: { "Content-Type": "application/json" },
      })
        // if API hit is successful then this section gets executed.
        .then((response) => {
          alert("Deleted successfully");
          setIsDeleted(false);
          return response.json();
        })
        // if API fails or throws an error then this section gets executed.
        .catch((error) => {
          window.alert(
            "An unexpected error occured while deleting. Sorry for the inconvenience!!!"
          );
        });
    } else {
      alert("Cancelled");
    }
  };

  const fetchProductsData = () => {
    fetch(`${beUrl}/api/project`)
      // if API hit is successful then following sections get executed.
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        setProducts(data);
      })
      // if API fails or throws an error then this section gets executed.
      .catch((error) =>
        window.alert("Failed to fetch products. Sorry for the inconvenience!!!")
      );
  };

  useEffect(() => {
    fetchProductsData();
  }, [isDeleted]);

  return (
    // listing of products are done here.
    <div className="container">
      <Header />
      <p>
        <b>Number of items present - {products.length}</b>
      </p>
      {products.length > 0 ? (
        <table className="products-table">
          <tbody>
            <tr>
              <th>Number</th>
              <th>Name</th>
              <th>Scrum Master</th>
              <th>Owner</th>
              <th>Developers</th>
              <th>Start Date</th>
              {/* <th>Methodology</th>
              <th>Location</th> */}
              <th>Actions</th>
            </tr>
            {products.map((product) => {
              // JSX code to Display each developer name
              const renderDevelopers = product.developers.map((dev, index) => (
                <>
                  {dev.name}
                  <br />
                </>
              ));
              return (
                <tr key={product.id}>
                  <td>{product.id}</td>
                  <td>{product.project.name}</td>
                  <td>{product.scrum_master.name}</td>
                  <td>{product.project_owner.name}</td>
                  <td>{renderDevelopers}</td>
                  <td>{product.start_date}</td>
                  {/* <td>{product.methodology}</td>
                  <td>{product.location}</td> */}
                  <td>
                    <Button
                      onClick={() => onUpdate(product)}
                      color="#fca130"
                      text="Edit"
                    />
                    <Button
                      onClick={() => onDelete(product.id)}
                      color="#f93e3e"
                      text="Delete"
                    />
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      ) : (
        "No products to show"
      )}
    </div>
  );
};

export default Home;
