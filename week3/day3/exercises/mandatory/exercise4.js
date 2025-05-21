const prompt = require('prompt-sync')();
function hotelCost(){
    let nombreNuit = parseInt(prompt("Enter the number of nights: "));
    while (nombreNuit <= 0 || nombreNuit == "") {
        nombreNuit = parseInt(prompt("Enter the number of nights: "));
    }
    prixNuit = 140;
    total = nombreNuit * prixNuit;
    return total;
}

function planeRideCost(){
    let destination = prompt("Enter the destination: ");
    while (destination == "" || destination == null ) {
        destination = prompt("Enter the destination: ");
    }
    switch (destination) {
        case "London":
            prixVol = 183;
            break;
        case "Paris":
            prixVol = 220;
            break;
        default:
            prixVol = 300;
            
    }
    return prixVol;
}

function rentalCarCost(){
    let nombreJours = parseInt(prompt("Enter the number of days (pour la voiture location): "));
    while (nombreJours <= 0 || nombreJours == "") {
        nombreJours = parseInt(prompt("Enter the number of days (pour la voiture location): "));
    }
    prixJour = 40;
    total = nombreJours * prixJour;
    if (nombreJours > 10) {
        total =total * 0.95;
    } 
    return total;
}
function totalVacationCost(){
    let hotel = hotelCost();
    let vol = planeRideCost();
    let location = rentalCarCost();
    let total = hotel + vol + location;
    console.log(`The total cost of your vacation is: ${total}`);
}
totalVacationCost();