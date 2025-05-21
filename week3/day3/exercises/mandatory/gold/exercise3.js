function swapCase(str) {
  let swapped = '';

  for (let i = 0; i < str.length; i++) {
    let char = str[i];

    if (char === char.toUpperCase()) {
      swapped += char.toLowerCase();
    } else {
      swapped += char.toUpperCase();
    }
  }

  return swapped;
}


console.log(swapCase('The Quick Brown Fox'));