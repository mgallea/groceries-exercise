# groceries.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

print(products)

#print the data types of the data structures
print("")
print("Metadata Test:")
print(type(products))
print(type(products[0]))

#print the name of the first product
print(products[0]["name"])

#print the first product
print(products[0])
print("")

#print the number of products
print("There are " + str(len(products)) + " products")
print("")

#define product_name
def product_name(any_product):
    return any_product["name"]

#sort the products by name
products = sorted(products, key=product_name)

#print each product

for item in products:
    print("+ " + item["name"] + " -- Price: $" + str("%0.2f" % item["price"]))

    
#count the number of departments
departments = [ ]
depCount = 0
for item in products:
    if item["department"] not in departments:
        departments.append(item["department"])
        depCount = depCount + 1

#sort the departments
departments = sorted(departments)

#print the departments header
print("")
print("There are " + str(depCount) + " departments")
print("")
print("The departments are:")

#print the number of departments and count of products in the department
for dep in departments:
    itemCounter = 0
    for item in products:
        if item["department"] == dep:
            itemCounter = itemCounter + 1
    if itemCounter > 1:
        print("+ " + dep + " has " + str(itemCounter) + " products")
    if itemCounter == 1:
        print("+ " + dep + " has " + str(itemCounter) + " product")
    if itemCounter < 1:
        print("+ " +    dep + " has " + str(itemCounter) + " products")

print("")
