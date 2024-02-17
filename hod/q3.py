"""
The Neighbor
https://hanukkah.bluebird.sh/5784/1/
"""
from datetime import date

from hod.data import customers
from hod.data import haversine
from hod.data import speedrun
from hod.q2 import result as contractor


# Years of the rabbit: 2035, 2023, 2011, 1999, 1987, 1975, 1963, 1951, 1939, 1927...
# Years of the goat:   2027, 2015, 2003, 1991, 1979, 1967, 1955, 1943, 1931...
# Cancer (Jun 21 - Jul 22)
# Libra  (Sep 23 - Oct 22)
candidates = []
for customer in customers.values():
    dob = customer["birthdate"]
    div = 11 if speedrun else 7
    m_d0 = (9, 23) if speedrun else (6, 21)
    m_d1 = (10, 22) if speedrun else (7, 22)
    if dob.year % 12 == div:
        d0 = date(dob.year, *m_d0)
        d1 = date(dob.year, *m_d1)
        if d0 <= dob <= d1:
            candidates.append(customer)


def key(rabbit):
    return haversine(contractor["lat"], contractor["long"], rabbit["lat"], rabbit["long"])


result = min(candidates, key=key)


if __name__ == "__main__":
    print(result["phone"], __doc__.splitlines()[1])
