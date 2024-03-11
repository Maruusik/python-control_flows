def calculate_discount(price, discount_percent):
    # calculate the discount percentage for the price
    original_price = 1000
    discount_percent = 25

    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price 


# Prompt the user for the original price and discount percentage
original_price = float(input("Enter the original price of the item: $: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price after applying the discount
final_price = calculate_discount(original_price, discount_percent)

# Print the final price
if final_price!= original_price:
    print("Final price after applying the discount: ${:.2f}".format(final_price))
else:
    print("No discount applied. Original price: ${:.2f}".format(original_price))