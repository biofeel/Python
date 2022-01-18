/* 
Parens Valid
Given an str that has parentheses in it
return whether the parentheses are valid
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parentheses in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
function parensValid(str) {
    open_counter = 0;
    close_counter = 0;
    for (let i = 0; i < str.length; i++) {
        if (str[i] == "(") {
            open_counter++;
        }
        else if (str[i] == ")") {
            close_counter++;
        }
        if (open_counter < close_counter) {
            return false
        }
    } console.log(open_counter)
    console.log(close_counter)
    if (open_counter == close_counter) {
        return true
    }
    return false
}
console.log(parensValid(str3))

// module.exports = { parensValid };

/*****************************************************************************/

/* 
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/


const str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected1 = true;

const str2 = "D(i{a}l[ t]o)n{e";
const expected2 = false;

const str3 = "A(1)s[O (n]0{t) 0}k";
const expected3 = false;

/**
 * Determines whether the string's braces, brackets, and parentheses are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */

function bracesValid2(str) {
    const stack = [];

    const opens = "({[";

    const closeToOpen = { ")": "(", "}": "{", "]": "[" };

    for (let i = 0; i < str.length; i++) {
        if (opens.includes(str[i])) {
            stack.push(str[i]);
        } else if (str[i] in closeToOpen) {
            if (closeToOpen[str[i]] === stack[stack.length - 1]) {
                stack.pop();
            } else {
                return false;
            }
        }
    }
    return stack.length === 0;
}
// module.exports = { bracesValid };

/*****************************************************************************/