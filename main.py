from products import (
    display_product,
    display_product_maybe,
    get_final_price
)


# Cell 1: Traditional OOP Demonstration
print("TRADITIONAL IMPLEMENTATION")
print("=========================")

display_product(102)

print("\nSearching for a missing product:")
display_product(999)


# Cell 2: Maybe Monad Demonstration
print("\nMAYBE MONAD IMPLEMENTATION")
print("=========================")

display_product_maybe(102)

print("\nSearching for a missing product:")
display_product_maybe(999)


# Cell 3: Test Chained Operations
print("\nTESTING CHAINED OPERATIONS")
print("==========================")

print("Product 101:", get_final_price(101))
print("Product 102:", get_final_price(102))
print("Product 103:", get_final_price(103))
print("Product 104:", get_final_price(104))
print("Product 105:", get_final_price(105))
print("Product 999:", get_final_price(999))


# Cell 4: Automated Testing
print("\nAUTOMATED TESTING")
print("=================")

assert get_final_price(101) == 1125.0
assert get_final_price(102) == 170.0
assert get_final_price(103) == 66.5
assert get_final_price(104) == 45.0
assert get_final_price(105) == 210.0
assert get_final_price(999) == "Product not found"

print("All test cases passed successfully!")


# Cell 5: Interactive Product Search
print("\nE-COMMERCE PRODUCT SEARCH SYSTEM")
print("================================")

product_id = int(input("Enter Product ID: "))

print("\nSearch Result:")
print("-------------")

print("Final Price:", get_final_price(product_id))