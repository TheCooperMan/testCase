AVG_TOTAL_PRODUCT = 1000
AVG_TOTAL_SELLS = 10000
AVG_TOTAL_LIKES = 500


class Scoring:

    def __init__(self, brand):
        self.brand = brand

    def get_score(self):
        return self.get_total_product_score() + self.get_total_sells_score() + self.get_total_likes_score() + self.get_rating_score() + self.get_is_top_seller_score()

    def get_total_product_score(self):
        total_products = self.brand.total_products
        if total_products:
            if total_products >= AVG_TOTAL_PRODUCT:
                return 2
            elif total_products >= AVG_TOTAL_PRODUCT / 2:
                return 1.5
            elif total_products >= AVG_TOTAL_PRODUCT / 10:
                return 1
            return 0
        else:
            return 0

    def get_total_sells_score(self):
        total_sells = self.brand.total_sells
        if total_sells >= AVG_TOTAL_PRODUCT:
            return 2
        elif total_sells >= AVG_TOTAL_PRODUCT / 10:
            return 1.5
        elif total_sells >= AVG_TOTAL_PRODUCT / 100:
            return 1
        return 0

    def get_total_likes_score(self):
        total_likes = self.brand.total_likes
        if total_likes:
            if total_likes >= AVG_TOTAL_PRODUCT:
                return 2
            elif total_likes >= AVG_TOTAL_PRODUCT / 2:
                return 1.5
            elif total_likes >= AVG_TOTAL_PRODUCT / 5:
                return 1
            return 0
        else:
            return 0

    def get_rating_score(self):
        total_rating = self.brand.rating
        if total_rating >= 4.5:
            return 2
        elif total_rating >= 3:
            return 1.5
        elif total_rating >= 2:
            return 1
        return 0

    def get_is_top_seller_score(self):
        if self.brand.is_top_seller:
            return 2
        else:
            return 0
