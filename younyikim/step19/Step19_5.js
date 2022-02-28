const input = [];
const deque = [];
let output = '';

input.forEach(input => {
  if (input.includes('push_front')) {
    deque.splice(0, 0, input.split(' ')[1]);
  }
  if (input.includes('push_back')) {
    deque.push(input.split(' ')[1]);
  }
  if (input === 'pop_front') {
    output += deque.length ? deque.shift() + '\n' : '-1' + '\n';
  }
  if (input === 'pop_back') {
    output += deque.length ? deque.pop() + '\n' : '-1' + '\n';
  }
  if (input === 'size') {
    output += deque.length + '\n';
  }
  if (input === 'empty') {
    output += deque.length ? 0 + '\n' : 1 + '\n'
  }
  if (input === 'front') {
    output += deque.length ? deque[0] + '\n' : '-1' + '\n'
  }
  if (input === 'back') {
    output += deque.length ? deque[deque.length - 1] + '\n' : '-1' + '\n'
  }
})

console.log(output);