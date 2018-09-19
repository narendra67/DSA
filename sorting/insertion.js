function slide(array, index) {
  let key = index;
  const val = array[index]
  // console.log(val)
  if(index > 0) {
    for (let i=index - 1; i>=0; i--) {
      if(val <= array[i]) {
        array[i+1] = array[i]
        array[i] = val
        if (i === 0) {array[i] = val}
        console.log(val, array, i)
      } else {
        // array[i] = val
        console.log(val, array, i)
        // break;
      }
    }
  }
  // console.log(val, array, i)
}

const array = [8, 11, 3, 2, 86, 4, -2, 0]

const insertionSort = (array) => {
  for (let i = 0; i < array.length; i++) {
    slide(array, i)
  }
console.log(array)
}
insertionSort(array)