/* 
Zip Arrays into Map


Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
Associative arrays are sometimes called maps because a key (string) maps to a value 
*/
// colbys psuedo code: create a function that take in two arrays and converts them into key:value pairs so that arr1[i]=arr2[i]
const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
const expected1 = {
    abc: 42,
    3: "wassup",
    yo: true,
};

const keys2 = ["abc", 3, "yo", "bro"];
const vals2 = [42, "wassup", true];
const expected2 = {
    abc: 42,
    3: "wassup",
    yo: true,
    "bro": ""
};

const keys3 = ["abc", 3, "yo"];
const vals3 = [42, "wassup", true, "tom"];
const expected3 = {
    abc: 42,
    3: "wassup",
    yo: true,
    "none": "tom"
};

const keys4 = ["abc", 3, "yo", 'yo'];
const vals4 = [42, "wassup", true, 'tom'];
const expected4 = {
    abc: 42,
    3: "wassup",
    yo: true,
    yo2: 'tom'
};

/**
 * Converts the given arrays of keys and values into an object.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} keys
 * @param {Array<any>} values
 * @returns {Object} The object with the given keys and values.
 */
function zipArraysIntoMap(keys, values) {
    let object1 = {}
    for (i = 0; i < keys.length; i++) {
        let key = keys[i]
        let value = values[i]
        if (value == undefined) {
            value = "none"
        }
        object1[key] = value
    }
    return object1
}
console.log(zipArraysIntoMap(keys2, vals2))


// *************************************************


/* 
Invert Hash
A hash table / hash map is an obj / dictionary
Given an object / dict,
return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
*/

const obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
const expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

const obj2 = { name: "Zaphod", charm: "high", morals: ['thing 1', 'thing 2'] };
const expected2 = { Zaphod: "name", high: "charm", 'thing 1': morals, 'thing 2': morals };

// 
const obj3 = { name: "Zaphod", charm: "", morals: "" };
const expected3 = { Zaphod: "name", "none": "charm", "none2": morals };

/**
 * Inverts the given object's key value pairs so that the original values
 * become the keys and the original keys become the values.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Object<string, string>} obj An object with string keys and string values.
 * @return The given object with key value pairs inverted.
 */
function invertObj(obj) { }
