import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Header.css';

const categories = ['Mountain', 'Beaches', 'Birds', 'Food'];

const Header = () => {
  const navigate = useNavigate();
  const handleClick = (category) => navigate(`/search/${category}`);

  return (
    <header className="header">
      <h1>Snap Shot</h1>
      <nav>
        {categories.map((cat) => (
          <button key={cat} onClick={() => handleClick(cat)}>{cat}</button>
        ))}
      </nav>
    </header>
  );
};

export default Header;