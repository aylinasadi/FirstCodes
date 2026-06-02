console.log(`Hello`);
console.log(`test`);

window.alert(`alert test`);

document.getElementById("firstH1").textContent = `hi`;

//comment

/*
multi
line
comment
*/

let name;
name = window.prompt("enter your name: ");


const year = new Date().getFullYear();

document.getElementById("firstP").textContent = `name: ${name}`;

document.getElementById("submit").onclick = function() {
    let age = document.getElementById("age").value;
    age = Number(age);
    document.getElementById("secondP").textContent = `age: ${age}`;
    let birthYear = year - age
    document.getElementById("thirdP").textContent = `your birth year: ${birthYear-1}/${birthYear}`;
};

