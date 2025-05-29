function isAnagram(str1, str2) {
    // Remove whitespace and convert to lowercase
    const clean = (str) => str.replace(/\s/g, '').toLowerCase();
    
    const cleanStr1 = clean(str1);
    const cleanStr2 = clean(str2);
    
    // If lengths are different, they cannot be anagrams
    if (cleanStr1.length !== cleanStr2.length) {
        return false;
    }
    
    // Sort the characters and compare
    const sortStr = (str) => str.split('').sort().join('');
    
    return sortStr(cleanStr1) === sortStr(cleanStr2);
}

// Usage examples
console.log(isAnagram("Astronomer", "Moon starer"));        // true
console.log(isAnagram("School master", "The classroom"));    // true
console.log(isAnagram("The Morse Code", "Here come dots"));  // true
console.log(isAnagram("Hello", "World"));                    // false
console.log(isAnagram("Listen", "Silent"));                  // true
console.log(isAnagram("Test", "Taste"));                     // false
