from products import get_final_price
from maybe import Maybe


# Test product prices
def test_product_prices():
    assert get_final_price(101) == 1125.0
    assert get_final_price(102) == 170.0
    assert get_final_price(103) == 66.5
    assert get_final_price(104) == 45.0
    assert get_final_price(105) == 210.0

    print("Product price tests passed!")


# Test missing product
def test_missing_product():
    assert get_final_price(999) == "Product not found"

    print("Missing product test passed!")


# Test Maybe Monad
def test_maybe_monad():
    maybe_value = Maybe(10)

    # Test map
    result = maybe_value.map(lambda x: x * 2)
    assert result.value == 20

    # Test flat_map
    result = maybe_value.flat_map(lambda x: Maybe(x + 5))
    assert result.value == 15

    # Test get_or_else
    result = Maybe(None).get_or_else(0)
    assert result == 0

    print("Maybe Monad tests passed!")


# Run all tests
if __name__ == "__main__":
    test_product_prices()
    test_missing_product()
    test_maybe_monad()

    print("\nAll tests passed successfully!")