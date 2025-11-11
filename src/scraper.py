thonimport requests
import json

class ShopeeScraper:
    def __init__(self, cookies):
        self.headers = {
            'User-Agent': 'Mozilla/5.0',
            'Cookie': cookies
        }
        self.base_url = "https://shopee.com.my/api/v2"

    def get_product_details(self, product_id):
        url = f"{self.base_url}/item/get"
        params = {'itemid': product_id}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_shop_details(self, shop_id):
        url = f"{self.base_url}/shop/get_shop_info"
        params = {'shopid': shop_id}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_category_products(self, category_id, limit=50):
        url = f"{self.base_url}/search_items"
        params = {'category': category_id, 'limit': limit}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_flash_sales(self):
        url = f"{self.base_url}/flash_sale/get_flash_sale_items"
        response = requests.get(url, headers=self.headers)
        return response.json()