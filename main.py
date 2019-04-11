from tkinter import *
import time

root = Tk()
root.title("Time")
width = 150
height = 100
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2)- (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.config(bg="light blue")

def tick():
    setTime = time.strftime('%I: %M %S %p')
    clock.config(text=setTime )
    clock.after(200, tick)

Top = Frame(root, width=600, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=600)
Mid.pack(side=TOP, expand=1)

lbl_title = Label(Top, text="Clock", width=600, font=("arial", 20))
lbl_title.pack(fill=X)

clock = Label(Mid, font=('Helvetica', 100), fg="green", bg="light blue")
clock.pack()

if __name__ == '__main__':
    tick()
    root.mainloop()
