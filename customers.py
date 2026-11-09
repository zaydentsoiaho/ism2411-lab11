#ISM2411 Lab 11 - Customer Dictionary & Lookup 
# Name: Zayden Tsoiaho 

#REFLECTION 1:
# I would use .get() for optional information like an email since
#it gives a default value when the key is missing. I would use brackets
#for information that should always be there regardless so I can notice and fix the missing data

#REFLECTION 2:
#It reminds me of using a Pivot Table because it can group data such as sales
#by region and add up the different amounts. Python can handle larger datasets than the Excel 
#Worksheet limit if there is enough memory and the code can be used on different data

#Exercise 1: One Customer 
customer = {
    "name": "Zayden",
    "email": "zayden@example.com",
    "tier": "silver",
    "ytd_spend": 2800,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

#Exercise 2: Update and add
customer["phone"] = "407-555-0123"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


#Exercise 3: Safe lookup

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError as error:
    print("KeyError caught:", error)


#Exercise 4: Iterate

for key, value in customer.items():
    print(f"{key}: {value}")

# .items() gives both the key and values.
#Without .items(), the loop gives only keys.

for key in customer: 
    print(key)

#Exercise 5: Lookup table
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15, 
}

discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = 200 * (1-discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount: {discount_rate:.0%}")
print(f"Final price: ${final_price:.2f}")

#Exercise 6: List of dicts 
customers = [
    {"name": "Michael", "tier": "bronze"},
    {"name": "Jaxson", "tier": "gold"},
    {"name": "Adam", "tier": "platinum"},
]

for record in customers: 
    rate = tier_discounts.get(record["tier"],0)
    discount = 300 * rate
    print(f"{record['name']}, {record['tier']}: ${discount:.2f} off a $300 purchase")

#Exercise 7: Nested Catalog
catalog = {
    "Widget A":{"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product}, stock: {details['stock']}")


#Exercise 8: Sales by Region

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_by_region = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")