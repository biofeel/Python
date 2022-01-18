/* 
  Balance Index
  Here, a balance point is ON an index, not between indices.
  Return the balance index where sums are equal on either side
  (exclude its own value).
  
  Return -1 if none exist.
  
*/

const nums1 = [-2, 5, 7, 0, 3];
const expected1 = 2;

const nums2 = [9, 9];
const expected2 = -1;

const nums3 = [-2, 5, 0, 7, 0, 3];
const expected3 = 3;

const nums4 = [-2, 5, 7, 5, 3];
const expected4 = -1;

/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The balance index or -1 if there is none.
 */
function balanceIndex(nums) {}

// *********************************************************************


/* 
Given an array of ints representing a line of people where the space between
indexes is 1 foot, with 0 meaning no one is there and 1 meaning someone is in
that space,
return whether or not there is at least 6 feet separating every person.
Bonus: O(n) linear time (avoid nested loops that cause re-visited indexes).
*/


const array1 = [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1];
const expected1 = false;

const array2 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected2 = true;

function socialDistancingEnforcer(array) {
    let count = 0;
    let foundIt = false
    for (let i = 0; i < array.length; i++) {
        if (array[i] === 1) {
            if (count < 5 && foundIt ) {
                return false
            }
            count = 0;
            foundIt = true

        }
        count++
    }
    return true
}
function balanceIndex(arr) {
    if (arr.length <= 2) {
        return -1
    }
    var left = 0
    var right = arr.length-1
    var leftCount = arr[left]
    var rightCount = arr[right]
    while (left < right) {
        if (leftCount === rightCount) {
            left++;
            right --;
            leftCount += arr[left];
            rightCount += arr[right];
        }
        else if (leftCount < rightCount) {
            left++;
            leftCount += arr[left];
        }
        else if (rightCount < leftCount) {
            right--;
            rightCount += arr[right]
        }
    }
    if (leftCount === rightCount) {
        if (left === right) {
            return left
        }
        // else {
        //     return [left, right]
        //     console.log("$$$$$$$$$$$$$$$$$")
        // }
    }else {
        return -1
    }
}