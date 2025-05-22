function isPalindrome(word) {
  let reversed = word.split('');
  reversed = reversed.reverse();
  reversed = reversed.join('');
  if(word=== reversed){
    console.log("The Entry is a Palindrome");
  }
  else{
    console.log("The Entry is not a Palindrome");
  }

  
}
isPalindrome('racecar');
isPalindrome('hello');
isPalindrome('madam');