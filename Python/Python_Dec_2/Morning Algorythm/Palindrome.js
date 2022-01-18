/* 
String: Is Palindrome
Create a function that returns a boolean whether the string is a strict palindrome. 
- palindrome = string that is same forwards and backwards

Do not ignore spaces, punctuation and capitalization
*/

// create a loop that workds through the string backwards
// create a new string
// add in those backwards values to the new string
// compare the new string to the old string, and if it mataches return True, doesn't return false

const str1 = "a x a";
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

function isPalindrome(str) {
    var newString = "";

    for (var i = str.length - 1; i >= 0; i--) {
        newString += str[i];
    }
    if (str == newString) {
        return true
    }
    else {
        return false
    }

}
console.log(isPalindrome(str1))
console.log(isPalindrome(str2))
console.log(isPalindrome(str3))
console.log(isPalindrome(str4))

/**
 * Determines if the given str is a palindrome (same forwards and backwards).
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given str is a palindrome or not.
 */
function isPalindrome(str) { }

// *******************************************************

/* 
Longest Palindrome
For this challenge, we will look not only at the entire string provided, but also at the substrings within it. Return the longest palindromic substring. 
Strings longer or shorter than complete words are OK.
All the substrings of "abc" are:
a, ab, abc, b, bc, c
*/

const two_str1 = "what up, daddy-o?";
const two_expected1 = "dad";

const two_str2 = "uh, not much";
const two_expected2 = "u";

const two_str3 = "Yikes! my favorite racecar erupted!";
const two_expected3 = "e racecar e";

const two_str4 = "a1001x20002y5677765z";
const two_expected4 = "5677765";

/**
 * Finds the longest palindromic substring in the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The longest palindromic substring from the given string.
 */

function isPalindrome(str) {
    i = 0;
    j = str.length - 1;
    while (i <= j) {
        if (str[i] != str[j]) {
            return false;
        }
        i++;
        j--;
    }
    return true
}

function longestPalindromicSubstring(str) {
    var longest = str[0];
    for (var i = 0; i < str.length; i++) {

        for (var j = 0; j < str.length - i; j++) {

            //var temp = str.splice(i, i+j);

            for (var k = 0; k <= j; k++) {
                var temp = str[i + k]
            }
            if (isPalindrome(temp)) {
                if (temp.length > longest.length) {
                    longest = temp;
                }
            }
        }
    }
    return longest;
}