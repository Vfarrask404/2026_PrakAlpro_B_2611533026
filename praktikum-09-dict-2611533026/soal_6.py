schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

# untk yg 6a. cari hari dengan matkul terbanyak
hari_sibuks = ""
max_courses = 0

for day, courses in schedule.items():
    if len(courses) > max_courses:
        max_courses = len(courses)
        hari_sibuks = day

print(f"Hari mata kuliah terbanyak: {hari_sibuks} ({max_courses} courses)")

# utk yg 6b. hitung jumlah hari kemunculannya
target_course = input()
count = 0

for courses in schedule.values():
    if target_course in courses:
        count += 1

print(f"{target_course}: {count} days")