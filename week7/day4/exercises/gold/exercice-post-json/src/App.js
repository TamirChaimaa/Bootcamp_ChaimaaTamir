import React from "react";
import PostJsonFetch from "./PostJsonFetch";
import PostJsonAxios from "./PostJsonAxios";

function App() {
  return (
    <div className="App" style={{ padding: 20 }}>
      <PostJsonFetch />
      <hr />
      <PostJsonAxios />
    </div>
  );
}

export default App;
