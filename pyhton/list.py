# question 1
fruit1 =str(input("Enter the fruits name:"))
fruit2 =str(input("Enter the fruits name:"))
fruit3 =str(input("Enter the fruits name:"))
fruit4 =str(input("Enter the fruits name:"))
fruit5 =str(input("Enter the fruits name:"))
fruit6 =str(input("Enter the fruits name:"))
fruit7 =str(input("Enter the fruits name:"))
fruits =["fruit1","fruit2","fruit3","fruit4","fruit5","fruit6","fruit7"]
print("fruits",fruits)
# question 2
# Create an empty list to collect marks
marks = []

# Loop to get marks from the user
for i in range(1, 7):
    while True:
        try:
            val = float(input(f"Enter marks for student {i}: "))
            if 0 <= val <= 100:
                marks.append(val)
                break
            else:
                print("Please enter a valid mark between 0 and 100.")
        except ValueError:
            print("That’s not a number—please try again.")

# Sort the marks (if you want ascending order; use reverse=True for descending)
sorted_marks = sorted(marks)

# Display results
print("\nOriginal marks:", marks)
print("Sorted marks:", sorted_marks)
