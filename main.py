products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream",
            "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# total price average for all products
total_price = 0
for price in prices:
    total_price += price


total_price_average = round(total_price / len(prices), 2)
print(total_price, total_price_average)

# new price list that reduces the old prices by $ 5
new_price_list = []
for price in prices:
    new_price_list.append(price - 5)
print(new_price_list)


