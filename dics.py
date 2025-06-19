# Creating a dictionary
student = {
    "name": "Monu",
    "age": 21,
    "course": "B.Tech",
    "marks": 85
}

# Printing the entire dictionary
print("Student Details:", student)

# Accessing a value
print("Name:", student["name"])

# Adding a new key-value pair
student["college"] = "RGPV"
print("After Adding College:", student)

# Updating a value
student["marks"] = 90
print("After Updating Marks:", student)

# Removing a key-value pair
del student["age"]
print("After Deleting Age:", student)

# Looping through dictionary keys and values
print("\nLooping through dictionary:")
for key, value in student.items():
    print(key, ":", value)
