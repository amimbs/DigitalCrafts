// // let n =1;
// // while (n < 10) {
// //     n++
// // }

// // console.log(n)

// let n = 5
// let conversation = ''

// while (n > 0) {
//     // !== is the "strict not equal" too operator. It checks if 2 oppends are the same type and value and returns a boolean expression
//     if (n % 2 !== 0) {
//         conversation += "one for me. "
//         if (n === 1){
//             conversation += "none for you."
//         }
//     } else {
//         conversation += "one for you\n"
//         if (n === 1) {
//             conversation += "none for me."
//         }
//     }
//     n--

//     // console.log("one for me")
//     // console.log(`${n} cookie: me`)
//     // conversation += "one for me \n"
//     // n--

//     // console.log(`${n} cookie: you`)
//     // conversation += "one for you \n"
//     // n--
// }

// console.log(conversation)

// // Our program is not perfect (the output is formatted oddly if you start with an even number of cookies), but it illustrates two points:

// //     Use loops to "build up" a String.
// //     Use conditionals to determine what gets added to a String.

// // The takeaway is that counting up and counting down is more useful than it first appears.




// // Counting specific items in an Array

// // In the cookie divider we just wrote, the source of our information was a number. We produced a sequence of numbers by counting down.

// // Sometimes, you will be given a sequence. Imagine an array of ratings for a product:

// // const ratings = [3, 1, 5, 2, 5, 2, 1, 4, 2, 3, 2, 5, 4, 3, 2, 4, 2, 4, 1, 5]

// // Let's say that this particular product needs at least six 5-star ratings to be featured on the homepage of shopping site. How would you know (without manually counting) whether this is a featured product?
// // The first thing to do is start with a loop that can print each rating. It's best to use a for-loop for iterating through an Array. (A while loop is best when you need fine-grained control of the loop variable.)

// const ratings = [3, 1, 5, 2, 5, 2, 1, 4, 2, 3, 2, 5, 4, 3, 2, 4, 2, 4, 1, 5]
// const max = ratings.length
// let count = 0

// for (let i = 0; i < max; i ++) {
//     const stars = ratings[i]
//     if (stars === 5) {
//         count++
//     }
// }

// if (count >= 6) {
//     console.log('This is a featured product!')
// } else {
//     console.log('Sorry, no homepage for you.')
// }
// In this example, we determined whether a particular product should be featured on a shopping site's home page. But, the combination of loops and conditionals is a good way to analyze the contents of any Array.





// // Summing Arrays

// // In a related problem, you may need to add all the numbers in an Array. Here are two arrays, each with the number of votes a candidate received from different polling stations:

// // Which candidate won the election?

// // As before, we start with a simple for-loop. In this example, the Arrays are the same length, so we can use a single loop. This loop prints the number of votes for a candidate from each polling station (c1Votes[i] and c2Votes[i]):

// const c1Votes = [996, 139, 80, 591, 217, 817, 235, 846, 141, 60];
// const c2Votes = [746, 154, 366, 515, 523, 846, 590, 806, 446, 23];
// const max = c1Votes.length //c2votes2.length is the same
// let c1Total = 0
// let c2Total = 0

// for (let i = 0; i < max; i ++) {
//     console.log(c1Votes[i])
//     c1Total += c1Votes[i]
//     console.log(c2Votes[i])
//     c2Total += c2Votes[i]
// }

// if (c1Total > c2Total) {
//     console.log('Candidate 1 is the winner')
// } else {
//     (c1Total < c2Total)
//     console.log('Candidate 2 is the winner')
// }




// // Searching

// // Strings, Arrays, and Objects are great for holding collections of values. But what if you needed to know if a particular value existed in a collection?
// // Finding the index of an Array item

// // In the "star-rating" problem earlier in this lesson, you counted the number of 5-star ratings the product received. A related problem is locating a particular item in an Array - that is, determining the index of that item.

// // Let's say that you have a list of guests at a wedding. When each arrives, they will tell you their name. You tell them their table number for the reception. That data might look like this:

// // If the information is in two separate Arrays, how do we find the table number if we're given the name?

// // The thing to keep in mind that the information in the two tables correspond: the first element in guests goes with the first element in tables, the second element in guests goes with the second element in tables. (Scarlett is seated at table 3, Plum is at table 1, Peacock at 1, etc.)

// // The first version will look similar to the loops you've already written. For now, our program will find what table Mustard is assigned to.

// const guests = ['Scarlett', 'Plum', 'Peacock', 'Green', 'Mustard', 'White'];
// const tables = [3, 1, 1, 2, 3, 2];

// const guestTofind = 'Plum'

// for (let i = 0; i < guests.length; i++) {
//     if (guests[i] === guestTofind) {
//         console.log(`${guestTofind} sits at table ${tables[i]}`)
//     }
// }

// // Line 6 sets up our loop for iterating through the guests list. Line 7 makes sure that we only console.log() if we've located that guest.

// // The second version makes sure to stop the loop once it is found:

// const guests = ['Scarlett', 'Plum', 'Peacock', 'Green', 'Mustard', 'White'];
// const tables = [3, 1, 1, 2, 3, 2];

// const guestToFind = 'Mustard'; // hard-coded in this example

// for (let i=0; i<guests.length; i++) {
//   if (guests[i] === guestToFind) {
//     console.log(`${guestToFind} sits at table ${tables[i]}`);
//     break;
//   }
// }

// // The break keyword stops a loop immediately.
// // Though we have found the correct table, it might be useful to save the index, instead of doing our work (printing) inside the loop. Let's add a foundIndex variable, initialized to -1, which can never be a valid index. 
// // If we do not find the guest's name in the Array, we can use the value -1 to tell our program to print an appropriate error message.

// const guests = ['Scarlett', 'Plum', 'Peacock', 'Green', 'Mustard', 'White'];
// const tables = [3, 1, 1, 2, 3, 2];
// const guestToFind = 'Mustard'; // hard-coded in this example
// let foundIndex = -1

// for (let i = 0; i < guests.length; i++) {
//     if (guests[i] === guestToFind) {
//         foundIndex = i
//         break
//     }
// }

// if (foundIndex !== -1) {
//     console.log(`${guestToFind} sits at table ${tables[foundIndex]}`)
// } else {
//     console.log(`${guestToFind} is not on the guest list`)
// }

// // The main reason for doing this is so that we can move our searching algorithm into its own function:

// const guests = ['Scarlett', 'Plum', 'Peacock', 'Green', 'Mustard', 'White'];
// const tables = [3, 1, 1, 2, 3, 2];

// function indexFor(guestToFind) {
//   let foundIndex = -1;
//   for (let i=0; i<guests.length; i++) {
//     if (guests[i] === guestToFind) {
//       foundIndex = i;
//       break;
//     }
//   }
//   return foundIndex;
// }

// // const guestToFind = 'Mustard'; // hard-coded in this example
// // const index = indexFor(guestToFind);
// // const guestTable = tables[index];
// // if (index !== -1) {
// //   console.log(`${guestToFind} sits at table ${guestTable}`)
// // } else {
// //   console.log(`${guestToFind} is not on the guest list.`)
// // }

// function printTablefor(guestToFind) {
//     const index = indexFor(guestToFind)
//     const guestTable = tables[index]
//     if (index !== -1) {
//         console.log(`${guestToFind} sits at table ${guestTable}`)
//     } else {
//         console.log(`${guestToFind} is not on the guest list.`)
//     }
// }

// printTablefor('Mustard');
// printTablefor('Batman');

// // printTableFor() can be used over and over for different guest names. Every time it is called, it calls indexFor().




// // Finding a substring

// // One way to think of a String is that it is a sequence (like an Array) of individual letters. (Some languages have a separate "Character" data type, but JavaScript is not one of them.)

// // The next example is a little sci-fi: you're programming a DNA-repair bot. (Don't worry, you don't really need to know anything about DNA. In fact, this example is mostly fiction and almost no science.)

// // Your DNA-repair bot has a copy of a healthy version of the sequence, consisting only of the letters G, A, T, and C:

// // 'GCTGGGTGGGACACTGTCGTTCCTTACCGCACCGCCACATCATTCACCCTTGGGCAACCC'

// // But it may encounter a damaged version that contains the letter Z:

// // 'GCTZGGTGGGZCACTGTCGTTCCTTACCGCACCGCCACATCATTCACCCTTGGGCAACCC'

// // The DNA-repair bot would locate the letter Z at indexes 3 and 10 and replace them with the corresponding letters from the healthy sequence (G and A).

// // To get started, here are three variables containing DNA Strings. The first is the HEALTHY version for reference. The other two are samples that the DNA-repair bot will search through, repairing as necessary.

// const HEALTHY = 'GCTGGGTGGGACACTGTCGTTCCTTACCGCACCGCCACATCATTCACCCTTGGGCAACCC'
// let sample1 = 'GCTGGGTGGGACACTGTCGTTCCTTACCGCACCGCCACATCATTCACCCTTGGGCAACCC'
// let sample2 = 'GCTZGGTGGGZCACTGTCGTTCCTTACCGCACCGCCACATCATTCACCCTZGGGCAACCC'

// // Our bot needs to look through each sample for the String Z and replace it with the corresponding letter from the HEALTHY sequence. (And no, it can't simply copy the entire String...that's cheating!)

// // The first thing we need to understand is that unlike Arrays, you cannot update individual letters in a String. However, we can copy individual letters into a new Array.

// // The first version of our program copies each letter into the new sequence Array using a for-loop, then converts it a String using the .join() method:

// const HEALTHY = 'GCTGGGTGGGACACTGTCGTTCCTTACCGCACCGCCACATCATTCACCCTTGGGCAACCC';
// let sample1 = 'GCTGGGTGGGACACTGTCGTTCCTTACCGCACCGCCACATCATTCACCCTTGGGCAACCC';
// let sample2 = 'GCTZGGTGGGZCACTGTCGTTCCTTACCGCACCGCCACATCATTCACCCTZGGGCAACCC';
// let sequence = []

// for (let i = 0; i < sample1.length; i++) {
//     sequence.push(sample1[i])
// } 
// sequence = sequence.join('')

// Next, before we copy the letter into the sequence Array, we should check if that letter is Z:

const HEALTHY = 'GCTGGGTGGGACACTGTCGTTCCTTACCGCACCGCCACATCATTCACCCTTGGGCAACCC';
let sample1 = 'GCTGGGTGGGACACTGTCGTTCCTTACCGCACCGCCACATCATTCACCCTTGGGCAACCC';
let sample2 = 'GCTZGGTGGGZCACTGTCGTTCCTTACCGCACCGCCACATCATTCACCCTZGGGCAACCC';
let sequence = []

for (let i = 0; i<sample1.length; i++) {
  const letter = sample1[i];
  if (letter === 'Z') {
    sequence.push(HEALTHY[i])
  } else {
    sequence.push(letter)
  }
}
sequence = sequence.join('')


