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

    # Test that map does not execute when the value is None
    result = Maybe(None).map(lambda x: x * 2)
    assert result.value is None

    # Test that flat_map does not execute when the value is None
    result = Maybe(None).flat_map(lambda x: Maybe(x + 5))
    assert result.value is None

    # Test is_present
    assert Maybe(10).is_present() is True
    assert Maybe(None).is_present() is False

    # Test is_empty
    assert Maybe(10).is_empty() is False
    assert Maybe(None).is_empty() is True
    
    print("Maybe Monad tests passed!")


# Run all tests
def test_maybe_filter():
    # Value satisfies the condition
    result = Maybe(10).filter(lambda x: x > 5)
    assert result.value == 10

    # Value does not satisfy the condition
    result = Maybe(3).filter(lambda x: x > 5)
    assert result.value is None

    # Empty Maybe remains empty
    result = Maybe(None).filter(lambda x: x > 5)
    assert result.value is None

    # Filtering a string
    result = Maybe("Python").filter(lambda x: len(x) > 3)
    assert result.value == "Python"

    print("Maybe filter tests passed!")

def test_maybe_extra_methods():
    assert Maybe(10).contains(10) is True
    assert Maybe(10).contains(5) is False
    assert Maybe(None).contains(10) is False

    assert Maybe(10).exists(lambda x: x > 5) is True
    assert Maybe(3).exists(lambda x: x > 5) is False
    assert Maybe(None).exists(lambda x: x > 5) is False

    print("Maybe extra methods tests passed!")    

    

if __name__ == "__main__":
    test_product_prices()
    test_missing_product()
    test_maybe_monad()
    test_maybe_filter()
    test_maybe_extra_methods()

    print("\nAll tests passed successfully!")