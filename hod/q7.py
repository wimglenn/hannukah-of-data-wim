"""
The Meet Cute
https://hanukkah.bluebird.sh/5784/7/
"""
from datetime import timedelta
from functools import cache

from hod.data import customers
from hod.data import orders
from hod.data import products
from hod.q6 import result as bargain_hunter


@cache
def is_col(sku):
    return products[sku]["desc"].endswith(")")


bargain_hunter_orders = []
for order in orders.values():
    if order["customerid"] == bargain_hunter["customerid"]:
        for item in order["items"]:
            if is_col(item["sku"]):
                bargain_hunter_orders.append(order)

collisions = []
for order in orders.values():
    if order["customerid"] == bargain_hunter["customerid"]:
        continue
    for item in order["items"]:
        if is_col(item["sku"]):
            for bargain_hunter_order in bargain_hunter_orders:
                delta = abs(bargain_hunter_order["shipped"] - order["shipped"])
                if delta <= timedelta(minutes=1):
                    collisions.append((order, bargain_hunter_order))

candidates = []
for order, bargain_hunter_order in collisions:
    items = [i for i in order["items"] if is_col(i["sku"])]
    bargain_hunter_items = [i for i in bargain_hunter_order["items"] if is_col(i["sku"])]
    names = {products[i["sku"]]["desc"].rsplit(None, 1)[0] for i in items}
    bargain_hunter_names = {products[i["sku"]]["desc"].rsplit(None, 1)[0] for i in bargain_hunter_items}
    if names & bargain_hunter_names:
        candidates.append(order)

[order] = candidates
result = customers[order["customerid"]]


if __name__ == "__main__":
    print(result["phone"], __doc__.splitlines()[1])
