import os

FILENAME = "persons.txt"

def load_data():
    records = {}
    if not os.path.exists(FILENAME):
        return records
    with open(FILENAME, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) != 5:
                continue
            pid, name, age, phone, height = parts
            records[pid] = {
                "name": name,
                "age": int(age),
                "phone": phone,
                "height": float(height)
            }
    return records

def save_data(records):
    with open(FILENAME, "w") as f:
        for pid, info in records.items():
            f.write(f"{pid},{info['name']},{info['age']},{info['phone']},{info['height']}\n")

def add_person(records):
    pid = input("Enter person ID: ").strip()
    if pid in records:
        print("Error: That person ID already exists.")
        return
    name = input("Enter name: ").strip()
    age = input("Enter age: ").strip()
    phone = input("Enter phone number: ").strip()
    height = input("Enter height (e.g. in cm): ").strip()
    try:
        info = {
            "name": name,
            "age": int(age),
            "phone": phone,
            "height": float(height)
        }
    except ValueError:
        print("Invalid numeric input!")
        return
    records[pid] = info
    save_data(records)
    print("Person added successfully.")

def display_all(records):
    if not records:
        print("No records found.")
        return
    print("All Persons:")
    for pid, info in records.items():
        print(f"ID: {pid}, Name: {info['name']}, Age: {info['age']}, Phone: {info['phone']}, Height: {info['height']}")

def search_person(records):
    pid = input("Enter the person ID to search: ").strip()
    info = records.get(pid)
    if info:
        print(f"Found: ID: {pid}, Name: {info['name']}, Age: {info['age']}, Phone: {info['phone']}, Height: {info['height']}")
    else:
        print("No person with that ID.")

def main():
    records = load_data()
    while True:
        print("\nMenu:")
        print("1. Add Person")
        print("2. Display All")
        print("3. Search by ID")
        print("4. Exit")
        choice = input("Enter choice (1‑4): ").strip()
        if choice == "1":
            add_person(records)
        elif choice == "2":
            display_all(records)
        elif choice == "3":
            search_person(records)
        elif choice == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
