from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root = Tk()
root.title("Time in py")
root.geometry("600x500")

clock_image = ImageTk.PhotoImage(Image.open("clock.jpg"))


class India():
    def times(self):
        home = pytz.timezone("Asia/Kolkata")
        local_time = datetime.now(home)
        formatedTime = local_time.strftime("%H:%M:%S")
        india_time['text'] = "Time : " + formatedTime
        india_time.after(200, self.times)
        
class Usa():
    def times(self):
        home = pytz.timezone("US/Central")
        local_time = datetime.now(home)
        formatedTime = local_time.strftime("%H:%M:%S")
        usa_time['text'] = "Time : " + formatedTime
        usa_time.after(200, self.times)

# INDIA UI #

India_Label = Label(root, text="India")
India_Label.place(relx=0.2, rely=0.05, anchor=CENTER)

india_img = Label(root)
india_img["image"] = clock_image
india_img.place(relx=0.2, rely=0.35, anchor=CENTER)

india_time = Label(root)
india_time.place(relx=0.2, rely=0.65, anchor=CENTER)

instance_of_india= India()
india_btn = Button(root, text="Show Time", command=instance_of_india.times)
india_btn.place(relx=0.2, rely=0.8)
# USA UI #

Usa_label = Label(root, text="USA")
Usa_label.place(relx=0.7, rely=0.05, anchor=CENTER)

usa_img = Label(root)
usa_img["image"] = clock_image
usa_img.place(relx=0.7, rely=0.35, anchor=CENTER)

usa_time = Label(root)
usa_time.place(relx=0.7, rely=0.65, anchor=CENTER)

instance_of_usa = Usa()
usa_btn = Button(root, text="Show Time", command=instance_of_usa.times)
usa_btn.place(relx=0.7, rely=0.8)

root.mainloop()