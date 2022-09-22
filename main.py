import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

index = len(names) - 1
random_number = random.randint(0,index)
random_name = names[random_number]

print(f"{random_name} is going to buy the meal today!")