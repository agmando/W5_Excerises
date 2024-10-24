address_book = {
    "name":"Freddy Kruger",
    "address":"1010 Elm Street",
    "city":"Chicago",
    "state":"Illinois",
    "zip":"60634"

}

print(f"""
{address_book['name']}
{address_book['address']}
{address_book['city']}, {address_book['state']} {address_book['zip']}
""")


address_book.pop("name")

full_name = {"first name": "Freddy", "last name": "Kruger"}

address_book.update({"honorific": "Mr."})

print(f"""
{address_book['honorific']} {full_name['first name']} {full_name['last name']}
{address_book['address']}
{address_book['city']}, {address_book['state']} {address_book['zip']}
""")