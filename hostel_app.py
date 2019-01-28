from tkinter import *
from tkinter import ttk

root = Tk()

mainFrame = ttk.Frame(root,relief="raised",padding=(4,4,4,4))
optionFrame = ttk.Labelframe(mainFrame,text="Options")
otherFrame = ttk.Frame(mainFrame)
extraFrame = ttk.Frame(optionFrame)
update = ttk.Button(optionFrame,text="Update")
view = ttk.Button(optionFrame,text="View")
search = ttk.Button(optionFrame,text="Search File")
lbl = ttk.Label(otherFrame, text="Just")
s = ttk.Separator(mainFrame,orient=HORIZONTAL)

mainFrame.grid(column=0,row=0,sticky=(N, S, E, W))
optionFrame.grid(column=0,row=0,sticky=(N, S, E, W))
otherFrame.grid(column=1,row=0,sticky=(N, S, E, W))
update.grid(column=0,row=1,sticky=(N, S, E, W))
view.grid(column=0,row=2,sticky=(N, S, E, W))
search.grid(column=0,row=3,sticky=(N, S, E, W))
extraFrame.grid(column=0,row=4,sticky=(N, S, E, W))
lbl.grid(column=2,row=1)
s.grid(column=1)

root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
mainFrame.rowconfigure(0,weight=2)
mainFrame.rowconfigure(1,weight=2)
mainFrame.rowconfigure(2,weight=2)
mainFrame.rowconfigure(3,weight=2)
mainFrame.rowconfigure(4,weight=5)
mainFrame.columnconfigure(0,weight=1)
mainFrame.columnconfigure(1,weight=5)
optionFrame.rowconfigure(0,weight=2)
optionFrame.rowconfigure(1,weight=2)
optionFrame.rowconfigure(2,weight=2)
optionFrame.rowconfigure(3,weight=2)
optionFrame.rowconfigure(4,weight=7)
optionFrame.columnconfigure(0,weight=1)
root.mainloop()