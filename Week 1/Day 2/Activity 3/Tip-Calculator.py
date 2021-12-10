print("This program caluclate how much your tip should be")

total_amount = float(input("How much was your meal?: "))
tip_percentage = float(input("How much would you like to tip using 2 decimal places: "))

def tip_total():
    total_tip = (total_amount * tip_percentage)
    print(round(total_tip, 2))

tip_total()