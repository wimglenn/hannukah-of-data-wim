"""
The Contractor
https://hanukkah.bluebird.sh/5784/2/
"""
from hod.data import customers
from hod.data import orders
from hod.data import products
from hod.data import speedrun

candidate_customers = set()
for customer_id, customer in customers.items():
    names = customer["name"].upper().split()
    initials = names[0][0] + names[1][0]
    seek = "DS" if speedrun else "JP"
    if seek == initials:
        candidate_customers.add(customer_id)

[sku] = [s for s, p in products.items() if p["desc"] == "Rug Cleaner"]

custids = set()
for oid, o in orders.items():
    if o["customerid"] in candidate_customers:
        if any(i["sku"] == sku for i in o["items"]):
            if o["ordered"].year == 2017 or o["shipped"].year == 2017:
                custids.add(o["customerid"])
[custid] = custids
result = customers[custid]


if __name__ == "__main__":
    print(result["phone"], __doc__.splitlines()[1])
