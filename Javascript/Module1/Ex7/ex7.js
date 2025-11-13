let rolls = parseInt(prompt("How many dice do you want to roll?"));

if (isNaN(rolls) || rolls <= 0) {
  document.write("Please enter a valid positive number of rolls.");
} else {
  let sum = 0;


  for (let i = 0; i < rolls; i++) {

    let roll = Math.floor(Math.random() * 6) + 1;
    sum += roll;
  }

  document.write(`You rolled ${rolls} dice. The sum of the results is ${sum}.`);
}
