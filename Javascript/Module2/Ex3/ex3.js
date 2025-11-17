'use strict'

let dogs = [];

for (let i = 0; i < 6; i++) {
  let dog = prompt(`Enter dog name ${i + 1}:`);
  dogs.push(dog);
}

dogs.sort();
dogs.reverse();

let ul = document.createElement("ul");

for (let i = 0; i < dogs.length; i++) {
  let li = document.createElement("li");
  li.textContent = dogs[i];
  ul.appendChild(li);
}

document.body.appendChild(ul);
