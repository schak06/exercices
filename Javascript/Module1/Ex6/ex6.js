'use strict'
const sqrt = confirm('Do you want to calculate the square root?')
if (sqrt){
    const number = prompt('Write your number')
if (number < 0){
    document.write('The square root of a negative number is not defined')}
else {
    document.write(`The square root of ${number} is ${Math.sqrt(number)}`)}}
else {
    document.write('The square root is not calculated.')}
