const queue = []
const C = input.shift()

let result = ""

for (let i = 0; i < C; i++) {
    switch (input[i].split(" ")[0].toString().trim()) {
      case "pop":
        result += `${queue[0] ? queue[0] : -1}\n`
        queue.shift()
        break
      case "size":
        result += `${queue.length}\n`
        break
      case "empty":
        result += `${queue.length === 0 ? 1 : 0}\n`
        break
      case "front":
        result += `${queue[0] ? queue[0] : -1}\n`
        break
      case "back":
        result += `${queue[queue.length - 1] ? queue[queue.length - 1] : -1}\n`
        break
      default:
        queue.push(Number(input[i].split(" ")[1]))
        break
    }
}