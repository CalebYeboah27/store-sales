products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream",
            "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# total price average for all products
total_price = 0
for price in prices:
    total_price += price


total_price_average = round(total_price / len(prices), 2)
print(total_price_average)

# new price list that reduces the old prices by $ 5
new_prices = []
for price in prices:
    new_prices.append(price - 5)
print(new_prices)


# initialize the accumulator variable
daily_revenue = []
total_revenue = 0
# Check if the two lists are
# equal in number of elements
if (len(prices) == len(last_week)):
    # use the range function to create a single loop
    # to prevent the effects of a nested loop
    for i in range(len(prices)):
        product = prices[i] * last_week[i]
        daily_revenue.append(product)
        # acumulate the revenue
        total_revenue += product
    print(daily_revenue)
    print(total_revenue)
else:
    print("Lists have different lenght cannot perform the operation")

# average daily revenue generated from the products
average_daily_revenue = round(total_revenue / len(daily_revenue))
print(average_daily_revenue)

# products are less than $ 30 based on new price
products_less_than_30 = []
for i in range(len(new_prices)):
    if new_prices[i] < 30:
        products_and_newprice = {products[i]:  new_prices[i]}
        products_less_than_30.append(products_and_newprice)
print(products_less_than_30)
