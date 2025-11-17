'use strict'

let count = Number(prompt("How many participants?"));
let participants = [];

for (let i = 0; i < count; i++) {
  let name = prompt(`Enter name of participant ${i + 1}:`);
  participants.push(name);
}

participants.sort();

let ol = document.createElement("ol");

for (let i = 0; i < participants.length; i++) {
  let li = document.createElement("li");
  li.textContent = participants[i];
  ol.appendChild(li);
}

document.body.appendChild(ol);

