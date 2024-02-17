"""
The Collector
https://hanukkah.bluebird.sh/5784/8/
"""
from collections import Counter

from hod.data import customers
from hod.data import orders

counter = Counter()
for order in orders.values():
    for item in order["items"]:
        if item["sku"].startswith("COL"):
            counter[order["customerid"]] += 1

[(customer_id, _)] = counter.most_common(1)
result = customers[customer_id]


if __name__ == "__main__":
    print(result["phone"], __doc__.splitlines()[1])
