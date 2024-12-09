import random

# 1から100までの乱数生成
random_number = random.randint(1,100)
print("数字当てゲーム！100回の間に1～100のランダムな数字を当ててください！")

# 数字の入力

count_game = 1
while count_game <= 100:
    try:
        predict = int(input(f"現在{count_game}回目の挑戦です！数字は何でしょうか："))
        if predict == random_number:
            print(f"正解です！数字は{random_number}でした！挑戦回数は{count_game}回でした！")
            break
        elif predict < random_number:
            print(f"{predict}より大きい数字です！")
            count_game += 1
        else:
            print(f"{predict}より小さい数字です！")
            count_game += 1
    except ValueError:
        print("無効な入力です。整数を入力してください。")
if count_game == 101:
    print("挑戦回数上限に到達しました。")