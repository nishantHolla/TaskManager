import customtkinter
from customtkinter import * 
from PIL import Image, ImageTk
from CTkListbox import *
from tkcalendar import * 


def add_to_do():
    contents = f"{entry_to_do.get()} : {entry_date.get()} : {entry_time.get()} {chr(10)} {entry_description.get()}"
    listbox.insert(END, contents)
    entry_to_do.delete(0, END)
    entry_description.delete(0, END)
    entry_time.delete(0, END)
    entry_date.delete(0, END)



app = CTk()
app.geometry("1000x800")
app.resizable(0,0)

side_img_data = Image.open("max-saeling-_CGxNOLM1gQ-unsplash.jpg")

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
                  text="Tasks", 
                  text_color="#601E88", 
                  anchor="w", 
                  justify="left", 
                  font=("Arial Bold", 24))

label1.pack(anchor="w", pady=(50, 5), padx=(25, 0))

label1.place(relx=0.44, rely=0.05)

# Button to Add a Task

button1 = CTkButton(master=frame, 
                    text="Add a Task", 
                    fg_color="#601E88", 
                    hover_color="#E44982", 
                    font=("Arial Bold", 12), 
                    text_color="#ffffff", 
                    width=240, 
                    command=add_to_do)

button1.pack(anchor="w", pady=(40, 0), padx=(25, 0))

button1.place(relx=0.07, rely=0.17)

# Button to Delete a Task

button2 = CTkButton(master=frame, 
                    text="Delete a Task", 
                    fg_color="#601E88", 
                    hover_color="#E44982", 
                    font=("Arial Bold", 12), 
                    text_color="#ffffff", 
                    width=240,
                    )

button2.pack(anchor="w", pady=(40, 0), padx=(25, 0))

button2.place(relx=0.52, rely=0.17)

# Button to Mark the task as Complete

button3 = CTkButton(master=frame, 
                    text="Mark Task as Completed", 
                    fg_color="#601E88", 
                    hover_color="#E44982", 
                    font=("Arial Bold", 12), 
                    text_color="#ffffff", 
                    width=240,
                    )

button3.pack(anchor="w", pady=(40, 0), padx=(25, 0))

button3.place(relx=0.07, rely=0.22)

# Button to Unmark the Task

button4 = CTkButton(master=frame, 
                    text="Unmark the task", 
                    fg_color="#601E88", 
                    hover_color="#E44982", 
                    font=("Arial Bold", 12), 
                    text_color="#ffffff", 
                    width=240,
                    )

button4.pack(anchor="w", pady=(40, 0), padx=(25, 0))

button4.place(relx=0.52, rely=0.22)

entry_to_do = CTkEntry(master=frame, 
                 placeholder_text="Enter the task: ", 
                 fg_color="#FFFFFF", 
                 font=("Arial Bold", 12), 
                 text_color="#000000", 
                 width=270)

entry_to_do.pack(pady=(40,0), padx=(25,0))

entry_to_do.place(relx=0.07, rely=0.297)

entry_date = CTkEntry(master=frame, 
                 placeholder_text="Enter the date (DD/MM/YYYY): ", 
                 fg_color="#FFFFFF", 
                 font=("Arial Bold", 12), 
                 text_color="#000000", 
                 width=196)

entry_date.pack(pady=(40,0), padx=(25,0))

entry_date.place(relx=0.587, rely=0.297)

entry_description = CTkEntry(master=frame, 
                 placeholder_text="Enter the description: ", 
                 fg_color="#FFFFFF", 
                 font=("Arial Bold", 12), 
                 text_color="#000000", 
                 width=270)

entry_description.pack(pady=(40,0), padx=(25,0))

entry_description.place(relx=0.07, rely=0.357)

entry_time = CTkEntry(master=frame, 
                 placeholder_text="Enter the time (HH/MM): ", 
                 fg_color="#FFFFFF", 
                 font=("Arial Bold", 12), 
                 text_color="#000000", 
                 width=196)

entry_time.pack(pady=(40,0), padx=(25,0))

entry_time.place(relx=0.587, rely=0.357)

listbox = CTkListbox(master=frame, 
                     height=400, 
                     width=450,
                     text_color="#000000")

listbox.pack(fill="both", padx=10, pady=10)

listbox.place(relx=0.07, rely=0.43)


app.mainloop()