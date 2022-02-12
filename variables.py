from pprint import pprint

product = {
    "name": "iPhone 12",
    "stock": 24,
    "price": 65432.1
}
phones = ["iPhone 12", "Samsung Galaxy S21", "Xiaomi Mi11"]
product["recomaded"] = phones
pprint(product["recomaded"])
product["recomaded"].append("iPhone 9")
pprint(product)