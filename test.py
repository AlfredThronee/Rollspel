import random

random.seed

list = [1, 5, 2, 4]

list.append((random.randint(1, 6)))

list.append((random.randint(1, 6)))

numbers_sum = sum(list)

print(numbers_sum)