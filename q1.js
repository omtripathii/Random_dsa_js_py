// #  1    2   3
// #  4    5   6
// #  9    8   9

function absolute_difference(arr) {
  let n = arr.length;
  let sum1 = 0;
  let sum2 = 0;

  for (let i = 0; i < n; i++) {
    sum1 += arr[i][i];
    sum2 += arr[i][n - 1 - i];
  }
  return Math.abs(sum2 - sum1);
}
const arr = [
  [1, 2, 3],
  [4, 5, 6],
  [9, 8, 9],
];
console.log(absolute_difference(arr));
