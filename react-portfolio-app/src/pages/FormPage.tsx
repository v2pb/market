import { useNavigate } from "react-router-dom";
import { useContext, useState } from "react";
import { GlobalContext } from "../context/GlobalContext";

const FormPage = () => {
  const nav = useNavigate();
  const context = useContext(GlobalContext);
  const addGlobalStateData = context?.addGlobalStateData;
  const [input, setInput] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (input.trim() && addGlobalStateData) {
      const keydata = `entry_${Date.now()}`;
      addGlobalStateData(keydata, input.trim());
      const existingData = JSON.parse(localStorage.getItem("formdata") || "[]");
      const newEntry = { [keydata]: input.trim() };
      const updatedData = [...existingData, newEntry];

      localStorage.setItem("formdata", JSON.stringify(updatedData));

      setInput("");
      nav("/");
    }
  };

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <form
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "8px", // optional spacing between input and button
        }}
        onSubmit={handleSubmit}
      >
        <input
          type="text"
          className="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default FormPage;
