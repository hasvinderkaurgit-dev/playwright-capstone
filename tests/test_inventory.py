import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize(
	"selected_items, items_to_remove",
	[
		(["sauce-labs-backpack"], ["sauce-labs-backpack"]),
		(["sauce-labs-backpack", "sauce-labs-bike-light"], ["sauce-labs-backpack"]),
		(
			["sauce-labs-backpack", "sauce-labs-bike-light", "sauce-labs-bolt-t-shirt"],
			["sauce-labs-bike-light", "sauce-labs-bolt-t-shirt"],
		),
		(["sauce-labs-onesie", "sauce-labs-fleece-jacket"], ["sauce-labs-onesie"]),
	],
)


def test_add_and_partial_remove(
	# add phase
	inventory_page, selected_items: list[str], items_to_remove: list[str]
):
	for added_count, item in enumerate(selected_items, start=1):
		inventory_page.add_to_cart(item)
		expect(inventory_page.cart_badge).to_have_text(str(added_count))

    # partial remove
	for item in items_to_remove:
		inventory_page.remove_from_cart (item)
	expected_count = len(selected_items) - len(items_to_remove)
	if expected_count:
		expect(inventory_page.cart_badge).to_have_text(str(expected_count))
	else:
		expect(inventory_page.cart_badge).to_have_count(0)

    #final remove
	remaining_items = [item for item in selected_items if item not in items_to_remove]
	expected_remaining = [item for item in remaining_items]
	for item in remaining_items:
		inventory_page.remove_from_cart(item)
	if expected_count:
		expect(inventory_page.cart_badge).to_have_count(0)

#A to Z and Z to A sorting tests
@pytest.mark.parametrize("option, reverse", [
	("Name (A to Z)", False),
	("Name (Z to A)", True),
])
def test_sort_by_name(inventory_page, option, reverse):
    names = inventory_page.item_names.all_text_contents()   # default order, before sorting
    inventory_page.apply_filter(option)
    expect(inventory_page.item_names).to_have_text(sorted(names, reverse=reverse))

#Price sorting tests
@pytest.mark.parametrize("option, reverse", [
    ("Price (low to high)", False),
    ("Price (high to low)", True),
])

def test_sort_by_price(inventory_page, option, reverse):
    inventory_page.apply_filter(option)
    prices = [
		float(price.replace("$", ""))
        for price in inventory_page.item_prices.all_text_contents()
    ]
    expected = [f"${price:.2f}" for price in sorted(prices, reverse=reverse)]
    expect(inventory_page.item_prices).to_have_text(expected)
