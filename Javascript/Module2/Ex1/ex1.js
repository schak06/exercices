'use strict'
let nums = [];

for (let i = 0; i < 5; i++) {
  let n = Number(prompt(`Enter number ${i + 1}:`));
  nums.push(n);
}

console.log("Numbers in reverse order:");

for (let i = nums.length - 1; i >= 0; i--) {
  console.log(nums[i]);
}

