import customtkinter
from customtkinter import *
from PIL import Image
from CTkListbox import * 


def delete_item():
    #listbox.delete(ANCHOR)
    collection_index = listbox.curselection()
    listbox.delete(collection_index)

def add_item():
    listbox.insert(END, entry.get())
    entry.delete(0, END)

def connect_to_do():
    pass

app = CTk()
app.geometry("1000x800")
app.resizable(0,0)

side_img_data = Image.open("photo-1570649236495-42fa5fe5c48b.jpeg")

side_image = CTkImage(dark_image=side_img_data, 
                      light_image=side_img_data, 
                      size=(450, 830))

CTkLabel(master=app, text="", image=side_image).pack(expand=True, side="left")

frame = CTkFrame(master=app, 
                 width= 550, 
                 height= 830, 
                 fg_color="#ffffff")

frame.pack_propagate(0)
frame.pack(expand=True, side="right")

# Label for the Heading 

label1 = CTkLabel(master=frame, 
                  text="Collections", 
                  text_color="#601E88", 
                  anchor="w", 
                  justify="left", 
                  font=("Arial Bold", 24))

label1.pack(anchor="w", pady=(50, 5), padx=(25, 0))

label1.place(relx=0.4, rely=0.05)

# Button to Add a Collection

button1 = CTkButton(master=frame, 
                    text="Add a Collection", 
                    fg_color="#601E88", 
                    hover_color="#E44982", 
                    font=("Arial Bold", 12), 
                    text_color="#ffffff", 
                    width=240, 
                    command=add_item)

button1.pack(anchor="w", pady=(40, 0), padx=(25, 0))

button1.place(relx=0.07, rely=0.2)

# Button to Delete a Collection

button2 = CTkButton(master=frame, 
                    text="Delete a Collection", 
                    fg_color="#601E88", 
                    hover_color="#E44982", 
                    font=("Arial Bold", 12), 
                    text_color="#ffffff", 
                    width=240,
                    command=delete_item)

button2.pack(anchor="w", pady=(40, 0), padx=(25, 0))

button2.place(relx=0.52, rely=0.2)

# Button to Open the Selected Collection

button3 = CTkButton(master=frame, 
                    text="Open the Selected Collection", 
                    fg_color="#601E88", 
                    hover_color="#E44982", 
                    font=("Arial Bold", 12), 
                    text_color="#ffffff", 
                    width=240)

button3.pack(anchor="w",pady=(40, 0), padx=(25, 0))

button3.place(relx=0.30, rely=0.26)

entry = CTkEntry(master=frame, 
                 placeholder_text="Enter the Name of the Collection", 
                 fg_color="#FFFFFF", 
                 font=("Arial Bold", 12), 
                 text_color="#000000", 
                 width=480)

entry.pack(pady=(40,0), padx=(25,0))

entry.place(relx=0.07, rely=0.342)

#global listbox
listbox = CTkListbox(master=frame, 
                     height=400, 
                     width=450,
                     text_color="#000000")

listbox.pack(fill="both", padx=10, pady=10)

listbox.place(relx=0.07, rely=0.42)

app.mainloop()