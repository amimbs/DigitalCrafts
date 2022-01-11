
//argv is the argument values of the process. The first process is node itself, the second process is the file we want to run, and the arguments are the things given by the user

//argv is an array from the command line. since we know what the first 2 things at the command line are (node and file name) we want the arguments after that. 2, 3 and 4 

let usernum1 = parseInt(process.argv[2])
let usernum2 = parseInt(process.argv[3])
let operation = process.argv[4]


console.log(process.argv)

function calculator(num1, num2, operation) {
    console.log("We are performing an operaiton with numbers: " + num1 + " and " + num2)
    //operation is a CALLBACK. meaning it is a function passed in as a paramater to be executed later on
    return operation(num1, num2)
}

let addition = function (num1, num2) {
    return num1 + num2
}

let subtraction = function (num1, num2) {
    return num1 - num2
}

let division = function (num1, num2) {
    return num1 / num2
}

// this switch case does the exact same thing as the loop below
switch(operation) {
    case 'addition':
        operation = addition
        break
    case 'subtraction':
        operation = subtraction
        break
    case 'division':
        operation = division
        break
}

// // this loop just checks the operation submitted at the argument and converts it to the actual funciton

// if (operation == 'addition') {
//     operation = addition;
// } else if (operation == 'subtraction') {
//     operation = subtraction
// } else if (operation == 'division') {
//     operation = division
// }

console.log(calculator(usernum1, usernum2, operation))

// $ node module2Day3.js 5 5 addition