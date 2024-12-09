print(1+1)
tax = 0.1
amount = float(input("消費税の計算をします。金額を入力してください："))
tax_amount = amount*tax
total_amount = tax_amount+amount
print("消費税は",tax_amount,"円で、合計金額は",total_amount,"円です。")