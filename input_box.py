from tkinter import *

def input_box():
    def submit():
        Label(inputBox, text=inputArea.get()).grid(row=1, column=0, columnspan=2)
    inputBox = Tk()
    inputBox.title("Input Box")
    
    inputFrame = Frame(inputBox, bd=20) #Creates a frame that seperated the input area and then calls using a grid
    explanation = Frame(inputBox, bd=10) #Explanation using code
    
    Label(inputFrame, text="Enter Something").grid(row=0, column=0) #Print text to window
    inputArea = Entry(inputFrame, width=100) #Text area. Create a input area with width 100
    
    #Grid System for Input area and text
    inputArea.grid(row=0, column=1) #
    inputFrame.grid(row=0,column=0)
    explanation.grid(row=3, column=0, columnspan=2)
    Button(inputBox, text="Submit", command=submit, width=10).grid(row=1, column=0)
    
    Label(explanation, anchor="w", text="""def submit():\n\t
        Label(inputBox, text=inputArea.get()).grid(row=1, column=0, columnspan=2)
    inputBox = Tk()\n
    inputBox.title("Input Box")\n
    inputFrame = Frame(inputBox, bd=20)\n
    Label(inputFrame, text="Enter Something").grid(row=0, column=0)\n
    inputArea = Entry(inputFrame, width=100)\n
    inputArea.grid(row=0, column=1)\n
    inputFrame.grid(row=0,column=0)\n
    Button(inputBox, text="Submit", command=submit, width=10).grid(row=1, column=0)""").grid(row=3, column=0, columnspan=2)
    inputBox.mainloop()
    