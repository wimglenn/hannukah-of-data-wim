"""
The Cat Lady
https://hanukkah.bluebird.sh/5784/5/
"""
from collections import Counter

from hod.data import customers
from hod.data import gender
from hod.data import orders
from hod.data import products
from hod.data import speedrun

cat_food = {sku for sku, product in products.items() if "Senior Cat Food" in product["desc"]}

counter = Counter()
for order in orders.values():
    item_skus = [item["sku"] for item in order["items"]]
    n_cat_foods = sum(1 for i in item_skus if i in cat_food)
    customer = customers[order["customerid"]]
    if speedrun or customer["citystatezip"].startswith("Staten Island"):
        counter[order["customerid"]] += n_cat_foods

cat_food_customers = dict(counter.most_common())
cat_ladies = []
for i, cust_id in enumerate(cat_food_customers):
    cat_person = customers[cust_id]
    first_name = cat_person["name"].split()[0]
    resp = gender(first_name)
    g = resp.get("gender", "female")
    confidence = resp.get("probability", 1.0)
    if confidence < 0.9 or (g == "female" and confidence >= 0.9):
        result = cat_person
        break


if __name__ == "__main__":
    print(result["phone"], __doc__.splitlines()[1])
