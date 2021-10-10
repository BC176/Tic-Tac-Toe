 #Brian Clark
#TTT week 2 Final
#11/18/18

from tkinter import *
from tkinter import font
import random

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.used = []
        self.count = 1
        self.turn = "X"
        self.create_widgets()

    def create_widgets(self):
        self.lbl_title = Label(self,
                               text = "Tic Tac Toe",
                               height = 3,
                               fg="blue",
                               bg="cyan",
                               font=font.Font(family="Comic sans ms", size=26, weight="bold"),
                               anchor = "center"
                               )
        self.lbl_title.grid(row=0, columnspan=5)

        self.lbl_status = Label(self,
                                text = "X goes First!",
                                height = 1,
                                bg="white",
                                fg="green",
                                font=font.Font(family="Times New Roman ms", size=14, weight="bold"),
                                anchor = "center"
                                )
        self.lbl_status.grid(row=1, columnspan=5)

        #buttons
        style=font.Font(family="Consolas", size=38, weight="bold")
        self.btn1 = Button(self,
                           command=self.btn1_clicked,
                           width=3,
                           height=1,
                           bg = "white",
                           relief="solid",
                           activebackground="green",
                           disabledforeground="black",
                           font=style
                           )                          
        self.btn1.grid(row=2,column=0, sticky=NSEW)

        self.btn2 = Button(self,
                           command=self.btn2_clicked,
                           width=3,
                           height=1,
                           bg = "white",
                           relief="solid",
                           activebackground="yellow",
                           disabledforeground="black",
                           font=style
                           )
        self.btn2.grid(row=2,column=1,sticky=NSEW)

        self.btn3 = Button(self,
                           command=self.btn3_clicked,
                           width=3,
                           height=1,
                           bg = "white",
                           relief="solid",
                           activebackground="purple",
                           disabledforeground="black",
                           font=style
                           )
        self.btn3.grid(row=2,column=2,sticky=NSEW)

        self.btn4 = Button(self,
                           command=self.btn4_clicked,
                           width=3,
                           height=1,
                           bg = "white",
                           relief="solid",
                           activebackground="black",
                           disabledforeground="black",
                           font=style
                           )
        self.btn4.grid(row=3,column=0,sticky=NSEW)

        self.btn5 = Button(self,
                           command=self.btn5_clicked,
                           width=3,
                           height=1,
                           bg = "white",
                           relief="solid",
                           activebackground="orange",
                           disabledforeground="black",
                           font=style
                           )
        self.btn5.grid(row=3,column=1,sticky=NSEW)

        self.btn6 = Button(self,
                           command=self.btn6_clicked,
                           width=3,
                           height=1,
                           bg = "white",
                           relief="solid",
                           activebackground="pink",
                           disabledforeground="black",
                           font=style
                           )
        self.btn6.grid(row=3,column=2,sticky=NSEW)

        self.btn7 = Button(self,
                           command=self.btn7_clicked,
                           width=3,
                           height=1,
                           bg = "white",
                           relief="solid",
                           activebackground="blue",
                           disabledforeground="black",
                           font=style
                           )
        self.btn7.grid(row=4,column=0,sticky=NSEW)

        self.btn8 = Button(self,
                           command=self.btn8_clicked,
                           width=3,
                           height=1,
                           bg = "white",
                           relief="solid",
                           activebackground="magenta",
                           disabledforeground="black",
                           font=style
                           )
        self.btn8.grid(row=4,column=1,sticky=NSEW)

        self.btn9 = Button(self,
                           command=self.btn9_clicked,
                           width=3,
                           height=1,
                           bg = "white",
                           relief="solid",
                           activebackground="cyan",
                           disabledforeground="black",
                           font=style
                           )
        self.btn9.grid(row=4,column=2,sticky=NSEW)

        self.reset = Button(self,
                            command=self.reset_clicked,
                            height=1,
                            text = "Reset",
                            fg="yellow",
                            bg="magenta",
                            font=font.Font(family="Times New Roman ms", size=18, weight="bold")
                            )
        self.reset.grid(row=5,column=0,sticky=NSEW,columnspan=3)

        self.autoPlay = Button(self,
                                command=self.autoPlay_clicked,
                                height=1,
                                text="Auto Play",
                                fg="magenta",
                                bg="yellow",
                                font=font.Font(family="Times New Roman ms", size=18, weight="bold")
                                )
        self.autoPlay.grid(row=6,column=0,sticky=NSEW,columnspan=3)

    used = []
    def check_win(self):  
        if self.btn1["text"]=="X" and self.btn2["text"]=="X" and self.btn3["text"]=="X":
            self.lbl_status["text"] = "X Wins!"
        elif self.btn4["text"]=="X" and self.btn5["text"]=="X" and self.btn6["text"]=="X":
            self.lbl_status["text"] = "X Wins!"
        elif self.btn7["text"]=="X" and self.btn8["text"]=="X" and self.btn9["text"]=="X":
            self.lbl_status["text"] = "X Wins!"
        elif self.btn1["text"]=="X" and self.btn4["text"]=="X" and self.btn7["text"]=="X":
            self.lbl_status["text"] = "X Wins!"
        elif self.btn2["text"]=="X" and self.btn5["text"]=="X" and self.btn8["text"]=="X":
            self.lbl_status["text"] = "X Wins!"
        elif self.btn3["text"]=="X" and self.btn6["text"]=="X" and self.btn9["text"]=="X":
            self.lbl_status["text"] = "X Wins!"
        elif self.btn1["text"]=="X" and self.btn5["text"]=="X" and self.btn9["text"]=="X":
            self.lbl_status["text"] = "X Wins!"
        elif self.btn3["text"]=="X" and self.btn5["text"]=="X" and self.btn7["text"]=="X":
            self.lbl_status["text"] = "X Wins!"
        elif self.btn1["text"]=="O" and self.btn2["text"]=="O" and self.btn3["text"]=="O":
            self.lbl_status["text"] = "O Wins!"
        elif self.btn4["text"]=="O" and self.btn5["text"]=="O" and self.btn6["text"]=="O":
            self.lbl_status["text"] = "O Wins!"
        elif self.btn7["text"]=="O" and self.btn8["text"]=="O" and self.btn9["text"]=="O":
            self.lbl_status["text"] = "O Wins!"
        elif self.btn1["text"]=="O" and self.btn4["text"]=="O" and self.btn7["text"]=="O":
            self.lbl_status["text"] = "O Wins!"
        elif self.btn2["text"]=="O" and self.btn5["text"]=="O" and self.btn8["text"]=="O":
            self.lbl_status["text"] = "O Wins!"
        elif self.btn3["text"]=="O" and self.btn6["text"]=="O" and self.btn9["text"]=="O":
            self.lbl_status["text"] = "O Wins!"
        elif self.btn1["text"]=="O" and self.btn5["text"]=="O" and self.btn9["text"]=="O":
            self.lbl_status["text"] = "O Wins!"
        elif self.btn3["text"]=="O" and self.btn5["text"]=="O" and self.btn9["text"]=="O":
            self.lbl_status["text"] = "O Wins!"
       

    #button definitions
    def autoPlay_clicked(self):
        buttons = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6,
                   self.btn7, self.btn8, self.btn9]
        if self.btn1["text"] == self.btn2["text"] and self.btn1["text"]!=self.turn and self.btn1["state"]=="disabled" and self.btn3 not in self.used:
            pick = self.btn3
        elif self.btn2["text"] == self.btn3["text"] and self.btn2["text"]!=self.turn and self.btn2["state"]=="disabled" and self.btn1 not in self.used:
            pick = self.btn1
        elif self.btn4["text"] == self.btn5["text"] and self.btn4["text"]!=self.turn and self.btn4["state"]=="disabled" and self.btn6 not in self.used:
            pick = self.btn6
        elif self.btn5["text"] == self.btn6["text"] and self.btn5["text"]!=self.turn and self.btn5["state"]=="disabled" and self.btn4 not in self.used:
            pick = self.btn4
        elif self.btn7["text"] == self.btn8["text"] and self.btn7["text"]!=self.turn and self.btn7["state"]=="disabled" and self.btn9 not in self.used:
            pick = self.btn9
        elif self.btn8["text"] == self.btn9["text"] and self.btn8["text"]!=self.turn and self.btn8["state"]=="disabled" and self.btn7 not in self.used:
            pick = self.btn7
        elif self.btn4["text"] == self.btn6["text"] and self.btn4["text"]!=self.turn and self.btn4["state"]=="disabled" and self.btn5 not in self.used:
            pick = self.btn5
        elif self.btn1["text"] == self.btn3["text"] and self.btn1["text"]!=self.turn and self.btn1["state"]=="disabled" and self.btn2 not in self.used:
            pick = self.btn2
        elif self.btn7["text"] == self.btn9["text"] and self.btn7["text"]!=self.turn and self.btn7["state"]=="disabled" and self.btn8 not in self.used:
            pick = self.btn8
        elif self.btn1["text"] == self.btn5["text"] and self.btn1["text"]!=self.turn and self.btn1["state"]=="disabled" and self.btn9 not in self.used:
            pick = self.btn9
        elif self.btn1["text"] == self.btn9["text"] and self.btn1["text"]!=self.turn and self.btn1["state"]=="disabled" and self.btn5 not in self.used:
            pick = self.btn5
        elif self.btn5["text"] == self.btn9["text"] and self.btn5["text"]!=self.turn and self.btn5["state"]=="disabled" and self.btn1 not in self.used:
            pick = self.btn1
        elif self.btn1["text"] == self.btn4["text"] and self.btn1["text"]!=self.turn and self.btn1["state"]=="disabled" and self.btn7 not in self.used:
            pick = self.btn7
        elif self.btn4["text"] == self.btn7["text"] and self.btn4["text"]!=self.turn and self.btn4["state"]=="disabled" and self.btn1 not in self.used:
            pick = self.btn1
        elif self.btn2["text"] == self.btn5["text"] and self.btn2["text"]!=self.turn and self.btn2["state"]=="disabled" and self.btn8 not in self.used:
            pick = self.btn8
        elif self.btn5["text"] == self.btn8["text"] and self.btn5["text"]!=self.turn and self.btn5["state"]=="disabled" and self.btn2 not in self.used:
            pick = self.btn2
        elif self.btn3["text"] == self.btn6["text"] and self.btn3["text"]!=self.turn and self.btn3["state"]=="disabled" and self.btn9 not in self.used:
            pick = self.btn9
        elif self.btn6["text"] == self.btn9["text"] and self.btn6["text"]!=self.turn and self.btn6["state"]=="disabled" and self.btn3 not in self.used:
            pick = self.btn3
        elif self.btn1["text"] == self.btn7["text"] and self.btn1["text"]!=self.turn and self.btn1["state"]=="disabled" and self.btn4 not in self.used:
            pick = self.btn4
        elif self.btn2["text"] == self.btn8["text"] and self.btn2["text"]!=self.turn and self.btn2["state"]=="disabled" and self.btn5 not in self.used:
            pick = self.btn5
        elif self.btn3["text"] == self.btn5["text"] and self.btn3["text"]!=self.turn and self.btn3["state"]=="disabled" and self.btn7 not in self.used:
            pick = self.btn7
        elif self.btn3["text"] == self.btn9["text"] and self.btn3["text"]!=self.turn and self.btn3["state"]=="disabled" and self.btn6 not in self.used:
            pick = self.btn6
        elif self.btn5["text"] == self.btn7["text"] and self.btn5["text"]!=self.turn and self.btn5["state"]=="disabled" and self.btn3 not in self.used:
            pick = self.btn3
        elif self.btn3["text"] == self.btn7["text"] and self.btn3["text"]!=self.turn and self.btn3["state"]=="disabled" and self.btn5 not in self.used:
            pick = self.btn5
        else:
            pick = random.choice(buttons)        
            while pick in self.used:
                pick = random.choice(buttons)
        self.used.append(pick)
        pick["text"] = self.turn
        if pick["text"]=="X":
            pick["bg"]="turquoise1"
        else:
            pick["bg"]="yellow"
        self.switch_turns()
        self.check_win()
        self.count_clicks()
        
    def reset_clicked(self):
        self.btn1["state"] = "normal"
        self.btn2["state"] = "normal"
        self.btn3["state"] = "normal"
        self.btn4["state"] = "normal"
        self.btn5["state"] = "normal"
        self.btn6["state"] = "normal"
        self.btn7["state"] = "normal"
        self.btn8["state"] = "normal"
        self.btn9["state"] = "normal"
        self.btn1["text"] = " "
        self.btn2["text"] = " "
        self.btn3["text"] = " "
        self.btn4["text"] = " "
        self.btn5["text"] = " "
        self.btn6["text"] = " "
        self.btn7["text"] = " "
        self.btn8["text"] = " "
        self.btn9["text"] = " "
        self.btn1["bg"]="white"
        self.btn2["bg"]="white"
        self.btn3["bg"]="white"
        self.btn4["bg"]="white"
        self.btn5["bg"]="white"
        self.btn6["bg"]="white"
        self.btn7["bg"]="white"
        self.btn8["bg"]="white"
        self.btn9["bg"]="white"
        self.lbl_status["text"] = "X goes First!"
        self.count = 1
        self.turn = "X"
        self.used = []

    def btn1_clicked(self):
        self.btn1["state"] = "disabled"
        self.btn1["text"] = self.turn
        if self.btn1["text"]=="X":
            self.btn1["bg"]="turquoise1"
        else:
            self.btn1["bg"]="yellow"
        self.used.append(self.btn1)
        self.switch_turns()
        self.check_win()
        self.count_clicks()

    def btn2_clicked(self):
        self.btn2["state"] = "disabled"
        self.btn2["text"] = self.turn
        if self.btn2["text"]=="X":
            self.btn2["bg"]="turquoise1"
        else:
            self.btn2["bg"]="yellow"
        self.used.append(self.btn2)
        self.switch_turns()
        self.check_win()
        self.count_clicks()

    def btn3_clicked(self):
        self.btn3["state"] = "disabled"
        self.btn3["text"] = self.turn
        if self.btn3["text"]=="X":
            self.btn3["bg"]="turquoise1"
        else:
            self.btn3["bg"]="yellow"
        self.used.append(self.btn3)
        self.switch_turns()
        self.check_win()
        self.count_clicks()

    def btn4_clicked(self):
        self.btn4["state"] = "disabled"
        self.btn4["text"] = self.turn
        if self.btn4["text"]=="X":
            self.btn4["bg"]="turquoise1"
        else:
            self.btn4["bg"]="yellow"
        self.used.append(self.btn4)
        self.switch_turns()
        self.check_win()
        self.count_clicks()

    def btn5_clicked(self):
        self.btn5["state"] = "disabled"
        self.btn5["text"] = self.turn
        if self.btn5["text"]=="X":
            self.btn5["bg"]="turquoise1"
        else:
            self.btn5["bg"]="yellow"
        self.used.append(self.btn5)
        self.switch_turns()
        self.check_win()
        self.count_clicks()

    def btn6_clicked(self):
        self.btn6["state"] = "disabled"
        self.btn6["text"] = self.turn
        if self.btn6["text"]=="X":
            self.btn6["bg"]="turquoise1"
        else:
            self.btn6["bg"]="yellow"
        self.used.append(self.btn6)
        self.switch_turns()
        self.check_win()
        self.count_clicks()
  
    def btn7_clicked(self):
        self.btn7["state"] = "disabled"
        self.btn7["text"] = self.turn
        if self.btn7["text"]=="X":
            self.btn7["bg"]="turquoise1"
        else:
            self.btn7["bg"]="yellow"
        self.used.append(self.btn7)
        self.switch_turns()
        self.check_win()
        self.count_clicks()

    def btn8_clicked(self):
        self.btn8["state"] = "disabled"
        self.btn8["text"] = self.turn
        if self.btn8["text"]=="X":
            self.btn8["bg"]="turquoise1"
        else:
            self.btn8["bg"]="yellow"
        self.used.append(self.btn8)
        self.switch_turns()
        self.check_win()
        self.count_clicks()

    def btn9_clicked(self):
        self.btn9["state"] = "disabled"
        self.btn9["text"] = self.turn
        if self.btn9["text"]=="X":
            self.btn9["bg"]="turquoise1"
        else:
            self.btn9["bg"]="yellow"
        self.used.append(self.btn9)
        self.switch_turns()
        self.check_win()
        self.count_clicks()

        

    #switch turns
    def switch_turns(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
        self.lbl_status["text"] = "It is " + self.turn + "'s turn"

    #count clicks
    def count_clicks(self):
        self.count+=1
        if self.count > 9:
            self.lbl_status["text"] = "Cat's Game!"
            self.count = 1


#main
root = Tk()
root.title("It's a game!")
app = Application(root)
root.mainloop()
