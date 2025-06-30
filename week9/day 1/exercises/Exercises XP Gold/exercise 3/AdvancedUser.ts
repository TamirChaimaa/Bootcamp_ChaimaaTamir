type AdvancedUser = {
    name: string;
    age: number;
    address?: string;
};

function introduceAdvancedUser(user: AdvancedUser): string {
    let message = `hello, my name is ${user.name} and I am ${user.age} years old.`;

    if (user.address) {
        message += ` i live at ${user.address}.`;
    }

    return message;
}

const user1: AdvancedUser = {
    name: "imane",
    age: 21,
    address: "123 idk",
};

const user2: AdvancedUser = {
    name: "ayman",
    age: 23,
};

console.log(introduceAdvancedUser(user1));
console.log(introduceAdvancedUser(user2));
