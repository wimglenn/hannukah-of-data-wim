"""
The Investigator
https://hanukkah.bluebird.sh/5784/1/
"""
from hod.data import customers

d = str.maketrans("abcdefghijklmnopqrstuvwxyz", "22233344455566677778889999")

for _, customer in customers.items():
    lastname = customer["name"].split()[-1].lower()
    phone = customer["phone"].replace("-", "")
    if lastname.translate(d) == phone:
        result = customer
        break


if __name__ == "__main__":
    print(result["phone"], __doc__.splitlines()[1])
