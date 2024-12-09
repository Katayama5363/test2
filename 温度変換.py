while True:
    select = input("変換元の温度は摂氏ですか？華氏ですか？どちらかで答えてください：")
    if select == "摂氏":
        celsius = float(input("温度(摂氏)を入力してください。華氏に変換します："))
        fahrenheit = celsius*1.8+32
        print("華氏",fahrenheit,"度です")
        break
    elif select == "華氏":
            fahrenheit = float(input("温度(華氏)を入力してください。摂氏に変換します："))
            celsius = (fahrenheit-32)*5/9
            print("摂氏",celsius,"度です")
            break
    else:
        print("『摂氏』か『華氏』の文字を入力してください")