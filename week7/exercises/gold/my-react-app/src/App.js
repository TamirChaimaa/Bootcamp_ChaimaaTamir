// App.js
import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import BootstrapCard from "./BootstrapCard";

function App() {
  const celebrities = [
    {
      title: "Bob Dylan",
      imageUrl:
        "https://miro.medium.com/max/4800/1*_EDEWvWLREzlAvaQRfC_SQ.jpeg",
      buttonLabel: "Go to Wikipedia",
      buttonUrl: "https://en.wikipedia.org/wiki/Bob_Dylan",
      description:
        "Bob Dylan (born Robert Allen Zimmerman, May 24, 1941) is an American singer/songwriter...",
    },
    {
      title: "McCartney",
      imageUrl:
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Paul_McCartney_in_October_2018.jpg/240px-Paul_McCartney_in_October_2018.jpg",
      buttonLabel: "Go to Wikipedia",
      buttonUrl: "https://en.wikipedia.org/wiki/Paul_McCartney",
      description:
        "Sir James Paul McCartney CH MBE (born 18 June 1942) is an English singer, songwriter...",
    },
  ];

  const planets = ["Mars", "Venus", "Jupiter", "Earth", "Saturn", "Neptune"];

  return (
    <div className="container">
      <h2 className="mt-5">Exercise 1: Bootstrap Cards</h2>
      <div className="d-flex flex-wrap justify-content-center">
        {celebrities.map((celeb, index) => (
          <BootstrapCard
            key={index}
            title={celeb.title}
            imageUrl={celeb.imageUrl}
            description={celeb.description}
            buttonLabel={celeb.buttonLabel}
            buttonUrl={celeb.buttonUrl}
          />
        ))}
      </div>

      <h2 className="mt-5">Exercise 2: Planets</h2>
      <ul className="list-group">
        {planets.map((planet, idx) => (
          <li key={idx} className="list-group-item">
            {planet}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
