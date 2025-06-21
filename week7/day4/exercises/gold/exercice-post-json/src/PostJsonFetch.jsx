import React, { Component } from "react";
import axios from "axios";

class PostJsonAxios extends Component {
  constructor(props) {
    super(props);
    this.state = {
      userId: "",
      title: "",
      body: ""
    };
  }

  handleChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  handleSubmit = (e) => {
    e.preventDefault();

    const { userId, title, body } = this.state;

    axios
      .post("https://jsonplaceholder.typicode.com/posts", {
        userId,
        title,
        body
      })
      .then((response) => {
        console.log("Data posted via axios:", response.data);
      })
      .catch((error) => console.error("Error:", error));
  };

  render() {
    const { userId, title, body } = this.state;

    return (
      <div>
        <h2>POST JSON Data with Axios</h2>
        <form onSubmit={this.handleSubmit}>
          <input
            type="number"
            name="userId"
            placeholder="User ID"
            value={userId}
            onChange={this.handleChange}
            required
          />
          <br />
          <input
            type="text"
            name="title"
            placeholder="Title"
            value={title}
            onChange={this.handleChange}
            required
          />
          <br />
          <textarea
            name="body"
            placeholder="Body"
            value={body}
            onChange={this.handleChange}
            required
          />
          <br />
          <button type="submit">Submit</button>
        </form>
      </div>
    );
  }
}

export default PostJsonAxios;
