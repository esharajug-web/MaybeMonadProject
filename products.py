from maybe import Maybe

# Product database
products = {
    101: {"name": "Laptop", "price": 1500, "discount": 25},
    102: {"name": "Headphones", "price": 200, "discount": 15},
    103: {"name": "Keyboard", "price": 70, "discount": 5},
    104: {"name": "Mouse", "price": 45, "discount": 0},
    105: {"name": "Monitor", "price": 300, "discount": 30}
}


# Traditional implementation
def search_product(product_id):
    if product_id in products:
        return products[product_id]
    return None


def calculate_final_price(product):
    if product is None:
        return None

    price = product["price"]
    discount = product["discount"]

    final_price = price - (price * discount / 100)
    return final_price


def display_product(product_id):
    product = search_product(product_id)

    if product is not None:
        final_price = calculate_final_price(product)

        print("Product:", product["name"])
        print("Original Price: $", product["price"])
        print("Discount:", product["discount"], "%")
        print("Final Price: $", final_price)

    else:
        print("Product not found.")


# Maybe Monad implementation
def search_product_maybe(product_id):
    product = products.get(product_id)
    return Maybe(product)


def get_product_name(product):
    return product["name"]


def calculate_discounted_price(product):
    price = product["price"]
    discount = product["discount"]

    final_price = price - (price * discount / 100)
    return Maybe(final_price)


def display_product_maybe(product_id):
    product_result = search_product_maybe(product_id)

    if product_result.value is None:
        print("Product not found.")
        return

    product = product_result.value

    product_name = product_result.map(get_product_name)

    final_price = product_result.flat_map(
        calculate_discounted_price
    )

    print("Product:", product_name.get_or_else("Unknown"))
    print("Original Price: $", product["price"])
    print("Discount:", product["discount"], "%")
    print("Final Price: $", final_price.get_or_else(0))


# Chained operations
def get_final_price(product_id):
    result = (
        search_product_maybe(product_id)
        .flat_map(calculate_discounted_price)
        .map(lambda price: round(price, 2))
    )

    return result.get_or_else("Product not found")