full_name = input("Enter your full name (First Name, Middle Name, Last Name): ")
parts = [p.strip() for p in full_name.split(",")]
first_name = parts[0].capitalize()
middle_name = parts[1].capitalize()
last_name = parts[2].capitalize()
middle_initial = middle_name[0] + "."
formatted_name = f"{last_name}, {first_name} {middle_initial}"
print("Formatted Name:", formatted_name)
