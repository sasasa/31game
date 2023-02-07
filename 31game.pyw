import PySimpleGUI as sg
import random
import os
import sys
sg.theme("DarkBrown3")

layout = [[sg.T("31ゲームをしよう！ 31を言うと負けだよ。")],
          [sg.Im(k="img1"), sg.T(k="txt1")],
          [sg.T("数を入力してください。", k="txt2")],
          [sg.I("",k="in1",size=(15)),
           sg.B(" 入力 ", k="btn", bind_return_key=True)]]
win = sg.Window("31ゲーム", layout, font=(None,14), finalize=True)

def get_resource(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    return filename

def getnextnums(n):
    global nextnums, choicemsg
    nextnums = list(range(n+1, min(32, n+4)))
    choicemsg = f"{nextnums} から入力してください。"
    win["txt2"].update(choicemsg)
    win["in1"].update("")

def question():
    global playflag
    getnextnums(0)
    win["txt1"].update("さあ、ゲームを始めるよ！")
    win["img1"].update(get_resource("res/futaba0.png"))
    playflag = True
    win["btn"].update(f" 入力 ")

def com_turn(comnum):
    player_num = comnum
    keynums = [2,6,10,14,18,22,26,30]
    getnextnums(comnum)
    for n in nextnums:
        if n in keynums:
            comnum = n
    if comnum == player_num:
        # 必勝法に当てはまらない場合
        comnum = random.choice(nextnums)
    if random.randint(0,5) == 0:
        # 1/6の確率で、必勝法を忘れる
        comnum = random.choice(nextnums)
    win["txt1"].update(f"ワタシは、[ {comnum} ] にするよ。")
    getnextnums(comnum)

def my_turn():
    global playflag
    if v["in1"].isdecimal() == False:
        win["txt1"].update("数字を入力してね。")
        win["in1"].update("")
    else:
        mynum = int(v["in1"])
        if mynum in nextnums:
            if mynum == 31:
                win["txt1"].update("31って言ったね。\nあなたの負けだよ。")
                win["img1"].update(get_resource("res/futaba2.png"))
                win["txt2"].update("ボタンを押すと、また遊べるよ。")
                win["btn"].update(f" また遊ぶ ")
                playflag = False
            elif mynum == 30:
                win["txt1"].update("31。あなたの勝ちだよ。\nおめでとう！")
                win["img1"].update(get_resource("res/futaba1.png"))
                win["txt2"].update("ボタンを押すと、また遊べるよ。")
                win["btn"].update(f" また遊ぶ ")
                playflag = False
            else:
                com_turn(mynum)
        else:
            # 入力された数が、範囲外の場合
            win["txt1"].update(choicemsg)
            win["in1"].update("")

question()
while True:
    e, v = win.read()
    if e == "btn":
        if playflag == False:
            question()
        else:
            my_turn()
    if e == None:
        break
win.close()
