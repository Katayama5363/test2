import random

omikuji_list = ["大吉","中吉","吉","小吉","末吉","凶","大凶"]
random.shuffle(omikuji_list)

result = omikuji_list.pop()
print(result)

