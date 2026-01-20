import random

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # letters to pick from
numbers = "0123456789"                  # numbers to pick from

def make_random_part():
    # make 3 random letters + 3 random numbers
    part = random.choice(letters) + random.choice(letters) + random.choice(letters)
    part = part + random.choice(numbers) + random.choice(numbers) + random.choice(numbers)
    return part

department = input("Department name: ")  # user enters department
how_many = int(input("How many EC2 names do you need? "))  # user enters amount

names = []  # list to store EC2 names

if how_many < 0:
    print("Please enter a positive number (not negative).")
elif how_many == 0:
    print("You entered 0, so there are no names to generate.")
else:
    for i in range(how_many):  # loop to create the requested number of names
        ec2_name = department + "-EC2-" + str(i + 1) + "-" + make_random_part()  # build name
        names.append(ec2_name)  # add name to list

    print("\nEC2 Names:")
    for i in range(how_many):  # loop to print each name
        print(names[i])
