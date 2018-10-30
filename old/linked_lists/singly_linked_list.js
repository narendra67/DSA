function linkedList () {

  let Node = function (element) {
    this.element = element;
    this.next = null;
  }

  let length = 0;
  let head = null;

  this.append = (element) => {
    let node = new Node(element),
    current;
    if (head === null) {
      head = node;
      length ++;
    } else {
      current = head;
      while (current.next) {
        current = current.next;
      }
      current.next = node;
      length ++;
    }
  }

  this.removeAt = (position) => {
    
    if (position > -1 && position < length) {

      let current = head,
      index = 0

      if (position === 0) {
        head = current.next;
      } else {
        while (index ++ < position) {
          previous = current;
          current = current.next;
        }
        previous.next = current.next;
      }
      length --;
      return current.element;
    } else {
      return null;
    }
  }

  this.size = () => {
    return length;
  }
}

const ll = new linkedList()

// ll.append(3)
// ll.append(4)
// ll.removeAt(0)