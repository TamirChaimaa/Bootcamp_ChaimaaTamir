// index.js

const { faker } = require('@faker-js/faker');
const prompt = require('prompt-sync')(); // pour le bonus

const users = [];

// Fonction pour générer un utilisateur avec faker
function addFakeUser() {
  const user = {
    name: faker.person.fullName(),
    address: faker.location.streetAddress(),
    country: faker.location.country(),
  };
  users.push(user);
}

// BONUS : Fonction pour ajouter un utilisateur à partir de l'entrée utilisateur
function addUserFromPrompt() {
  const name = prompt("Entrez le nom complet : ");
  const address = prompt("Entrez l'adresse : ");
  const country = prompt("Entrez le pays : ");
  
  const user = { name, address, country };
  users.push(user);
}

// Exemple d'utilisation
addFakeUser(); // Ajoute un utilisateur fake
addUserFromPrompt(); // Ajoute un utilisateur réel

console.log("Liste des utilisateurs :");
console.log(users);
