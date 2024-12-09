# ランダム機能の読み込み
import random 

# 山札として♤の１～１３までのカードをリストとして用意
cards = ["♤1","♤2","♤3","♤4","♤5","♤6","♤7","♤8","♤9","♤10","♤J","♤Q","♤K"]
#　カードをシャッフル
random.shuffle(cards)

# 自分の手札を表すリストを用意
my_cards = []

# pop()を使用して山札の一番うしろのカードを削除し、drawn_card変数に代入
drawn_card = cards.pop() 
print(drawn_card)
# appned（）を使用して引いたカードを手札リストに追加
my_cards.append(drawn_card)
print(my_cards)

drawn_card = cards.pop() 
print(drawn_card)
my_cards.append(drawn_card)
print(my_cards)

drawn_card = cards.pop() 
print(drawn_card)
my_cards.append(drawn_card)
print(my_cards)