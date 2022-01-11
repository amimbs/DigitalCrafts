// people < 4 tip : 10%
// people >4 < 6: 15%
// people >6 < 10: 20%
// people >10: 25%
// THE AMOUNT OF ITEMS IS THE AMOUNT OF PEOPLE

function totalWithTip(items) {
    let subtotal = 0;
    let tip_rate = 0;
    let people = items.length
  
    for (let i = 0; i < items.length; i = i + 1) {
      subtotal = subtotal + items[i]
    }

    if (people < 4) {
        tip_rate = 0.1
    } else if (people < 6) {
        tip_rate = 0.15
    } else if (people < 10) {
        tip_rate = 20
    } else {
        tip_rate = 0.25
    }
  
    // if (subtotal < 100) {
    //   tip_rate = 0.1;
    // } else if (subtotal < 200) {
    //   tip_rate = 0.2;
    // } else if (subtotal < 300) {
    //   tip_rate = 0.3;
    // } else {
    //   tip_rate = 0.5
    // }
  
    const tip = subtotal * tip_rate;
    return {
        total: subtotal + tip,
        tip_rate: tip_rate,
        people: people
    }
  }
  
  let receipt = totalWithTip([5, 10, 15, 20, 100, 500, 30, 20, 60, 70, 50]);
  let total2 = totalWithTip([5, 10]);
  let total3 = totalWithTip([5, 10, 15, 20]);

  // back ticks allow literal strings using ${}
  console.log(`For a party of ${receipt.people} people, with a tip rate of ${receipt.tip_rate * 100}% Your total should be $${receipt.total} `)