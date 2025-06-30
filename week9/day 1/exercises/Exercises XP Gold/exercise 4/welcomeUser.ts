function welcomeUser(name: string, greeting: string = "Hello"): string {
    return `${greeting}, ${name}!`;
}

console.log(welcomeUser("imane"));             
console.log(welcomeUser("ayman", "Welcome"));      
console.log(welcomeUser("sanaa", "Good day")); 
