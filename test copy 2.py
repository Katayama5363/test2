wait = float(input("あなたの体重を入力してください："))
height = float(input("あなたの身長をセンチで入力してください："))
bmi = wait / ((height/100)**2)
print("あなたのBMIは", bmi , "です。")