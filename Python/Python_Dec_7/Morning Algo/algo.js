/* 
Given a string containing space separated words
Reverse each word in the string.
If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

function reverseWords(str) {
    var newString = str.split(" ");
    var answer = "";
    for (i = 0; i < newString.length; i++) {
        for (j = newString[i].length - 1; j >= 0; j--) {
            answer += newString[i][j];
        }
        answer += " ";
    }
    return answer
}
console.log(reverseWords(str1));
console.log(reverseWords(str2));
console.log(reverseWords(str3));

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */


/*****************************************************************************/


/* 
Reverse Word Order
Given a string of words (with spaces)
return a new string with words in reverse sequence.
*/

const str1 = "This is a test";
const expected1 = "test a is This";

/**
 * Reverses the order of the words but not the words themselves form the given
 * string of space separated words.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string containing space separated words.
 * @returns {string} The given string with the word order reversed but the words
 *    themselves are not reversed.
 */
function reverseWordOrder(wordsStr) { }


/*****************************************************************************/

// if all spaces
if (wordsStr == false) {
    return wordsStr;
}

const words = wordsStr.split(" ");
let reversedWordOrder = "";

// loop backwards
for (let i = words.length - 1; i >= 0; --i) {
    reversedWordOrder += words[i];

    // don't add an extra space at the end
    if (i !== 0) {
        reversedWordOrder += " ";
    }
}
return reversedWordOrder;

/**
 * - Time: O(n) linear.
 * - Space: O(n) linear. wordsStr is stored again in reversedWOrdOrder var.
 */
function reverseWordOrder(wordsStr) {
    // if all spaces
    if (wordsStr == false) {
        return wordsStr;
    }

    let currWord = "";
    let reversedWordOrder = "";

    for (let i = wordsStr.length - 1; i >= 0; --i) {
        if (wordsStr[i] !== " ") {
            // prepend so the Word itself is not reversed by looping backWords
            currWord = wordsStr[i] + currWord;
        }
        // space found
        else {
            // add a space in front of the word, except on first word
            if (reversedWordOrder.length > 0) {
                currWord = " " + currWord;
            }

            reversedWordOrder += currWord;
            currWord = "";
        }
    }

    // no space at end of string means we didn't add the last word
    if (currWord.length > 0) {
        reversedWordOrder += " " + currWord;
    }
    return reversedWordOrder;
}