# Initialize variables
count = 0
average = 0
low_score = 10000
high_score = 0
total_score = 0

# Prompt for grade
grades = str(input("Enter score: "))

# If the length of grade is greater than 0
while len(grades) > 0:  # Change this to true or false later
    total_score = total_score + int(grades)
    grades = str(input("Enter score: "))
    count += 1
    average = total_score / count
    if len(grades) == 0:
        print("No score entered")
        break
    if int(grades) < int(low_score):
        low_score = grades
    if int(grades) > int(high_score):
        high_score = grades


print(count, low_score, high_score, total_score, average)
