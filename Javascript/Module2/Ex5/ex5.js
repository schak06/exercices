'use strict'

let nums = [];
let input = Number(prompt("Enter a number:"));

while (!nums.includes(input)) {
  nums.push(input);
  input = Number(prompt("Enter a number:"));
}

console.log("Number has already been entered. Program stops.");

nums.sort((a, b) => a - b);

console.log("Numbers in ascending order:");
for (let i = 0; i < nums.length; i++) {
  console.log(nums[i]);
}
