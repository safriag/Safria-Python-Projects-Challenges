#This program connects lines to create a star with my name displayed in the middle to mimic the Hollywood Star.
import tkinter #Import tkinter wrapper class
class MyGUI():
    def __init__(self):
        #Create main window.
        self.main_window = tkinter.Tk()
        #Create Canvas widget.
        self.canvas = tkinter.Canvas(self.main_window, width = 300, height = 250)
        #Draw line to connect multiple points and create the star.
        self.canvas.create_line(134.5,1,110,99,5.5,99,93,150,50,239,135.5,180.22,219,239,177.5,150,264,99,160.5,99,134.5,1) 
        #Display text in the center of the star.
        self.canvas.create_text(134.5,134.5, text='Safria George')
        #Pack the canvas.
        self.canvas.pack() 
        #Start mainloop for GUI until user closes it.
        tkinter.mainloop()
#Create an instance of the MyGUI class.
if __name__ == "__main__":
    my_gui = MyGUI()