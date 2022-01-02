from tkinter import *

FONT_NAME = 'calibri'
def generate_font(font_size=15):
  return (FONT_NAME, font_size)

def click():
  hello.configure(text='You clicked the button!')

mw = Tk()
mw.title("Hello World!")
mw.geometry("500x500")

hello = Label(mw, text="Hello world!", font=generate_font(17))
hello.pack()
button = Button(mw, text="Click me!", command=click)
button.pack()

mw.mainloop()