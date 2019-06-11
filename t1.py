from tkinter import *
from tkinter import ttk
import time
root = Tk()


def doNothing():
    print("Ok Ok I won't")


def start_progress():
    progress_bar.start()

def pause_progress(event):
    b = []
    b.append('1')
    while event:
        if len(b)%2 == 0:
            time.sleep(100000000000000000000000)


# def rev_progress():


root.title("PRABHAV'S MUSIC PLAYER")
root.state('zoomed')

# # Adding image without PIL
# photo = PhotoImage(file='musicimage.png')
# label_image = Label(root,image=photo)
# label_image.place(x=200, y=300 )


# **** DROP DOWN START ****
MyMenu = Menu(root) # Menu bar
root.config(menu=MyMenu)

SubMenu = Menu(MyMenu)
MyMenu.add_cascade(label='Option', menu = SubMenu)

SubMenu.add_command(label='View', command=doNothing)

SubMenu.add_command(label='Add', command=doNothing)

SubMenu.add_command(label='Remove', command=doNothing)

Reverse_button = Button(root,text='<<',command=doNothing)
Reverse_button.place(x=350, y=400)

play_button = Button(root,text='|>',command=start_progress)
play_button.place(x=400, y=400)

pause_button = Button(root,text='||')
pause_button.bind("<Button-1>",pause_progress)
pause_button.place(x=450, y=400)

FastForward_button = Button(root,text='>>',command=doNothing)
FastForward_button.place(x=500, y=400)
# **** DROP DOWN CLOSED ****

# **** PROGRESS BAR STARTS ****
progress_bar = ttk.Progressbar(root,orient='horizontal',length='300',mode='determinate')
progress_bar.place(x=1000,y=500)


# **** PROGRESS BAR ENDS

root.mainloop()