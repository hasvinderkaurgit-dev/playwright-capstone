
class InventoryPage():
	URL = "https://www.saucedemo.com/inventory.html"


	def __init__(self, page):
		self.page = page
		self.SORT_DROPDOWN = "[data-test='product-sort-container']"
		self.item_names = page.locator(".inventory_item_name")
		self.item_prices = page.locator(".inventory_item_price")
		self.cart_badge = page.locator(".shopping_cart_badge")

	def load(self):
		self.page.goto(self.URL)
		return self

	def is_loaded(self):
		return "inventory.html" in self.page.url

	def add_to_cart(self, product_id):
		self.page.locator(f"#add-to-cart-{product_id}").click()
		return self

	def remove_from_cart(self, product_id):
		self.page.locator(f"#remove-{product_id}").click()
		return self

	def apply_filter(self, option_text):
		"""Apply a filter from the sort dropdown."""
		self.page.locator(self.SORT_DROPDOWN).select_option(label=option_text)
		return self


	def get_item_prices(self):
		prices = self.item_prices.all_text_contents()
		return [float(price.replace("$", "")) for price in prices]
