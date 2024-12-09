amount_str = input("購入金額を入力してください：")
if amount_str.isdigit():
    amount = int(amount_str)
    if amount < 5000:
        print(f"金額は{amount}円、割引はありません。")
    elif amount < 20000:
        discount = amount*0.1
        af_discount = amount-discount
        print(f"元値は{amount}円、10%割引適応、{discount}円の割引、支払金額は{af_discount}円です")
    elif amount < 50000:
        discount = amount*0.2
        af_discount = amount-discount
        print(f"元値は{amount}円、20%割引適応、{discount}円の割引、支払金額は{af_discount}円です")
    else:
        discount = amount*0.3
        af_discount = amount-discount
        print(f"元値は{amount}円、30%割引適応、{discount}円の割引、支払金額は{af_discount}円です")      
else:
    print("入力された値が不正です。整数値で入力してください。")
