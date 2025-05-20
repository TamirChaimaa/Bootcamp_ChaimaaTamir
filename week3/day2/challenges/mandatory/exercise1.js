function replaceNotBadWithGood(sentence) {
  let wordNot = sentence.indexOf("not");
  console.log(wordNot);
  let wordBad = sentence.indexOf("bad");
  console.log(wordBad);
  let result = "";

  if (wordBad > wordNot && wordNot !== -1 && wordBad !== -1) {
    result = sentence.substring(0, wordNot);
    result = result.concat("good");
    result = result.concat(sentence.substring(wordBad + 3));
    return result;
  } else {
    return sentence;
  }
}

console.log(replaceNotBadWithGood("The movie is not that bad, I like it!"));
console.log(
  replaceNotBadWithGood("This dinner is not that bad ! You cook well")
);
console.log(replaceNotBadWithGood("This movie is not so bad !"));
console.log(replaceNotBadWithGood("This dinner is bad !"));

