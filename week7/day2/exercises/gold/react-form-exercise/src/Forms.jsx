import React, { useState } from 'react';

function Forms() {
  const [username, setUsername] = useState('');
  const [age, setAge] = useState('');
  const [errormessage, setErrorMessage] = useState('');
  const [description, setDescription] = useState('Écrivez quelque chose ici...');
  const [car, setCar] = useState('Volvo');

  const handleChange = (e) => {
    const { name, value } = e.target;

    if (name === 'username') {
      setUsername(value);
    }

    if (name === 'age') {
      if (!Number(value)) {
        setErrorMessage("L'âge doit être un nombre.");
      } else {
        setErrorMessage('');
      }
      setAge(value);
    }
  };

  const mySubmitHandler = (e) => {
    e.preventDefault();
    if (!Number(age)) {
      alert("L'âge doit être un nombre.");
    } else {
      alert(`Nom: ${username}, Âge: ${age}`);
    }
  };

  let header;
  if (username || age) {
    header = <h1>Bonjour {username}, vous avez {age} ans.</h1>;
  }

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      {header}

      <form onSubmit={mySubmitHandler}>
        <p>Entrez votre nom :</p>
        <input type="text" name="username" onChange={handleChange} />

        <p>Entrez votre âge :</p>
        <input type="text" name="age" onChange={handleChange} />
        <br />
        {errormessage && <p style={{ color: 'red' }}>{errormessage}</p>}
        <br />

        <button type="submit">Soumettre</button>
      </form>

      <br />
      <hr />

      <h3>Texte (Textarea)</h3>
      <textarea
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        rows="4"
        cols="50"
      />
      <p>Contenu: {description}</p>

      <br />
      <hr />

      <h3>Choisissez une voiture</h3>
      <select value={car} onChange={(e) => setCar(e.target.value)}>
        <option value="Volvo">Volvo</option>
        <option value="Ford">Ford</option>
        <option value="Fiat">Fiat</option>
        <option value="BMW">BMW</option>
      </select>
      <p>Voiture sélectionnée: {car}</p>
    </div>
  );
}

export default Forms;
