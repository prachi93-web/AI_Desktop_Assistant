from tkinter import*
from PIL import Image , ImageTk
import speech_to_text
import action
root =Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False,False)
root.config(bg="#6F8FAF")

def ask ():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END , "User---> "+user_val+"\n")
    if bot_val != None :
        text.insert(END , "BOT <--- "+str(bot_val)+"\n")
    if bot_val == "Ok Prachi" :
        root.destroy()

def send ():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END , "User---> "+send+"\n")
    if bot != None :
        text.insert(END , "BOT <--- "+str(bot)+"\n")
    if bot == "Ok Prachi" :
        root.destroy()

def del_text ():
    text.delete('1.0' , "end")

#Frame
frame = LabelFrame(root , padx=100 ,  pady=7 , borderwidth=3 ,  relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row = 0 ,  column= 1 ,  padx= 55 ,  pady =  10)

#text
text_label = Label(frame, text = "Hey I am Nexa" , font=("comic Sans ms" ,  14 , "bold" ) , bg = "#356696")
text_label.grid(row=0 ,  column=0 , padx=20 , pady= 10)

#image
image = ImageTk.PhotoImage(Image.open("image/assist.png"))
image_Label = Label(frame, image= image)
image_Label.grid(row = 1 ,  column=0 , pady=20)

#text widget

text=Text(root , font= ('courier 10 bold') , bg = "#356696")
text.grid(row = 2,  column= 0)
text.place(x= 100, y= 375, width= 375, height= 100) 

#entry widget
entry = Entry(root, justify = CENTER)
entry.place(x=100 , y = 500 , width= 350, height= 30)

#button1
button1 =  Button(root,  text="ASK" , bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=ask)
button1.place(x= 70, y= 575)

#button2
button2 =  Button(root,  text="SEND" , bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=send)
button2.place(x= 400, y= 575)

#button3
button3 = Button(root, text="DELETE", bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,command=del_text)
button3.place(x= 225, y= 575)
root.mainloop()