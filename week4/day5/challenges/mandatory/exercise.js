function isAnagram(str1, str2) {
  // Remove whitespace and convert to lowercase
  const clean = (str) => str.replace(/\s/g, "").toLowerCase();

  const cleanStr1 = clean(str1);
  const cleanStr2 = clean(str2);

  // If lengths differ, they can't be anagrams
  if (cleanStr1.length !== cleanStr2.length) {
    return false;
  }

  // Sort characters in the string
  const sortStr = (str) => str.split("").sort().join("");

  // Compare sorted strings
  return sortStr(cleanStr1) === sortStr(cleanStr2);
}

// Array of string pairs to test
const pairs = [
  ["Astronomer", "Moon starer"],
  ["School master", "The classroom"],
  ["The Morse Code", "Here come dots"],
  ["Hello", "World"],
  ["Listen", "Silent"],
  ["Test", "Taste"],
];

// Display results for each pair
pairs.forEach(([str1, str2]) => {
  if (isAnagram(str1, str2)) {
    console.log(`"${str1}" is an anagram of "${str2}"`);
  } else {
    console.log(`"${str1}" is NOT an anagram of "${str2}"`);
  }
});
