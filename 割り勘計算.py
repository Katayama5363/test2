count = 0
saki_total_amount = 0
saki_people = int(input("個別の支払いをする人数は何人いますか(いなければ0にしてください)："))
while count < saki_people:
    count += 1
    saki_amount = int(input(f"{count}人目の金額を入力してください"))
    saki_total_amount += saki_amount
n_people = int(input("個別支払いをした人を除いた割り勘の人数は何人ですか："))
total_amount = int(input("合計金額は何円ですか"))
dutch_treat = (total_amount-saki_total_amount)/n_people
print("先に支払いをした人の合計金額は",saki_total_amount,"円です")
print("一人当たりの割り勘金額は",dutch_treat,"円です")
