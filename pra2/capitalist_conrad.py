import random

MAX_INCREASE = 0.175  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "data.txt"

price = INITIAL_PRICE
print("Startin price: ${:,.2f}".format(price))
day = 0
out_file = open(OUTPUT_FILE, 'w')
while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
               # generate a random integer of 1 or 2
                      #  if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:         # generate a random floating-point number
                                          #  between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
        day += 1
    else:         # generate a random floating-point number
                  #  between negative MAX_INCREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)
        day += 1
    price *= (1 + price_change)
    print("On day {} price is: {:.2f} ".format(day, price))

out_file.close()
