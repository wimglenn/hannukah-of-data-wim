"""
The Early Bird
https://hanukkah.bluebird.sh/5784/1/
"""
from collections import Counter

from hod.data import customers
from hod.data import orders


counter = Counter()
for order in orders.values():
    items = order["items"]
    n_pastries = sum(item["qty"] for item in items if item["sku"].startswith("BKY"))
    if n_pastries > 1:
        if order["shipped"].hour <= 5:
            counter[order["customerid"]] += 1
customer_id = max(counter, key=counter.get)
result = customers[customer_id]


if __name__ == "__main__":
    print(result["phone"], __doc__.splitlines()[1])
