/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

// const str1 = "creature";
// const expected1 = "erutaerc";

// const str2 = "dog";
// const expected2 = "god";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */

// psuedo code
// - create a function that takes in string
// - create create new string
// - loop through given string starting at the end
// - add the current index to the new string
// - iterate down
// - repeat until you get to the beginning

// function reverseString(str) {}

// *****************************************

/* 
Acronyms
Create a function that, given a string, returns the string’s acronym 
(first letter of each word capitalized). 
Do it with .split first if you need to, then try to do it without
*/

const str1 = " there's no free lunch - gotta pay yer way. ";
const expected1 = "TNFL-GPYW";

const str2 = "Live from New York, it's Saturday Night!";
const expected2 = "LFNYISN";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string to be turned into an acronym.
 * @returns {string} The given str converted into an acronym.
 */

// psuedo code
// - create a function that takes in string
// - create new string
// - split up letters
// - iterate and pick up first letters to print
// - print the output to uppercase
function acronymize(str) {
    var newStr2 = "";
    for(var i = 0; i<str.length; i++){
        if(i == 0 && str[i] != " "){
            newStr2 += str[i];
        }
        else if(str[i-1] == " "){
            newStr2 += str[i];
        }
    }
    return newStr2.toUpperCase()
}