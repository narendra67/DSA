function swap(array, firstIndex, secondIndex) {
  let temp = array[firstIndex];
  array[firstIndex] = array[secondIndex];
  array[secondIndex] = temp;
}

function minimumIndex(array, startIndex) {
  let minIndex = startIndex
  let minValue = array[minIndex]
  
  for (var i = minIndex + 1; i < array.length; i++) {
    if (array[i] < minValue) {
      minIndex = i
    }
  }
  return minIndex
}

function selectionSort(array) {
  for(let i = 0; i < array.length; i++) {
    let firstIndex = i;
    let secondIndex = minimumIndex(array, i);
    swap(array, firstIndex, secondIndex)
  }
  console.log(array)
  return array
}

const array = [2,4,6,7,1]

selectionSort(array)