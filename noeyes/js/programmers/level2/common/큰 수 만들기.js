function solution(number, k) {
  const answer = number
    .split("")
    .reduce((answer, current) => {
      if (answer.length === 0) answer.push(current);
      else if (k > 0 && current > Math.min(...answer)) {
        const max = Math.max(...answer, current);
        const idx = answer.lastIndexOf(max + "");

        if (idx === -1) {
          const length = answer.length;
          answer = [...answer.slice(0, length > k ? length - k : 0), current];
          length > k ? (k = 0) : (k -= length);
        } else {
          const length = answer.length;
          answer = [
            ...answer.slice(0, length - (idx + 1) > k ? idx + 1 + k : idx + 1),
            current,
          ];
          length - (idx + 1) > k ? (k = 0) : (k -= length - (idx + 1));
        }
      } else {
        answer.push(current);
      }
      return answer;
    }, [])
    .join("");

  return k > 0 ? answer.slice(0, answer.length - k) : answer;
}

console.log(solution("1231234", 3));
