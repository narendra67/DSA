/**
 * HashTable
 * 
 */
class HashTable {
  constructor(size) {
    this.data = new Array(size)
  }

  _hashReminderMethod(key) {
    let hash = 0
    const length = this.data.length
    if (typeof (key) === "number") {
      console.log(typeof (key))

      hash = key % length
    } else {
      for (let i = 0; i < key.length; i++) {
        hash = (hash + key.charCodeAt(i) * i) % length
      }
    }
    return hash
  }

  set(key, value) {
    let hashIndex = this._hashReminderMethod(key)
    let currentBucket = this.data[hashIndex]
    if (!currentBucket) {
      // this.data[hashIndex] = []
      this.data[hashIndex] = [[key, value]]
    } else {
      let exits = false
      for (let i = 0; i < this.data[hashIndex].length; i++) {
        if (this.data[hashIndex][i][0] === key) {
          exits = true
          this.data[hashIndex][i] = [key, value]
          break;
        }
      }
      if (!exits) {
        this.data[hashIndex].push([key, value])
      }
    }
    return this.data
  }

  get(key) {
    let hashIndex = this._hashReminderMethod(key)
    if (this.data[hashIndex]) {
      for (let i = 0; i < this.data[hashIndex].length; i++) {
        if (this.data[hashIndex][i][0] === key) {
          return this.data[hashIndex][i]
        }
      }
      return "No key exits."
    } else {
      return `No value present at index${key}`
    }
  }

}

let HT = new HashTable(50)
HT.set("apple", 11111)
HT.set("banana", 1)
HT.set("banana", 2)
HT.set(1,1)
HT.set(51, 2)
console.log(HT.data)
console.log(HT.get(51))