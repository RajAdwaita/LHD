from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Rock Paper Scissor")
root.configure(background='#00bfff')

rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))
# # rock_img = ImageTk.PhotoImage(Image.open("rock_user.png"))

user_label = Label(root, image=rock_img, bg="#00bfff")
comp_label = Label(root, image=rock_img_comp, bg="#00bfff")

comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

playerScore = Label(root, text=0, font=100, bg="#00bfff", fg="white")
computerScore = Label(root, text=0, font=100, bg="#00bfff", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

user_indicator = Label(root, font=50, text="USER",
                       bg="#00bfff").grid(row=0, column=1)
comp_indicator = Label(root, font=50, text="BOT",
                       bg="#00bfff").grid(row=0, column=3)


msg = Label(root, text="", font=50, bg="#00bfff", fg="white")
msg.grid(row=1, column=2)


def updateChoices(x):
    if x == 'rock':
        user_label.config(image=rock_img)
    elif x == 'paper':
        user_label.config(image=paper_img)
    elif x == 'scissors':
        user_label.config(image=scissor_img)


rock = Button(root, width=20, height=2, text="Rock",
              bg="white", fg="black").grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="Paper",
               bg="white", fg="black").grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="Scissor",
                 bg="white", fg="black").grid(row=2, column=3)


root.mainloop()
