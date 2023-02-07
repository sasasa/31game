import PySimpleGUI as sg
import random
import os
import sys

class Game31():
    def get_resource(self, filename):
        if hasattr(sys, "_MEIPASS"):
            return os.path.join(sys._MEIPASS, filename)
        return filename

    def getnextnums(self, n):
        self.nextnums = list(range(n+1, min(32, n+4)))
        self.choicemsg = f"{self.nextnums} から入力してください。"
        self.win["txt2"].update(self.choicemsg)
        self.win["in1"].update("")
        return self.nextnums

    def question(self):
        self.getnextnums(0)
        self.win["txt1"].update("さあ、ゲームを始めるよ！")
        self.win["img1"].update(self.get_resource("res/futaba0.png"))
        self.playflag = True
        self.win["btn"].update(" 入力 ")

    def com_turn(self, comnum):
        player_num = comnum
        keynums = [2,6,10,14,18,22,26,30]
        self.getnextnums(comnum)
        for n in self.nextnums:
            if n in keynums:
                comnum = n
        if comnum == player_num:
            # 必勝法の数字が選べないとき
            comnum = random.choice(self.nextnums)
        if random.randint(0,4) == 0:
            # 1/5の確率で必勝法を忘れる
            comnum = random.choice(self.nextnums)
        self.win["txt1"].update(f"ワタシは、[ {comnum} ] にするよ。")
        self.getnextnums(comnum)

    def my_turn(self):
        if self.v["in1"] == "" or self.v["in1"].isdecimal() == False:
            self.win["txt1"].update("数字を入力してね。")
            self.win["in1"].update("")
        else:
            mynum = int(self.v["in1"])
            if mynum in self.nextnums:
                if mynum == 31:
                    self.win["txt1"].update("31って言ったね。\nあなたの負けだよ。")
                    self.win["img1"].update(self.get_resource("res/futaba2.png"))
                    self.win["txt2"].update("ボタンを押すと、また遊べるよ。")
                    self.win["btn"].update(" また対戦する ")
                    self.playflag = False
                elif mynum == 30:
                    self.win["txt1"].update("31。あなたの勝ちだよ。\nおめでとう！")
                    self.win["img1"].update(self.get_resource("res/futaba1.png"))
                    self.win["txt2"].update("ボタンを押すと、また遊べるよ。")
                    self.win["btn"].update(" また対戦する ")
                    self.playflag = False
                else:
                    self.com_turn(mynum)
            else:
                # 3つの中にない数字を入力した場合
                self.win["in1"].update("")
                self.win["txt1"].update(self.choicemsg)

    def __init__(self):
        self.nextnums = []
        self.choicemsg = ""
        self.playflag = False

        sg.theme("DarkBrown3")
        layout = [[sg.T("31ゲームをしよう！ 31を言うと負けだよ。")],
                [sg.Im(k="img1"), sg.T(k="txt1")],
                [sg.T("数を入力してください。", k="txt2")],
                [sg.I("",k="in1",size=(15)),
                sg.B(" 入力 ", k="btn", bind_return_key=True)]]
        self.win = sg.Window("31ゲーム", layout, font=(None,14), finalize=True)
        self.question()
        while True:
            e, self.v = self.win.read()
            if e == "btn":
                if self.playflag == False:
                    self.question()
                else:
                    self.my_turn()
            if e == None:
                break
        self.win.close()

Game31()




