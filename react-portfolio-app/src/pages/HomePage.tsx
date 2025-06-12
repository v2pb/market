// Home.js

import { useNavigate } from "react-router-dom";
import { useContext, useEffect } from "react";
import { GlobalContext } from "../context/GlobalContext";

const HomePage = () => {
  interface FormDataItem {
    [key: string]: any; // use `key` instead of `string` here
  }

  const navigate = useNavigate();
  const context = useContext(GlobalContext);
  // const location = useLocation();

  const handleOnclick = () => {
    navigate("/form");
  };
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        gap: "20px",
        padding: "20px",
        maxWidth: "800px",
        margin: "0 auto",
      }}
    >
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <h1>Items List</h1>
        <button
          onClick={handleOnclick}
          style={{
            padding: "8px 16px",
            backgroundColor: "#007bff",
            color: "white",
            border: "none",
            borderRadius: "4px",
            cursor: "pointer",
          }}
        >
          Add New Item
        </button>
      </div>

      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "10px",
        }}
      >
        {context?.globalStateMap &&
          Array.from(context.globalStateMap.entries()).map(([key, value]) => (
            <div
              key={key}
              style={{
                padding: "15px",
                backgroundColor: "#f8f9fa",
                borderRadius: "4px",
                boxShadow: "0 2px 4px rgba(0,0,0,0.1)",
              }}
            >
              <p style={{ margin: 0 }}>{value}</p>
              <small style={{ color: "#6c757d" }}>{key}</small>
            </div>
          ))}

        {(!context?.globalStateMap || context.globalStateMap.size === 0) && (
          <p style={{ textAlign: "center", color: "#6c757d" }}>
            No items added yet. Click the button above to add some!
          </p>
        )}
      </div>
    </div>
  );
};

export default HomePage;
