/* 
  Given an array of strings
  return a sum to represent how many times each array item is found (a frequency table)
  Useful methods:
    Object.hasOwnProperty("keyName")
      - returns true or false if the object has the key or not
    Python: key in dict
*/

// Psuedo code
// Creating new dictionary
// Create a for loop that iterates through the array
const arr1 = ["a", "a", "a"];
const expected1 = {
    a: 3,
};

const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
    a: 2,
    b: 1,
    c: 3,
    B: 1,
    d: 1,
};

const arr3 = [];
const expected3 = {};

/**
 * Builds a frequency table based on the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} arr
 * @returns {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.
 */
function frequencyTableBuilder(arr) {
    newObj = {};
    if (arr.length < 1) {
        return newObj
    }
    for (var i = 0; i < arr.length; i++) {
        if (newObj.hasOwnProperty(arr[i]) == false) {
            newObj[arr[i]] = 1;
        }
        else {
            newObj[arr[i]]++;
        }
    }
    return newObj
}

console.log(frequencyTableBuilder(arr1))
console.log(frequencyTableBuilder(arr2))
console.log(frequencyTableBuilder(arr3))

// ****************************************************

/* 
Given a non-empty array of odd length containing ints where every int but one
has a matching pair (another int that is the same)
return the only int that has no matching pair.
*/

const nums1 = [1];
const expected1 = 1;

const nums2 = [5, 4, 5];
const expected2 = 4;

const nums3 = [5, 4, 3, 4, 3, 4, 5];
const expected3 = 4; // there is a pair of 4s but one 4 has no pair.

const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const expected4 = 1;

function frequencyTableBuilder(arr) {
    var newObj = {};
    var expected = 0;

    if (arr.length < 1) {
        return newObj
    }
    for (var i = 0; i < arr.length; i++) {
        // console.log(arr[i]);
        if (newObj.hasOwnProperty(arr[i]) === false) {
            newObj[arr[i]] = 1;
        }
        else if (newObj.hasOwnProperty(arr[i]) === true && newObj[arr[i]] == 2) {
            newObj[arr[i]] = 1;
        }
        else {
            newObj[arr[i]]++;
        }
    }
    // console.log(newObj);
    for (const key in newObj) {
        // console.log(newObj[key])
        // expected = key;     //HOW TO GRAB KEYS WITH A VALUE THAT EQUALS 1?!?!?!
        if (newObj[key] === 1) {
            console.log('*******')
            // return parseInt(key)
            return +key
        }
    }
    // return expected

}

console.log(typeof frequencyTableBuilder(nums1))
console.log(frequencyTableBuilder(nums2))
console.log(frequencyTableBuilder(nums3))
console.log(frequencyTableBuilder(nums4))

/////////////////////////////////////////////////////
function oddOccurrencesInArray(nums) {
    const freqTable = {}

    for (const n of nums) {
        if (freqTable.hasOwnProperty(n)) {
            freqTable[n]++
        } else {
            freqTable[n] = 1
        }
    }

    for (const key in freqTable) {
        if (freqTable[key] % 2 !== 0) {
            return +key
        }
    }
}