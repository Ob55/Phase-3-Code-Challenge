import pytest
from classes.many_to_many import Restaurant, Customer, Review

class TestRestaurant:
    """Restaurant in many_to_many.py"""

    def test_has_name(self):
        """Restaurant is initialized with a name"""
        restaurant = Restaurant("Mel's")

        assert restaurant.name == "Mel's"

    def test_name_is_mutable_string(self):
        """name is a mutable string"""
        restaurant = Restaurant("Mel's")
        restaurant.name = "Mel'b"

        assert restaurant.name == "Mel'b"
        assert isinstance(restaurant.name, str)

        with pytest.raises(ValueError):
            restaurant.name = 4

    def test_name_is_valid(self):
        """name must be 1 or more characters long"""
        restaurant = Restaurant("Mel's")
        assert len(restaurant.name) > 0
        
        with pytest.raises(ValueError):
            restaurant.name = ""

    def test_has_many_reviews(self):
        """restaurant has many reviews"""
        restaurant = Restaurant("Mels")
        customer = Customer("Steve", "Wayne")
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert len(restaurant.reviews()) == 2  # Fixed

    def test_reviews_of_type_review(self):
        """restaurant reviews are of type Review"""
        restaurant = Restaurant("Truluck's")
        customer = Customer("Bruce", "Miller")
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert isinstance(restaurant.reviews()[0], Review)
        assert isinstance(restaurant.reviews()[1], Review)

    def test_has_many_customers(self):
        """restaurant has many customers"""
        restaurant = Restaurant("Mels")
        customer = Customer("Steve", "Wayne")
        customer_2 = Customer("Dima", "Bay")
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer_2, restaurant, 5)

        assert len(restaurant.customers()) == 2  # Fixed

    def test_customers_of_type_customer(self):
        """customers must be of type Customer"""
        restaurant = Restaurant("Franklin's")
        customer = Customer("Bruce", "Miller")
        customer_2 = Customer("Dima", "Bay")
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer_2, restaurant, 5)

        assert isinstance(restaurant.customers()[0], Customer)
        assert isinstance(restaurant.customers()[1], Customer)

    def test_customers_are_unique(self):
        """customers are unique"""
        restaurant = Restaurant("Franklin's")
        customer_1 = Customer("Bruce", "Miller")
        customer_2 = Customer("Dima", "Bay")
        review_1 = Review(customer_1, restaurant, 2)
        review_2 = Review(customer_2, restaurant, 5)
        review_3 = Review(customer_1, restaurant, 3)

        assert len(set(restaurant.customers())) == len(restaurant.customers())  # Fixed

    def test_average_star_rating(self):
        """returns average of restaurant's review ratings"""

        restaurant = Restaurant("Mels")
        customer = Customer("Steve", "Wayne")
        customer_2 = Customer("Dima", "Bay")

        assert restaurant.average_star_rating() == 0.0

        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer_2, restaurant, 5)
        review_3 = Review(customer_2, restaurant, 4)

        assert restaurant.average_star_rating() == 3.7

    def test_top_two_restaurants(self):
        """returns the top 2 restaurants in descending order by average star rating"""
        Review.all = []
        restaurant_1 = Restaurant("Mels")
        restaurant_2 = Restaurant("IronMeal")
        restaurant_3 = Restaurant("Da Giovanni")
        restaurant_4 = Restaurant("Mel'b")
        customer = Customer("Steve", "Wayne")
        customer_2 = Customer("Dima", "Bay")
        review_1 = Review(customer, restaurant_1, 5)
        review_2 = Review(customer, restaurant_2, 4)
        review_3 = Review(customer, restaurant_3, 3)
        review_4 = Review(customer, restaurant_4, 2)
        review_5 = Review(customer_2, restaurant_1, 5)
        review_6 = Review(customer_2, restaurant_2, 5)
        review_7 = Review(customer_2, restaurant_3, 5)

        top_restaurants = Restaurant.top_two_restaurants()
        assert restaurant_1 in top_restaurants
        assert restaurant_2 in top_restaurants
        assert restaurant_3 not in top_restaurants
        assert restaurant_4 not in top_restaurants

        Review.all = []
        assert Restaurant.top_two_restaurants() is None

