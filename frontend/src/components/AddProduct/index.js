// This file deals form for creating/updating products.

import { useState, useEffect } from "react";
import "react-tagsinput/react-tagsinput.css";
import Button from "../Button/index";
import { useNavigate, useLocation } from "react-router-dom";
import "./styles.css";
import TagsInput from "react-tagsinput";
import { MultiSelect } from "react-multi-select-component";
import beUrl from "../../constants";


// State creation and handling is done below since we use same form for create and update.
const AddProduct = ({ label }) => {
  const lct = useLocation();
  const state = lct ? lct.state : "";
  const ID = state ? state.id : null;
  const dateFormatter = (d) => {
    // a date formatter to make sure the date format is same as expected
    let dt = d.split("/");
    return `${dt[0]}-${dt[2]}-${dt[1]}`;
  };
  const [product, setProduct] = useState(state ? state.project.name : "");
  const [owner, setOwner] = useState(state ? state.project_owner.name : "");
  const [developers, setDevelopers] = useState(state ? state.developers : []);
  const [developer_list , setDevelopersList] = useState([]);
  const [projectList , setProductsList] = useState([]); // this is for the dropdown list of products
  const [scrumMaster, setScrumMaster] = useState(
    state ? state.scrum_master.name : ""
  );
  const [date, setDate] = useState(state ? state.start_date : "");
  // const [date, setDate] = useState(state ? dateFormatter(state.start_date) : "");
  // const [methodology, setMethodology] = useState(
  //   state ? state.methodology : "Agile"
  // );
  // const [location, setLocation] = useState(state ? state.location : "");
  const setDeveloperState = (dev) => {
    setDevelopers(dev);
  }
  const navigate = useNavigate();
  useEffect(() => {
    fetch(`${beUrl}/api/project/get_form_iniital_data/`)
    // if API hit is successful then following sections get executed.
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      setDevelopersList(data.employees);
      setProductsList(data.projects);
      if (!ID)
    {
      setProduct(data.projects[0].id);
      setOwner(data.employees[0].id);
      setScrumMaster(data.employees[0].id);

    }
    else{
      setProduct(state.project.id);
      setOwner(state.project_owner.id);
      setScrumMaster(state.scrum_master.id);
      setDevelopers(state.developers.map((dev) => ({ value: dev.id, label: dev.name })));
    }
      
    })
    // if API fails or throws an error then this section gets executed.
    .catch((error) =>
      window.alert("Failed to fetch products. Sorry for the inconvenience!!!")
    );
  }, [ID]);


  const options = developer_list.map((dev) => {
    return {label: dev.name, value: dev.id}
  })

  const onSubmit = (e) => {
    // we prevent form submission and do basic validation like if all the fields have some value
    e.preventDefault();

    if (!product) {
      alert("Please enter a product name.");
      return;
    }

    if (!owner) {
      alert("Please add an owner.");
      return;
    }

    if (!developers || developers.length === 0) {
      alert("Please add a developer.");
      return;
    }

    if (!scrumMaster) {
      alert("Please add a scrum master.");
      return;
    }

    if (!date) {
      alert("Please add a date.");
      return;
    }

    // if (!location) {
    //   alert("Please add a location.");
    //   return;
    // }
    
    const formData = {
      project_id: parseInt(product),
      project_owner_id: parseInt(owner),
      developers: developers.map((dev) => ({ id: parseInt(dev.value) })),
      scrum_master_id: parseInt(scrumMaster),
      start_date: date,
      // methodology: methodology,
      // location: location,
    };
    if (label.includes("Edit")) {
      // IF condition is true then EDIT product API gets triggereed.
      fetch(`${beUrl}/api/project/${ID}`, {
        method: "PUT",
        mode: "cors",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      })
        // if API hit is successful then this section gets executed.
        .then((response) => {
          alert("Product updated successfully.");
          navigate("/");
          return response.json();
        })
        // if API fails or throws an error then this section gets executed.
        .catch((error) => {
          window.alert(
            "An unexpected error occured while updating product. Sorry for the inconvenience!!!"
          );
        });
    } else {
      // IF condition is false then CREATE product API gets triggered.
      fetch(`${beUrl}/api/project`, {
        method: "POST",
        mode: "cors",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      })
        // if API hit is successful then this section gets executed.
        .then((response) => {
          alert("Product created successfully.");
          navigate("/");
          return response.json();
        })
        // if API fails or throws an error then this section gets executed.
        .catch((error) => {
          window.alert(
            "An unexpected error occured while creating product. Sorry for the inconvenience!!!"
          );
        });
    }
  };

  const onExit = () => {
    // Rerouting to home page on click of exit button.
    navigate("/");
  };

  return (
    <form className="add-form container" id="add-form" onSubmit={onSubmit}>
      <div className="add-product-header">
        <Button onClick={onExit} color="black" text="Exit" />
        <h1>{label}</h1>
      </div>
      <div className="form-control">
        <label>Product Name</label>
        <select name="selectedFruit" className="form-control"  onChange={(e) => setProduct(e.target.value)} >
        {projectList.map((_project, index) => (
          <option value={_project.id} selected={product ? _project.id === product : index === 0}>{_project.name}</option>
          ))}
        </select>
      </div>
      <div className="form-control">
        <label>Product Owner Name</label>
        <select name="selectedFruit" className="form-control"  onChange={(e) => setOwner(e.target.value)} >
        {developer_list.map((dev, index) => (
          <option value={dev.id} selected={owner ? dev.id === owner : index === 0}>{dev.name}</option>
          ))}
         
        </select>
      </div>
      <div className="">
        <label>Developer Name</label>
        <MultiSelect
        options={options}
        value={developers.map((dev) => ({ value: dev?.value, label: dev?.label }))}
        onChange={setDeveloperState}
        labelledBy="Select"
      />
      </div>
      <div className="form-control">
        <label>Scrum Master Name</label>
        <select name="selectedFruit" className="form-control"  onChange={(e) => setScrumMaster(e.target.value)} >
        {developer_list.map((dev, index) => (
          <option value={dev.id} selected={scrumMaster ? dev.id === scrumMaster : index === 0}>{dev.name}</option>
          ))}
         
        </select>
      </div>
      {/* Not showing date field on edit form (as per document) logic added here */}
      {/* {!ID && ( */}
        <div className="form-control">
          <label>Start Date</label>
          <input
            type="date"
            value={date}
            onChange={(e) => setDate(e.target.value)}
            required
          ></input>
        </div>
      {/* )} */}
      <input
        type="submit"
        onClick={onSubmit}
        value="Save Product"
        className="btn btn-block"
      />
    </form>
  );
};

export default AddProduct;
