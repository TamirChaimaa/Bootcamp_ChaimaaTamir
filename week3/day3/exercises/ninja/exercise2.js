function capitalize(s) {
  let evenCaps = '';
  let oddCaps = '';

  for (let i = 0; i < s.length; i++) {
    if (i % 2 === 0) {
      evenCaps += s[i].toUpperCase();
      oddCaps += s[i];
    } else {
      evenCaps += s[i];
      oddCaps += s[i].toUpperCase();
    }
  }

  return [evenCaps, oddCaps];
}

console.log(capitalize("abcdef")); 
