// // console.log is how we print to terminal in js
// console.log("Hello, world!") 

// // const <variable name> is how we store variables
// const friendlyGreeting = "Hello World!"

// //console is an object and log is a function that recieves an input.
// console.log(friendlyGreeting);


// // node hello_world.js <-- in terminal to run js code

// //object is our key. the values are testing, test2 and something. Known as key value pairs
// // you must list the commas for each value
// var object = {
//     testing: 4,
//     test2: "hello",
//     someThing: "Just because",
//     object2: {
//         mysecond: "something"
//     }
// }

// console.log(object.someThing)
// console.log(object["someThing"])
//  // Here we created an object using structures
// var person = {
//     name: "Juan",
//     lastName: "Mrad",
//     //This is a nested object
//     hobbies: {
//         favorites: "Video Games",
//         second: "Programming"
//     },
//     address: {
//         first: "123",
//         second: "street",
//         state: "Georgia"
//     },
//     gender: "male"
// }

// // Use dot notation to access the values within an object, and even it's nested objects
// console.log(person.address.state)

// var person2 = {
//     name: "Josh",
//     lastName: "Joshery",
//     //This is a nested object
//     hobbies: {
//         favorites: "Video Games",
//         second: "Programming"
//     },
//     address: {
//         first: "123",
//         second: "street",
//         state: "Georgia"
//     },
//     gender: "male"
// }

// var people = [person, person2]

// //this will print the objects and their values
// console.log(people)

// var number1 = 5
// var number2 = 10

// number1 += 10 
// numebr2 -= 5

// console.log(number1)






// Modern Javascript

// You cannot overwrite const variables, this protects us if we have variables that should never change. Lie tax rates
// const firstName = "Andy"

// // let variables CAN be overwritten. They are scope assignments
// let lastName = "Mimbs"

// //Here we overwrite it's previous value
// lastName = "Mimbsy"

// console.log("Hello " + firstName + " " + lastName)

// // This will print 'true'. Simple boolean
// console.log(firstName == "Andy" && lastName == "Mimbsy")







// FUNCTIONS!!!!!!!!!!!!!!!!!!!!!!!!


// // We define out funciton
// function add() {
//     let number1 = 5;
//     let number2 = 10;

//     console.log(number1 + number2)
// }

// add()
// add()

// // We can pass parameters into functions as well. And this is the correct way to write a function
// function addition(number3, number4) {
//     return(number3 + number4)
// }

// console.log(addition(5, 13))


//Loops 

// i++ is the same as i = i + 1

// var students = ["student1", "student2", "student3"];
// for (var i = 0; i < 3; i ++) {
//     console("Current value of i : " + i)
//     console.log(students[i])
//     // this will loop 3 times
// }

// function totalWithTip(itmes) {
//     const tip_rate = 0.20
//     let subtotal = 0

//     for (let i = 0; i < itmes.length; i ++) {
//         subtotal = subtotal + itmes[i]
//     }

//     const tip = subtotal * tip_rate;
//     return subtotal + tip;
// }

// let total = totalWithTip([5, 10, 15, 20, 50])

// console.log("With a tip rate of 20%, your total should be: " + total)

// let num1 = 5;
// let num2 = 10;

// let subtotal = num1 + num2;
// let tip = subtotal * 0.2;
// let total = tip + subtotal;

// console.log(total);

// as we can see in this example, our scope will quickly become too large. Because each time our customer wants to add an item to their order, we have to add another number to the program. It would become too unwieldly. Instead we should write a function

function totalWithTips(items) {
    let tip_rate = 0;
    let subtotal = 0;

    for (let i = 0 ; i < items.length; i++) {
        subtotal = subtotal + items[i]
    }

    if (subtotal < 100) {
        tip_rate = 0.1;
    } else if ( subtotal < 500) {
        tip_rate = 0.15;
    } else {
        tip_rate = 0.2;
    }
        
    const tip = subtotal * tip_rate;
    return subtotal + tip;
}

let total = totalWithTips([5, 10, 15, 20])
 console.log(total)

 let total2 = totalWithTips([5, 10, 15, 20, 100])
 console.log(total2)

 let total3 = totalWithTips([5, 10, 15, 20, 100, 500])
 console.log(total3)