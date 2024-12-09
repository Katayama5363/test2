import random
while True:
    npc = ["グー","チョキ","パー"]
    random.shuffle(npc)
    npc_hand = npc.pop()


    print("じゃんけんゲームです！プレイヤーは「グー」か「チョキ」か「パー」を入力してください！：")
    player = input("プレイヤーが出す手を選択してください！")
    if player == "グー":
        if npc_hand ==  "グー":
            print("相手の手はグー！あいこです！もう一回！")
        elif npc_hand == "パー":
            print("相手の手はパー！あなたの負けです…")
            retry = input("もう一度じゃんけんしますか[y/n]")
            if retry == "n":
                break
        else:
            print("相手の手はチョキ！あなたの勝ちです！")
            retry = input("もう一度じゃんけんしますか[y/n]")
            if retry == "n":
                break
    elif player == "チョキ":
        if npc_hand ==  "チョキ":
            print("相手の手はチョキ！あいこです！もう一回！")
        elif npc_hand == "グー":
            print("相手の手はグー！あなたの負けです…")
            retry = input("もう一度じゃんけんしますか[y/n]")
            if retry == "n":
                break
        else:
            print("相手の手はパー！あなたの勝ちです！")
            retry = input("もう一度じゃんけんしますか[y/n]")
            if retry == "n":
                break
    elif player == "パー":
        if npc_hand ==  "パー":
            print("相手の手はパー！あいこです！もう一回！")
        elif npc_hand == "チョキ":
            print("相手の手はチョキ！あなたの負けです…")
            retry = input("もう一度じゃんけんしますか[y/n]")
            if retry == "n":
                break
        else:
            print("相手の手はグー！あなたの勝ちです！")
            retry = input("もう一度じゃんけんしますか[y/n]")
            if retry == "n":
                break
    else:
        print("「グー」「チョキ」「パー」以外の文字が入力されました。やり直してください！")
    