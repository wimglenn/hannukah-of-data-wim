import os
import json
from datetime import date
from datetime import datetime
from functools import cache
from math import asin
from math import cos
from math import radians
from math import sin
from math import sqrt
from pathlib import Path

import urllib3

here = Path(__file__).parent

speedrun = int(os.environ.get("HOD_SPEEDRUN", "1"))

data = os.environ.get("HOD_DATA", "5784")
if speedrun:
    data += "-speedrun"
data_path = here.parent / data

customers_path = data_path / "noahs-customers.jsonl"
customers = [json.loads(x) for x in customers_path.read_text().splitlines()]
customers = {c["customerid"]: c for c in customers}
for c in customers.values():
    c["birthdate"] = date.fromisoformat(c["birthdate"])

orders_path = data_path / "noahs-orders.jsonl"
orders = [json.loads(x) for x in orders_path.read_text().splitlines()]
orders = {o.pop("orderid"): o for o in orders}
for o in orders.values():
    o["ordered"] = datetime.fromisoformat(o["ordered"])
    o["shipped"] = datetime.fromisoformat(o["shipped"])

products_path = data_path / "noahs-products.jsonl"
products = [json.loads(x) for x in products_path.read_text().splitlines()]
products = {p.pop("sku"): p for p in products}


@cache
def gender(name):
    return urllib3.request("GET", "https://api.genderize.io?name=" + name).json()


@cache
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6_378_137  # Radius of earth at sea level in meters
    r += 10  # elevation of nyc above sea level
    return c * r
