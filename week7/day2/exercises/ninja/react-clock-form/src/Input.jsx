// Input.js
import React from 'react';

function Input({ label, name, value, onChange, error }) {
  return (
    <div style={{ marginBottom: '1rem' }}>
      <label>{label}</label><br />
      <input
        type="text"
        name={name}
        value={value}
        onChange={onChange}
        style={{ borderColor: error ? 'red' : '#ccc' }}
      />
      {error && <div style={{ color: 'red' }}>{error}</div>}
    </div>
  );
}

export default Input;
