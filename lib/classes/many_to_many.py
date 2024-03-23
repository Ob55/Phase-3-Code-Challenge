class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reviews_list = []  # To store reviews authored by the customer

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str) or len(value) < 1 or len(value) > 25:
            raise ValueError("First name must be a string between 1 and 25 characters.")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str) or len(value) < 1 or len(value) > 25:
            raise ValueError("Last name must be a string between 1 and 25 characters.")
        self._last_name = value

    def reviews(self):
        return self.reviews_list

    def restaurants(self):
        return list({review.restaurant for review in self.reviews_list})

    def num_negative_reviews(self):
        return sum(1 for review in self.reviews_list if review.rating <= 2)

    def has_reviewed_restaurant(self, restaurant):
        return any(review.restaurant == restaurant for review in self.reviews_list)


class Restaurant:
    all_restaurants = []  # Class variable to store all restaurant instances

    def __init__(self, name):
        self.name = name
        self.reviews_list = []  # To store reviews of the restaurant
        self.all_restaurants.append(self)  # Add the restaurant to the list of all restaurants

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 1:
            raise ValueError("Restaurant name must be a non-empty string.")
        self._name = value

    def add_review(self, review):
        self.reviews_list.append(review)

    def add_customer(self, customer):
        for review in self.reviews_list:
            if review.customer == customer:
                return
        raise ValueError("Customer has not reviewed this restaurant.")

    def reviews(self):
        return self.reviews_list

    def customers(self):
        return list({review.customer for review in self.reviews_list})

    def average_star_rating(self):
        if not self.reviews_list:
            return 0.0
        total_rating = sum(review.rating for review in self.reviews_list)
        return round(total_rating / len(self.reviews_list), 1)

    @classmethod
    def top_two_restaurants(cls):
        sorted_restaurants = sorted(cls.all_restaurants, key=lambda r: r.average_star_rating(), reverse=True)
        return sorted_restaurants[:2]


class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int) or value < 1 or value > 5:
            raise ValueError("Rating must be an integer between 1 and 5.")
        self._rating = value
