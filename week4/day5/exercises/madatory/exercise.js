// List of robot objects with basic information
const robots = [
  {
    id: 1,
    name: "Leanne Graham",
    username: "Bret",
    email: "Sincere@april.biz",
    image: "https://robohash.org/1?200x200",
  },
  {
    id: 2,
    name: "Ervin Howell",
    username: "Antonette",
    email: "Shanna@melissa.tv",
    image: "https://robohash.org/2?200x200",
  },
  {
    id: 3,
    name: "Clementine Bauch",
    username: "Samantha",
    email: "Nathan@yesenia.net",
    image: "https://robohash.org/3?200x200",
  },
  {
    id: 4,
    name: "Patricia Lebsack",
    username: "Karianne",
    email: "Julianne.OConner@kory.org",
    image: "https://robohash.org/4?200x200",
  },
  {
    id: 5,
    name: "Chelsey Dietrich",
    username: "Kamren",
    email: "Lucio_Hettinger@annie.ca",
    image: "https://robohash.org/5?200x200",
  },
  {
    id: 6,
    name: "Mrs. Dennis Schulist",
    username: "Leopoldo_Corkery",
    email: "Karley_Dach@jasper.info",
    image: "https://robohash.org/6?200x200",
  },
  {
    id: 7,
    name: "Kurtis Weissnat",
    username: "Elwyn.Skiles",
    email: "Telly.Hoeger@billy.biz",
    image: "https://robohash.org/7?200x200",
  },
  {
    id: 8,
    name: "Nicholas Runolfsdottir V",
    username: "Maxime_Nienow",
    email: "Sherwood@rosamond.me",
    image: "https://robohash.org/8?200x200",
  },
  {
    id: 9,
    name: "Glenna Reichert",
    username: "Delphine",
    email: "Chaim_McDermott@dana.io",
    image: "https://robohash.org/9?200x200",
  },
  {
    id: 10,
    name: "Clementina DuBuque",
    username: "Moriah.Stanton",
    email: "Rey.Padberg@karina.biz",
    image: "https://robohash.org/10?200x200",
  },
];

// Get the container where robot cards will be displayed
const robotContainer = document.getElementById("robot-container");

// Get the search input field
const searchInput = document.getElementById("search");

// Function to display robots
const displayRobots = (robots) => {
  // If no robots match, show "No Robots Found"
  robots.length === 0
    ? (robotContainer.innerHTML = `<h3>No Robots Found</h3>`)
    : (robotContainer.innerHTML = robots
        .map(
          (robot) => `
       <div class="robot-card" style="background-image: url('https://raw.githubusercontent.com/devtlv/studentsGitHub/refs/heads/master/JS/Week%204/Day5/Mini%20Projects/Mini%20Project%201%20(Robots)/circuit-pattern.png'); background-size: cover; background-position: center;">
            <img src="${robot.image}" alt="${robot.name}">
            <div class="robot-info">
              <h2>${robot.name}</h2>
              <b><p>@${robot.username}</p></b>
              <b><p>${robot.email}</p></b>
            </div>
          </div>
        `
        )
        .join("")); // Join all robot cards into a single HTML string
};

// Initial display of all robots
displayRobots(robots);

// Event listener on the search input field
searchInput.addEventListener("input", (e) => {
  // Get the search term and convert it to lowercase
  const searchTerm = e.target.value.toLowerCase();

  // Filter the robot list by name based on the search term
  const filteredRobots = robots.filter((robot) =>
    robot.name.toLowerCase().includes(searchTerm)
  );

  // Display the filtered list
  displayRobots(filteredRobots);
});
