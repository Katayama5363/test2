import random


number = [1,2,3,4,5,6,7,8,9]

random.shuffle(number)

picked_number = number.pop()

if picked_number == 7:
    print("ラッキー7です！")
else:
    print(picked_number)


print(number.pop())
print(number.pop())
print(number.pop())
print(number.pop())
print(number.pop())
