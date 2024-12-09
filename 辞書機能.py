pc = {"CPU":"","GPU":""}
pc["CPU"] = input("CPUを教えてください：")
pc["GPU"] = input("GPUを教えてください：")

while True:
    print(f"現在のPC構成一覧は{pc}です")
    add_key = input("追加、削除したい項目は他にありますか。追加があれば種類を入力してください。削除する場合は[d]、無ければ[n]を入力してください：")
    if add_key == "n":
        break
    elif add_key == "d":
        del_key = input("削除したい項目の種類を入力してください：")
        del pc[del_key]
    else: 
        add_value = input("その型番、もしくはスペック等を記載ください：")
        pc[add_key] = add_value

print(f"pcの構成は{pc}です")