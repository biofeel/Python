/* 
  Given in an alumni interview in 2021.
  String Encode
  You are given a string that may contain sequences of consecutive letters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */

/*
- write function
- loop through string
- check "value"/character
- adding a count for each repetive one
- if next character is different THEN push value and count of previous character in new string
- loop through until end of string
- check lengths print larger one if new string -> original return new, otherwise print old value
- call the function
*/

const str1 = "aaaabbcddd";
const expected1 = "a4b2c1d3";

const str5 = "aaaabbcdddaaa";
const expected5 = "a4b2c1d3a3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

function encode(someString) {
  var newString = "";
  for (var i = 0; i < someString.length; i++) {
    var count = 1;
    while (someString[i] == someString[i + 1]) {
      // if someString
      count += 1;
      // console.log(count);
      i++;
    }
    newString += someString[i] + count;
  }
  if (newString.length < someString.length) {
    return newString;
  }
  else {
    return someString;
  }

}
console.log(encode(str2))
console.log(encode(str4))
console.log(encode(str5))




/**
 * Encodes the given string such that duplicate characters appear once followed
 * by a number representing how many times the char occurs only if the
 * character occurs more than two time.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string to encode.
 * @returns {string} The given string encoded.
 */
function encodeStr(str) { }

//   *****************************************************************************

/* 
  String Decode  
*/

const str1 = "a3b2c1d3";
const expected1 = "aaabbcddd";

const str2 = "a3b2c12d10";
const expected2 = "aaabbccccccccccccdddddddddd";

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
function decodeStr(str) { }