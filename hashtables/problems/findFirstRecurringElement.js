/**
 * Problem Statement: Given an array find the first recurring character.
 * input: [2,3,5,6,1,2,5,7,8,0]
 * output: 2
 */


function findFirstRecurringElement(list) {
  if (!Array.isArray(list)) {
    return "Input should be an array."
  }

  const hashTable = new Array(list.length)

  const hashFunc = (key) => {
    let hashIndex = 0
    if (typeof (key) === "number") {
      hashIndex = key % list.length
    } else {
      for (let i = 0; i < key.length; i++) {
        hashIndex += key.charCodeAt(i) % list.length
      }
    }
    return hashIndex
  }

  for (let i = 0; i < list.length; i++) {
    const hashIndex = hashFunc(list[i])
    if (hashTable[hashIndex]) {
      return `${list[i]} - is the first repeated element.`
    } else {
      hashTable[hashIndex] = list[i]
    }
  }

  return "No element's repeat in the given list."

}

console.log(findFirstRecurringNumber(["apple", "ball", "car"]))
