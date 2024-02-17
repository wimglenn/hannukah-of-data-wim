"""
The Bargain Hunter
https://hanukkah.bluebird.sh/5784/6/
"""
from collections import Counter

from hod.data import customers
from hod.data import orders
from hod.data import products


counter = Counter()
for order in orders.values():
    customer_id = order["customerid"]
    for item in order["items"]:
        sku = item["sku"]
        product = products[sku]
        if item["unit_price"] <= product["wholesale_cost"]:
            counter[customer_id] += 1
result = customers[max(counter, key=counter.get)]


if __name__ == "__main__":
    print(result["phone"], __doc__.splitlines()[1])
