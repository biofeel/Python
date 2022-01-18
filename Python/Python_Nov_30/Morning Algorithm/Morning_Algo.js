/* 
Given an arr and a separator string, output a string of every item in the array separated by the separator.
No trailing separator at the end
Default the separator to a comma with a space after it if no separator is provided
*/

const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

/**
 * Converts the given array into a string of items separated by the given separator.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string|number|boolean>} arr The items to be joined as a string.
 * @param {string} separator To separate each item of the given arr.
 * @returns {string} The given array items as a string separated by the given separator.
 */

// Create a new_string variable
// Check to see if list length is equal to 1, then add that single value to new_string 
// if it isn't then
// Create a loop that starts at the beginning of the given list and stops at the end
// for each iteration:
//      add the value at the current index to new_string
//      add the separator to new_string
// after loop add last value in array
// return new_string

function join(arr, separator) {
    var new_string = "";
    if(arr.lentgth === 1){
        new_string += arr[0];
    }
    else{
        for(var i = 0; i < arr.length-1; i++){
            new_string += arr[i];
            new_string += separator;
        }
        new_string += arr[arr.length-1];
    }
    return new_string
}

console.log(arr1, separator1)

// ***********************************************************

/* 
Book Index
Given an array of ints representing page numbers
return a string with the page numbers formatted as page ranges when the nums span a consecutive range
*/

const two_nums1 = [1, 13, 14, 15, 37, 38, 70];
const two_expected1 = "1, 13-15, 37-38, 70";

const two_nums2 = [1,2,3,4,7,8,9,12,14,20,21];
const two_expected2 = "1-4, 7-9, 12, 14, 20-21";

// const two_nums2 = [-2,-1,2,3];
// const two_expected2 = "(-2)-(-1)";

/**
 * Turns the given arr of page numbers into a string of comma hyphenated
 * page ranges.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Page numbers.
 * @returns {string} The given page numbers as comma separated hyphenated
 *    page ranges.
 */
function bookIndex(nums) {
    var pages = "";
    for(var i = 0; i<nums.length; i++){
        var j=1
        if(nums[i+j] == nums[i]+j){
            while(nums[i+j]==nums[i]+j){
                j++;
            }
            j--;
            pages += nums[i]+"-"+nums[i+j];
            i+=j;
        }
        else{
            pages += nums[i];
        }
        if(i != nums.length-1){
            pages += ", ";
        }
    }
    return pages;
}

console.log(bookIndex(two_nums1));
console.log(bookIndex(two_nums2));
