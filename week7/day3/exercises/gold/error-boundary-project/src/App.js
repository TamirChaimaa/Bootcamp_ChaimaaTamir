// src/App.js
import React from "react";
import ColumnLeft from "./columns/ColumnLeft";
import ColumnRight from "./columns/ColumnRight";
import ErrorBoundary from "./ErrorBoundary";

function App() {
  return (
    <div className="App">
      <h1>My App</h1>
      <div className="columns">
        <ColumnLeft />
        <ErrorBoundary>
          <ColumnRight />
        </ErrorBoundary>
      </div>
    </div>
  );
}

export default App;
