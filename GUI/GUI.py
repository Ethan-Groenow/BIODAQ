#importing libraries
from tkinter import *
from matplotlib import pyplot as plt
###########################################################
#function definitions
def plotfunc(event):
    #print(event)
    x=[25,26,27,28,29,30]
    y=[100,101,102,103,104,105]
    plt.plot(x,y)
    plt.title("EMG Signal")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude(Volts)")
    plt.show()

##############################################################
    
#GUI
##############################################################
root=Tk()
root.title("BIODAQ GUI")
Screen_width=root.winfo_screenwidth() #Retrieve the width of the computer screen
Screen_height=root.winfo_screenheight() #Retrieve the height of the computer screen
root.geometry("%dx%d+0+0" % (Screen_width,Screen_height)) #Making the window full screen
###############################################################################
#Creating Status Bar
status=Label(root, text=" ",bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM,fill=X)
########################################################################
#Creating ToolBar
ToolBar=Frame(root,bg="white")
Tbutton1=Button(ToolBar,text="Plot")
Tbutton1.bind("<Button-1>",plotfunc)
Tbutton1.pack(side=LEFT,padx=2,pady=2)
Tbutton2=Button(ToolBar,text="About",command=print(1))
Tbutton2.pack(side=LEFT,padx=2,pady=2)
ToolBar.pack(side=TOP,fill=X)
#######################################################################
#Creating Menus
menu=Menu(root)
root.config(menu=menu)
subMenu=Menu(menu,tearoff=False)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_separator()
subMenu.add_command(label="Save",command=print(1))
subMenu.add_separator()
subMenu.add_command(label="Save as",command=print(2))
subMenu.add_separator()
modeMenu=Menu(menu,tearoff=False)
menu.add_cascade(label="Mode",menu=modeMenu)
modeMenu.add_command(label="EMG")
modeMenu.add_separator()
modeMenu.add_command(label="EOG")
modeMenu.add_separator()
#####################################################################
MainFrame=Frame(root)
MainFrame.pack()
button1=Button(MainFrame,text="Button1",fg="red")
button1.bind("<Button-1>",plotfunc)
button2=Button(MainFrame,text="Button2",fg="blue")
button3=Button(MainFrame,text="Button3",fg="green")
button1.pack()
button2.pack()
button3.pack()
CheckBox=Checkbutton(root,text="HAND CONTRACTIONS")
CheckBox.pack()
#Label=Label(root,text="GUI",bg="red",fg="white")
#Label.pack()
root.mainloop()
