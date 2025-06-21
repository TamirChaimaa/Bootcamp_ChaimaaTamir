// src/columns/ColumnRight.js
import React, { useState } from "react";
import ErrorBoundary from "../ErrorBoundary";

function ColumnRight() {
  const [text, setText] = useState(
    '{"function":"I live to crash"}'
  );

  const handleReplace = () => {
    // Remplacer la string par un objet JS -> provoque une erreur
    setText({ function: "I live to crash" });
  };

  return (
    <div>
      <p>Here is a paragraph.</p>

      <ErrorBoundary>
        <p>{text}</p>
      </ErrorBoundary>

      <button onClick={handleReplace}>
        Replace string with object
      </button>

      <button onClick={() => console.log("Clicked handler")}>
        Invoke event handler
      </button>
    </div>
  );
}

export default ColumnRight;
