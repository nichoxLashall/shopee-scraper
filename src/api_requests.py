thonfrom scraper import ShopeeScraper

class APIRequests:
    def __init__(self, cookies):
        self.scraper = ShopeeScraper(cookies)

    def fetch_product_data(self, product_id):
        return self.scraper.get_product_details(product_id)

    def fetch_shop_data(self, shop_id):
        return self.scraper.get_shop_details(shop_id)

    def fetch_category_data(self, category_id, limit=50):
        return self.scraper.get_category_products(category_id, limit)

    def fetch_flash_sales_data(self):
        return self.scraper.get_flash_sales()