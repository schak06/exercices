'use strict';
const num1 = Number(prompt("Enter the first number:"))
const num2 = Number(prompt("Enter the second number:"))
const num3 = Number(prompt("Enter the third number:"))
const sum = num1 + num2 + num3
const product = num1 * num2 * num3
const average = sum / 3
document.write(`The sum of ${num1}, ${num2}, and ${num3} is ${sum}.<br>`)
document.write(`The product of ${num1}, ${num2}, and ${num3} is ${product}.<br>`)
document.write(`The average of ${num1}, ${num2}, and ${num3} is ${average}.`)
