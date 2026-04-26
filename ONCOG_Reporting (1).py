import json
from pathlib import Path

script_path = Path(__file__)
script_dir = script_path.parent
json_file = script_dir / 'database.json'

def load_file(filename = json_file) :
    with open(filename, 'r') as file :
        return json.load(file)
    
def save_file(data, filename = json_file):
    with open(filename, "w") as file:
        json.dump(data, file, indent = 4)

#b. Read

#Find all snacks in the "chips" category.
def find_chips():
    data = load_file()
    chips = [s for s in data["snacks"] if s["category"] == "chips"]
    for c in chips:
        print(f"{c["name"]}")

#Show all sales made by Grade 10 students.
def student_sales():
    data = load_file()
    grade_10 = [s["student_id"] for s in data["students"] if s["grade_level"] == 10]
    grade_10_sales = [sale for sale in data["sales"] if sale["student_id"] in grade_10]
    for s in grade_10_sales:
        print(f"Sale ID {s["sale_id"]}: {s["total_price"]} pesos.")

#Display the total quantity of snacks sold today. (Assuming that today is Monday.)
def total_snacks_sold():
    data = load_file()
    quantity_sold = 0
    for sale in data["sales"]:
        if sale["day"] == "Monday":
            quantity_sold += sale["quantity"]
    print(f"Total quantity of snacks sold on Monday: {quantity_sold}")

#c. Update

#Change the price of a snack.
def update_snack_price(snack_id, new_price):
    data = load_file() 
    for snack in data["snacks"]:
        if snack["snack_id"] == snack_id:
            snack["price"] = new_price  
            print(f"Updated {snack['name']} price to {new_price}")
    save_file(data)  

#Update a student's grade level.
def update_student_grade(student_id, new_grade):
    data = load_file()
    for student in data["students"]:
        if student["student_id"] == student_id:
            student["grade_level"] = new_grade
            print(f"Updated {student['name']} to Grade {new_grade}")
    save_file(data)

#Correct a sale that recorded the wrong quantity.
def update_sale_quantity(sale_id, new_quantity):
    data = load_file()
    for sale in data["sales"]:
        if sale["sale_id"] == sale_id:
            # Look up the price of the snack to update the total_price correctly
            for snack in data["snacks"]:
                if snack["snack_id"] == sale["snack_id"]:
                    sale["quantity"] = new_quantity
                    sale["total_price"] = new_quantity * snack["price"]
                    print(f"Sale {sale_id} new total is: {sale['total_price']}")
    save_file(data)

#d. Delete

#Remove a discontinued snack.
def delete_snack(snack_id):
    data = load_file()
    data["snacks"] = [s for s in data["snacks"] if s["snack_id"] != snack_id]
    save_file(data)
    print(f"Snack {snack_id} has been removed.")

#Delete a student who transferred schools.
def delete_student(student_id):
    data = load_file()
    data["students"] = [s for s in data["students"] if s["student_id"] != student_id]
    save_file(data)
    print(f"Student {student_id} has been removed.")

#Remove a sale that was enetered by mistake.
def delete_sale(sale_id):
    data = load_file()
    data["sales"] = [sale for sale in data["sales"] if sale["sale_id"] != sale_id]
    save_file(data)
    print(f"Sale {sale_id} has been removed.")

#Questions

#What is the most popular snack overall?
def most_popular_snack():
    data = load_file()
    snack_counts = {}
    
    for sale in data["sales"]:
        sales = sale["snack_id"]
        snack_counts[sales] = snack_counts.get(sales, 0) + sale["quantity"]
    
    popular_id = max(snack_counts, key=snack_counts.get)
    print(f"Most Popular Snack ID: {popular_id} ({snack_counts[popular_id]} units sold)")

#Which grade level spends the most money on snacks?
def most_grade_level():
    data = load_file()
    student_to_grade = {s["student_id"]: s["grade_level"] for s in data["students"]}
    grade_totals = {}

    for sale in data["sales"]:
        grade = student_to_grade.get(sale["student_id"])
        grade_totals[grade] = grade_totals.get(grade, 0) + sale["total_price"]

    most_grade = max(grade_totals, key=grade_totals.get)
    print(f"Grade {most_grade} spent the most: P{grade_totals[most_grade]}")

#What day of the week has the highest number of sales?
def highest_sales_day():
    data = load_file()
    day_counts = {}
    for sale in data["sales"]:
        day = sale["day"]
        day_counts[day] = day_counts.get(day, 0) + 1
    
    highest = max(day_counts, key=day_counts.get)
    print(f"Highest number of sales happened on: {highest}")

#Which students has made the most purchases?
def most_purchases_student():
    data = load_file()
    student_purchases = {}
    for sale in data["sales"]:
        sid = sale["student_id"]
        student_purchases[sid] = student_purchases.get(sid, 0) + 1
    
    most_student_id = max(student_purchases, key=student_purchases.get)
    print(f"Student ID {most_student_id} made the most purchases.")

#What is the average amount spent per sale?
def average_spent():
    data = load_file()
    total_revenue = sum(sale["total_price"] for sale in data["sales"])
    total_sales = len(data["sales"])
    average = total_revenue / total_sales
    print(f"Average amount spent per sale: P{average}")

#What trends do you notice? How could the snack shop use this information to improve sales?
#These show how data becomes useful information when we use it to spot trends. Such as identifying Saturday as the busiest day or finding the most popular snacks. The shop can use these to improve sales by scheduling more staff during busy times and keeping high-demand items in stock. By understanding what students like, the shop can also improve student life. For example, stocking more favorite items. 

print("Read:")
find_chips()
student_sales()
total_snacks_sold()

print("Update:")
update_snack_price(1, 25)
update_student_grade(1, 11)
update_sale_quantity(1, 3)

print("Questions:")
most_popular_snack()
most_grade_level()
highest_sales_day()
most_purchases_student()
average_spent()
