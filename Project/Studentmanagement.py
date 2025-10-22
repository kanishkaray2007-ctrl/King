import sqlite3

# ---------------- DATABASE SETUP ----------------
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT,
    marks REAL
)
""")
conn.commit()



def add_student():
    try:
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        dept = input("Enter Department: ")
        marks = float(input("Enter Marks: "))

        cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", 
                       (roll, name, age, dept, marks))
        conn.commit()
        print("Student added successfully!\n")
    except Exception as e:
        print("Error:", e, "\n")


def view_students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    if data:
        print("\nStudent Records:")
        print("-" * 60)
        print("Roll | Name        | Age | Dept    | Marks")
        print("-" * 60)
        for row in data:
            print(f"{row[0]:<4} | {row[1]:<10} | {row[2]:<3} | {row[3]:<7} | {row[4]:<5}")
        print()
    else:
        print("No records found.\n")


def search_student():
    roll = int(input("Enter Roll Number to search: "))
    cursor.execute("SELECT * FROM students WHERE roll=?", (roll,))
    row = cursor.fetchone()
    if row:
        print(f"\nFound: Roll={row[0]}, Name={row[1]}, Age={row[2]}, Dept={row[3]}, Marks={row[4]}\n")
    else:
        print("⚠ Student not found.\n")


def update_student():
    roll = int(input("Enter Roll Number to update: "))
    cursor.execute("SELECT * FROM students WHERE roll=?", (roll,))
    row = cursor.fetchone()
    if row:
        print("Leave blank if no change.")
        name = input(f"Enter New Name ({row[1]}): ") or row[1]
        age = input(f"Enter New Age ({row[2]}): ") or row[2]
        dept = input(f"Enter New Department ({row[3]}): ") or row[3]
        marks = input(f"Enter New Marks ({row[4]}): ") or row[4]

        cursor.execute("""
        UPDATE students 
        SET name=?, age=?, department=?, marks=? 
        WHERE roll=?""", (name, int(age), dept, float(marks), roll))
        conn.commit()
        print("Student updated successfully!\n")
    else:
        print("Student not found.\n")


def delete_student():
    roll = int(input("Enter Roll Number to delete: "))
    cursor.execute("SELECT * FROM students WHERE roll=?", (roll,))
    row = cursor.fetchone()
    if row:
        cursor.execute("DELETE FROM students WHERE roll=?", (roll,))
        conn.commit()
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")


# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("\n=====Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")
if __name__ == "__main__":
    main()
    conn.close()
