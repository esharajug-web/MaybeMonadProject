from products import (
    display_product,
    display_product_maybe,
    get_final_price
)


# Demonstration 1: Traditional Implementation
print("\n========== TRADITIONAL IMPLEMENTATION ==========")

print("\nSearching for Product ID 102:")
display_product(102)

print("\nSearching for missing Product ID 999:")
display_product(999)


# Demonstration 2: Maybe Monad Implementation
print("\n========== MAYBE MONAD IMPLEMENTATION ==========")

print("\nSearching for Product ID 102:")
display_product_maybe(102)

print("\nSearching for missing Product ID 999:")
display_product_maybe(999)


# Demonstration 3: Chained Operations
print("\n========== CHAINED OPERATIONS ==========")

print("Laptop final price:", get_final_price(101))
print("Headphones final price:", get_final_price(102))
print("Keyboard final price:", get_final_price(103))
print("Mouse final price:", get_final_price(104))
print("Monitor final price:", get_final_price(105))
print("Missing product:", get_final_price(999))


# Demonstration 4: Interactive Search
print("\n========== INTERACTIVE PRODUCT SEARCH ==========")

try:
    product_id = int(input("Enter Product ID: "))
    result = get_final_price(product_id)

    print("Final Price:", result)

except ValueError:
    print("Please enter a valid numeric Product ID.")