function makeAnumber(){
    let myNum = 42
    return myNum
}

// number = makeAnumber()

// console.log(makeAnumber())

function makeAnInteger() {
    let myInt = 37
    return myInt
}

function makeAFloat() {
    let myFloat = 2.21
    return myFloat
}

function makeZero() {
    const zilch = 0
    return zilch
}

function makeNothing() {
    let huh
    return huh
}
function makeBoolean() {
    let myBool = true
    return myBool
}

function makeTrue() {
    let yep = true
    return yep
}

function makeFalse() {
    let nope = false
    return nope
}

function makeNull() {
    let nothingMuch = null
    return nothingMuch
}

function helloWorld() {
    let greeting = "Hello, world!"
    return greeting
}
// console.log(helloWorld())

function helloName(name) {
    return "Hello, " + name + "!"
}
// console.log(helloName("David"))

function abstractLength() {
    const tarPitAbstract = 'Complexity is the single major difficulty in the successful development of large-scale software systems. ' +
      'Following Brooks we distinguish accidental from essential difficulty, but disagree with his premise that most complexity remaining in contemporary systems is essential. ' +
      'We identify common causes of complexity and discuss general approaches which can be taken to eliminate them where they are accidental in nature. ' +
      'To make things more concrete we then give an outline for a potential complexity-minimizing approach based on functional programming and Codd’s relational model of data.'
      return tarPitAbstract.length
  }
// console.log(abstractLength())

function makeLoud() {
    let chorus = 'Who let the dogs out'
    return chorus.toUpperCase()
}
// console.log(makeLoud())


function makeQuiet(str) {
    return str.toLowerCase()
}
// console.log(makeQuiet("SCREAMING"))

function add99(number) {
    return number + 99
}

function add(a , b) {
    return a + b
}

function subract(n1 , n2) {
    return n1 - n2
}

function multiply(a1 , b1) {
    return a1 * b1
}

function divide(a2 , b2) {
    return a2 * b2
}

function mod(a3 , b3) {
    return a3 % b3
}

function threeFruits() {
    let fruits = ['Apple', 'Banana', 'Cherry']
    return fruits
}
// console.log(threeFruits())

function multipleTypes() {
    let diverseArray = ['Skateboard', null, 8.75, 'Eiffel Tower', 44, 7, true, null]
    return diverseArray
}

// Made it 23

function usePush() {
    let arr = ['a', 'b', 'c']
    return arr
}

// console.log(usePush())


function useIndexof() {
    let arr = ['C', 'A', 'G', 'T', 'A', 'A', 'G', 'T']

    return arr.indexOf('T')
}

function useJoin() {
    let arr = ['a', 'b', 'c', 'd', 'e', 'f']
    return arr.join()
}

// console.log(useJoin())

function threeNumbers() {
    const numbers = {numberOne: 1, numberTwo: 2, numberThree: 3}
    return numbers
}

// console.log(threeNumbers())

function manyTypes() {
    const diverseObject = {name: 'banana', count: 42, isDelicious: true}
    
    // below code will prin the keys in an object

    console.log(Object.keys(diverseObject))

    // Use dot notation to access the keys of an object

    return diverseObject.name
}

// console.log(manyTypes())

//Need Juan to expand on the console.assert() thing

function keyAccess() {
    const bestFruit = { name: 'banana', count: 42, isDelicious: true}

    bestFruit.color = 'yellow'

    return bestFruit

}

// console.log(keyAccess())

function largeObject() {
    const bootCampStudent = {
        name: 'Andy',
        email: 'andy@gmail',
        age: 30,
        height: 'small',
        favoriteColor: 'Black',
        homeTown: 'Atlanta',
        pet: 'Cat',
        onwsCar: true
    }
}

function nestedArray () {
    const bootcampInstructor = {
      name: 'Susan',
      favoriteColor: 'green',
      favoriteFoods: [
        'chicken pot pie',
        'salmon',
        'pho'
      ]
    }

    return bootcampInstructor.favoriteFoods[1]

}

console.log(nestedArray())

  // Some examples of using dot notation vs bracket notation:
//   console.assert(bootcampInstructor.name === 'Susan')
//   console.assert(bootcampInstructor['name'] === 'Susan')
//   const nameString = 'name'
//   console.assert(bootcampInstructor[nameString] === 'Susan')

//   console.assert(bootcampInstructor.favoriteColor === 'green')
//   console.assert(bootcampInstructor['favoriteColor'] === 'green')
//   console.assert(bootcampInstructor['favorite' + 'Color'] === 'green')

//   console.assert(bootcampInstructor['favoriteFoods'][0] === 'chicken pot pie')
//   console.assert(bootcampInstructor.favoriteFoods[0] === 'chicken pot pie')

  // Return the name of the bootcampInstructor Object using dot notation