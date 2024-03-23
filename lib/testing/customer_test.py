import pytest
from classes.many_to_many import Restaurant, Customer, Review

class TestCustomer:
    """Test cases for the Customer class."""

    def test_has_names(self):
        """Customer is initialized with first name and last name"""
        customer = Customer("Steve", "Wayne")
        assert customer.first_name == "Steve"
        assert customer.last_name == "Wayne"

    def test_names_are_mutable_strings(self):
        """Names must be of type str and mutable"""
        customer = Customer("Ned", "Stark")

        assert isinstance(customer.first_name, str)
        assert isinstance(customer.last_name, str)

        customer.first_name = "Rob"
        customer.last_name = "Stark"
        assert customer.first_name == "Rob"
        assert customer.last_name == "Stark"

    def test_names_are_valid(self):
        """First and last names must be between 1 and 25 characters, inclusive"""
        customer = Customer("Steve", "Wayne")

        assert 1 <= len(customer.first_name) <= 25
        assert 1 <= len(customer.last_name) <= 25

        with pytest.raises(ValueError):
            Customer("", "Wayne")

        with pytest.raises(ValueError):
            Customer("Steve", "")

        with pytest.raises(ValueError):
            Customer("F" * 26, "Wayne")

        with pytest.raises(ValueError):
            Customer("Steve", "F" * 26)

        assert customer.first_name == "Steve"
        assert customer.last_name == "Wayne"

    def test_has_many_reviews(self):
        """Customer has many reviews"""
        restaurant = Restaurant("Mels")
        customer = Customer("Steve", "Wayne")
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert len(customer.reviews()) == 2
        assert review_1 in customer.reviews()
        assert review_2 in customer.reviews()

    def test_reviews_of_type_review(self):
        """Reviews must be of type Review"""
        customer = Customer("Ned", "Stark")
        restaurant = Restaurant("Lento")
        review_1 = Review(customer, restaurant, 5)
        review_2 = Review(customer, restaurant, 2)

        assert isinstance(customer.reviews()[0], Review)
        assert isinstance(customer.reviews()[1], Review)

    def test_has_many_restaurants(self):
        """Customer has many restaurants"""
        restaurant = Restaurant("Mels")
        restaurant_2 = Restaurant("Chipotle")
        customer = Customer("Steve", "Wayne")
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant_2, 5)

        assert restaurant in customer.restaurants()
        assert restaurant_2 in customer.restaurants()

    # Other test methods...

if __name__ == "__main__":
    pytest.main()
