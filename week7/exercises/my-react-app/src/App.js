import "./App.css";
import UserFavoriteAnimals from "./UserFavoritAnimals";
import Exercise from "./Exercise3";

// Exercise 1 & 2
function App() {
  const user = {
    firstName: "Bob",
    lastName: "Dylan",
    favAnimals: ["Horse", "Turtle", "Elephant", "Monkey"],
  };
  const myelement = <h1>I Love JSX!</h1>;
  const sum = 5 + 5;

  return (
    <div>
      {/* Exercise 1 */}
      <p>Hello World!</p>
      {myelement}
      <p>React is {sum} times better with JSX</p>

      {/* Exercise 2 */}
      <h3>{user.firstName}</h3>
      <h3>{user.lastName}</h3>
      <UserFavoriteAnimals favAnimals={user.favAnimals} />
       <Exercise />
    </div>
  );
}

export default App;
