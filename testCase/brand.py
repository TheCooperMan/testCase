class Brand:

    def __init__(self, brand_contact_url, brand_name, total_products, total_sells, total_likes, is_top_seller, location, rating):
        self.brand_contact_url = brand_contact_url
        self.brand_name = brand_name
        self.total_products = total_products
        self.total_sells = total_sells
        self.total_likes = total_likes
        self.is_top_seller = is_top_seller
        self.location = location
        self.rating = rating
        self.score = None

    def set_score(self, score):
        self.score = score
