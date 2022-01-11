// Let's define functions that add, subtract, multiply, and divide:

const add = (x , y ) => {
    return x + y;
}

const sub = (x , y ) => {
    return x - y;
}

const mult = (x , y) => {
    return x * y;
}

const divis = (x , y) => {
    return x / y;
}

//This function receives 2 arguments and our math function from above

const apply =  (a, b, arithmetic) => {
    const value = arithmetic(a , b);
    return value;
}

// const result = apply(2, 3, mult);

// console.log(result);
// I want a little more explanation on this
const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const reduce = (arr, fn) => {
    let result = arr[0];

    for (let i = 1; i < arr.length; i++) {
        result = fn(result , arr[i]);
    }
    return result;
}

// const result =  reduce(nums, add);

// console.log(result);

const square = (z) => {
    return z *z;
}

const cube = (z) => {
    return z * z * z;
}

const map = (arr, arithmetic) => {
    const result = [];
    for (let i = 0; i < arr.length; i++) {
        result.push(arithmetic(arr[i]));
    }
    return result;
}

const r6 = map(nums, square)

const r7 = map(nums, cube)

console.log(r6)
console.log(r7)