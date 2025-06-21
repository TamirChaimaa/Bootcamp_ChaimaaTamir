// src/ErrorBoundary.js
import React from "react";

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      hasError: false,
      error: null,
      errorInfo: null,
    };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error("Error caught by ErrorBoundary:", error, errorInfo);
    this.setState({ errorInfo });
  }

  handleReload = () => {
    window.location.reload();
  };

  render() {
    if (this.state.hasError) {
      return (
        <div className="card my-5 p-4 bg-red-100 border border-red-400 text-red-700">
          <h2 className="font-bold mb-2">Something went wrong.</h2>
          <p>{this.state.error && this.state.error.toString()}</p>
          <pre style={{ whiteSpace: "pre-wrap" }}>
            {this.state.errorInfo?.componentStack}
          </pre>
          <button
            onClick={this.handleReload}
            className="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
          >
            Reload Page
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary;
