const BSA = (array, number) => {
  /**
   * 1. Sort the Array
   * 2. get minIndex and maxIndex
   * 3. eval (minIndex + maxIndex)/2 = number ? END : step 4
   * 4. check number < avg or number > avg
   * 5. change minIndex and maxIndex accordingly
   * 6. repeat 3, 4 and 5 
  */
  
  const sortedArray = array.sort((a, b) => a-b)
  console.log(sortedArray.length)
  var minIndex = 0
  var maxIndex = sortedArray.length - 1

  const findNum = (minIndex, maxIndex, sortedArray, number) => {
    console.log(minIndex, maxIndex)
    const avgIndex = Math.round((minIndex + maxIndex)/2)

    console.log(`The guess is ${avgIndex}`)

    if (maxIndex < minIndex) {
      console.log('Index not in array')
    } else if (sortedArray[avgIndex] === number) {
      console.log(`The index of the number is ${avgIndex}: ${sortedArray[avgIndex]}`)
    } else if (sortedArray[avgIndex] > number) {
      maxIndex = avgIndex - 1
      console.log('Number is lesser than the guess', minIndex, maxIndex, avgIndex, sortedArray[avgIndex])
      findNum (minIndex, maxIndex, sortedArray, number)
    } else if (sortedArray[avgIndex] < number) {
      minIndex = avgIndex + 1
      console.log('Number is greater than the guess')
      findNum (minIndex, maxIndex, sortedArray, number)
    }
  }

  findNum (minIndex, maxIndex, sortedArray, number)
  
}

BSA([1, 3, 13, 5, 7, 90, 4, 23, 16], 7)