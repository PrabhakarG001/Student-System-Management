from database import load_data, save_data

students = load_data()

def get_student(i):
    return next((s for s in students if s["id"] == i), None)

def add_student(i, n, m):
    if get_student(i): return False, "ID already exists!"
    students.append({"id": i, "name": n, "marks": m})
    save_data(students)
    return True, "Added successfully!"

def delete_student(i):
    s = get_student(i)
    if not s: return False, "ID not found!"
    students.remove(s)
    save_data(students)
    return True, "Deleted successfully!"
