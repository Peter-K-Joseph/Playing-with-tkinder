from tkinter import *
    
def input_box():
    
    def submit():
        if (inputArea.get() != ""):
            Label(inputBox, text="You Entered \"" + inputArea.get() + "\"").grid(row=2, column=0, columnspan=2)
            Menu

    
    inputBox = Tk()
    inputBox.title("Input Box")
    
    inputFrame = Frame(inputBox, bd=20) # Creates a frame that seperated the input area and then calls using a grid
    explanation = Frame(inputBox, bd=10) # Explanation using code
    
    Label(inputFrame, text="Enter Something: ").grid(row=0, column=0) #Print text to window
    inputArea = Entry(inputFrame, width=100) #Text area. Create a input area with width 100
    
    #Grid System for Input area and text
    inputArea.grid(row=0, column=1)
    inputFrame.grid(row=0,column=0)
    explanation.grid(row=3, column=0, columnspan=2)
    Button(inputBox, text="Submit", command=submit, width=10).grid(row=1, column=0)
    
    Label(explanation, text="""
    Label(inputBox, text=inputArea.get()).grid(row=1, column=0, columnspan=2)
    inputBox = Tk()
    inputBox.title("Input Box")
    inputFrame = Frame(inputBox, bd=20)
    Label(inputFrame, text="Enter Something").grid(row=0, column=0)
    inputArea = Entry(inputFrame, width=100)
    inputArea.grid(row=0, column=1)
    inputFrame.grid(row=0,column=0)
    Button(inputBox, text="Submit", command=submit, width=10).grid(row=1, column=0)""", font= ('Helvetica 13'),background="DeepSkyBlue1", anchor="w").pack()
    
    
def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()
   
if __name__ == '__main__':
    root = Tk() # Root to display
    menubar = Menu(root) # A menu bar
    display_menubar = Menu(menubar, tearoff=0)
    display_menubar.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=display_menubar)
    
    root.title("Tkinter Codes") # Just a title
    root.configure(bg="#1b1b1b") # The backgroudn color set
    root.state('zoomed') # Just do stuff in full screen
    inputBox_window = Button(root, text="Input Box using tkinter", command=input_box, width=20, height=5) # Just a Button
    inputBox_window.grid(row=0,column=0) # Pach the button in specified grid location
    
    root.config(menu=menubar)
    root.mainloop() # Loop this till program exits
