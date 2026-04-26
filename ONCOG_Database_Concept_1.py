import json 
from pathlib import Path

script_path = Path(__file__)
script_dir = script_path.parent
json_file = script_dir / 'database.json'

def load_file(filename = json_file):
    with open(filename, 'r') as file:
        return json.load(file)

def save_file(data, filename = json_file):
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4) 


def create_student(name, age, subject, color, song): 
    data = load_file()
    students = data.get("students", []) 
    
    new_student = {
        "name": name,
        "age": age,
        "favorite_subject": subject,
        "favorite_color": color,
        "favorite_song": song
    }
    
    students.append(new_student) 
    data["students"] = students 
    save_file(data) 

def read_all_students():
    data = load_file()
    students = data.get("students", [])
    print("\n------------------------------")
    for s in students: 
        print(f"Name: {s['name']} | Age: {s['age']} | Color: {s['favorite_color']}")
        print(f"Subject: {s['favorite_subject']} | Song: {s['favorite_song']}")
        if "school" in s:
            print(f"Campus: {s['school']}")
        print("-" * 30)

def update_with_campus(): 
    data = load_file()
    for student in data["students"]:
        student["school"] = "PSHS-CVisC" 
    save_file(data)
    print("\nUpdated all students with school field information.")

def delete_by_colors(): 
    data = load_file()
    original_count = len(data["students"])
    target_colors = ["red", "blue", "yellow"]
    

    data["students"] = [s for s in data["students"] 
                        if s["favorite_color"].lower() not in target_colors] 
    
    save_file(data)
    deleted = original_count - len(data["students"])
    print(f"\nDeleted {deleted} students with Red, Blue, or Yellow as favorite colors.")

def main():
    friends = [
        ("Zaphyra", 13, "CS", "Pink", "Kagome"),
        ("Xianne", 13, "Math", "Purple", "Midnight Sun"),
        ("Glen Matthew L. Montante", 14, "Lunch", "Orange", "Wish You Were Gay/L'amour de Ma Vie"),
        ("Miggy", 13, "Health", "Red", "Carol of the NEW! Ones"),
        ("Kirby James F. Basalo", 14, "Physics", "Green", "Tokyo Teddybear"),
        ("Joy", 13, "Math", "Red", "Running Up That Hill")
    ]
    
    save_file({"students": []})
    
    for f in friends:
        create_student(f[0], f[1], f[2], f[3], f[4])
    
    read_all_students()
    
    update_with_campus()
    
    delete_by_colors()
    
    read_all_students()


main()