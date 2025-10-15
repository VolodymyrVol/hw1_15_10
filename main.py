first_tuple = (2, 2, 3, 4, 5, 2, 6)
second_tuple = (4, 2, 6, 5, 7, 8, 1, 2)
third_tuple = (7, 2, 9, 12, 8, 31, 4)

task1 = []
task2 = []
task3 = []

for number in first_tuple:
    if number in second_tuple and number in third_tuple and number not in task1:
        task1.append(number)

print("Task 1:", task1)

for number in first_tuple:
    if number not in second_tuple and number not in third_tuple and number not in task2:
        task2.append(number)

for number in second_tuple:
    if number not in first_tuple and number not in third_tuple and number not in task2:
        task2.append(number)

for number in third_tuple:
    if number not in second_tuple and number not in first_tuple and number not in task2:
        task2.append(number)

print("Task 2:", task2)

for i in range(len(first_tuple)):
    if first_tuple[i] == second_tuple[i] == third_tuple[i] and number not in task3:
        task3.append(first_tuple[i])

print("Task 3:", task3)