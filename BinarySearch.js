/*
 * This is a JavaScript Scratchpad.
 *
 * Enter some JavaScript, then Right Click or choose from the Execute Menu:
 * 1. Run to evaluate the selected text (Cmd-R),
 * 2. Inspect to bring up an Object Inspector on the result (Cmd-I), or,
 * 3. Display to insert the result in a comment after the selection. (Cmd-L)
 */
var numOfIter = 0

const BinarySearch = (min, max, num) => {
  const avg = Math.round((min + max)/2)
  if (num < min | num > max) {
    console.log(`The number you are searching for is out of range`)
  }else if (avg === num) {
    console.log(`You found the number: ${avg}.`, `Number of Iterations: ${numOfIter}`, 2 ** numOfIter)
  } else if (avg > num) {
    console.log(`The num is too high.`)
    numOfIter++
    BinarySearch(min, avg - 1, num)
  } else if (avg < num) {
    console.log (`The num is too low.`)
    numOfIter++
    BinarySearch(avg + 1, max, num)
  }
}

BinarySearch(1, 2048000, 1)
