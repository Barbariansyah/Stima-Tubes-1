import tkinter as tk
from PIL import Image,ImageTk
import random

emblem = ['C','D','H','S']
List_Num = []

def GetCard():
   Card_Num = random.randint(1,13)
   List_Num.append(Card_Num)

   file_name = (str(Card_Num) + random.choice(emblem) + '.png')

   return file_name

def PrintCard():
   pos = 500
   for i in range(4):
      file_name = GetCard()
      img = Image.open(file_name)
      img = img.resize((200, 250), Image.ANTIALIAS)
      img = ImageTk.PhotoImage(img)
      card = tk.Label(root, image=img, bg = 'green')
      card.x = img
      card.place(x = pos, y = 200)
      pos += 250

def Layout(Card):
   tk.Label(root, 
		   text='WELCOME TO',
		   fg = 'white',
         bg = 'green',
		   font = 'Helvetica 40 bold italic').pack()

   tk.Label(root, 
		      text='24 FAKE GAME SOLVER',
		      fg = 'white',
            bg = 'green',
		      font = 'Helvetica 40 bold italic').pack()

   tk.Button(root, image = Card, bg = 'green', command = PrintCard).place(x = 100,y = 200)

   tk.Label(root, 
      text = "SOLUTION : ",  
      font = ('Helvetica',30,'bold','italic'),
      bg = 'Green', 
      fg = 'White').place(x = 100, y = 500)


   tk.Label(root, 
            text = "SCORE : ",  
            font = ('Helvetica',30,'bold','italic'),
            bg = 'Green', 
            fg = 'White').place(x = 1200, y = 500)

   root.state('zoomed')
   root.configure(background='green')

if __name__ == '__main__':
   root = tk.Tk()
   Card = Image.open("Card.png")
   Card = Card.resize((200, 250), Image.ANTIALIAS)
   Card = ImageTk.PhotoImage(Card)
   Layout(Card)
   root.mainloop()
   
