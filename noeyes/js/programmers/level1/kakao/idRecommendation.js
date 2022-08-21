function solution(new_id) {
  let id = new_id.toLocaleLowerCase();
  let i = 0;

  function removeEnd(id) {
    let count = 0;
    if (id[0] === ".") {
      id = id.replace(id[0], "");
      count++;
    }
    if (id[id.length - 1] === ".") {
      id = id.slice(0, -1);
      count++;
    }

    return { newId: id, count };
  }

  while (i < id.length) {
    if (
      id[i] !== "-" &&
      id[i] !== "_" &&
      id[i] !== "." &&
      ((57 < id[i].charCodeAt() && id[i].charCodeAt() < 97) ||
        id[i].charCodeAt() > 122 ||
        id[i].charCodeAt() < 48)
    ) {
      id = id.slice(0, i) + id.slice(i + 1);
      i--;
    }

    i++;
  }

  i = 0;
  while (i < id.length) {
    if (id[i] === ".") {
      while (id[i + 1] === ".") {
        id = id.slice(0, i) + id.slice(i + 1);
      }
    }
    i++;
  }

  i = 0;
  while (i < id.length) {
    if (id[i] === ".") {
      while (id[i + 1] === ".") {
        id = id.slice(0, i) + id.slice(i + 1);
      }
    }
    i++;
  }

  while (true) {
    let { newId, count } = removeEnd(id);
    id = newId;
    if (count === 0) break;
  }

  if (id.length === 0) {
    id = ["a"];
  }

  if (id.length <= 2) {
    while (id.length < 3) {
      id += id[id.length - 1];
    }
  }

  if (id.length >= 16) {
    id = id.slice(0, 15);

    let { newId } = removeEnd(id);
    id = newId;
  }

  return id;
}

console.log(solution("..!3.32.2#.#.a"));
