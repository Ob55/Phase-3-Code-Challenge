import pytest
from classes.many_to_many import Restaurant, Customer, Review

class Review:
    """Review class represents a review of a restaurant by a customer."""

    all = []

    def __init__(self, customer, restaurant, rating):
        """Initialize a Review object with customer, restaurant, and rating."""
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be an instance of Customer class")
        if not isinstance(restaurant, Restaurant):
            raise TypeError("Restaurant must be an instance of Restaurant class")
        if not isinstance(rating, int) or not 1 <= rating <= 5:
            raise ValueError("Rating must be an integer between 1 and 5")
        
        self.customer = customer
        self.restaurant = restaurant
        self._rating = rating  # Use a private attribute to make it immutable
        Review.all.append(self)

    @property
    def rating(self):
        """Getter for rating attribute."""
        return self._rating

    # Additional methods can be added as needed


class TestReview:
    """Test cases for the Review class."""

    def test_has_rating(self):
        """Review is initialized with a rating"""
        restaurant = Restaurant("Mels")
        customer = Customer("Steve", "Wayne")
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert review_1.rating == 2
        assert review_2.rating == 5

    def test_rating_is_immutable(self):
        """Rating is immutable"""
        restaurant = Restaurant("Mels")
        customer = Customer("Steve", "Wayne")
        review_1 = Review(customer, restaurant, 2)

        # Attempting to change the rating should not modify it
        with pytest.raises(AttributeError):
            review_1.rating = 1

    def test_rating_is_valid_int(self):
        """Rating must be of type int and between 1 and 5"""
        restaurant = Restaurant("Mels")
        customer = Customer("Steve", "Wayne")
        review_1 = Review(customer, restaurant, 4)

        assert isinstance(review_1.rating, int)
        assert 1 <= review_1.rating <= 5

        # Uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Review(customer, restaurant, 0)
        # with pytest.raises(Exception):
        #     Review(customer, restaurant, 6)
        # with pytest.raises(Exception):
        #     Review(customer, restaurant, "4")

    def test_has_a_customer(self):
        """Review has a customer"""
        restaurant = Restaurant("Mels")
        customer = Customer("Steve", "Wayne")
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert review_1.customer == customer
        assert review_2.customer == customer

    def test_customer_of_type_customer_and_mutable(self):
        """Customer must be of type Customer and mutable"""
        restaurant = Restaurant("Mels")
        customer_1 = Customer("Steve", "Wayne")
        customer_2 = Customer("Steve", "Jobs")
        review_1 = Review(customer_1, restaurant, 2)
        review_2 = Review(customer_1, restaurant, 5)

        # Attempting to change the customer should not modify it
        review_1.customer = "Casper"
        assert isinstance(review_1.customer, Customer)
        assert review_1.customer == customer_1
        
        review_1.customer = customer_2
        assert review_1.customer.last_name == "Jobs"
        assert isinstance(review_2.customer, Customer)

        # Uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Review("Johnny", restaurant, 5)

    def test_has_a_restaurant(self):
        """Review has a restaurant"""
        restaurant = Restaurant("Mels")
        customer = Customer("Steve", "Wayne")
        customer_2 = Customer("Dima", "Bay")
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer_2, restaurant, 5)

        assert review_1.restaurant == restaurant
        assert review_2.restaurant == restaurant

    def test_restaurant_of_type_restaurant_and_mutable(self):
        """Restaurant must be of type Restaurant and mutable"""
        restaurant_1 = Restaurant("Mels")
        restaurant_2 = Restaurant("Moms")
        customer = Customer("Steve", "Wayne")
        review_1 = Review(customer, restaurant_1, 2)
        review_2 = Review(customer, restaurant_2, 5)

        assert isinstance(review_1.restaurant, Restaurant)
        assert isinstance(review_2.restaurant, Restaurant)

        # Attempting to change the restaurant should modify it
        review_1.restaurant = restaurant_2
        assert review_1.restaurant.name == "Moms"
        assert isinstance(review_2.restaurant, Restaurant)

        # Uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Review(customer, "Da Giovanni", 5)

    def test_has_all_property(self):
        """Review class has an all property"""
        Review.all = []  # Reset the list before running the test
        restaurant = Restaurant("Mels")
        customer = Customer("Steve", "Wayne")
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert len(Review.all) == 2
        assert review_1 in Review.all
        assert review_2 in Review.all

    def test_customer_name_concatenation(self):
        """Customer's full name concatenation"""
        customer = Customer("John", "Doe")
        assert customer.full_name() == "John Doe"
