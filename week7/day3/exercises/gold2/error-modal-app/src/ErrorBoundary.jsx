// ErrorBoundary.js
import React from 'react';
import Modal from './Modal';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      hasError: false,
      errorInfo: null
    };
  }

  occurError = () => {
    this.setState({ hasError: true });
  }

  componentDidCatch(error, info) {
    this.setState({ errorInfo: info });
  }

  handleClose = () => {
    this.setState({ hasError: false, errorInfo: null });
  }

  render() {
    if (this.state.hasError) {
      return (
        <Modal
          message="Something went wrong!"
          onClose={this.handleClose}
        />
      );
    }

    return (
      <div>
        <button onClick={this.occurError}>Trigger Error</button>
      </div>
    );
  }
}

export default ErrorBoundary;
