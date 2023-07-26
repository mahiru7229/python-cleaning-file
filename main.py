from tkinter import messagebox
import os
import shutil
import customtkinter
import json
import webbrowser
#var FONT
FONT = ("Comic Sans MS", 25)
FONT_BUTTON = ("Comic Sans MS", 20)



#Mở trang hướng dẫn sử dụng
def open_help_center():
    webbrowser.open("google.com")

#Phần code để dọn dẹp file
def cleaning():
    if os.path.exists("need_to_clean"):
        extensions = json.loads(open("extension.json", "r").read())
        directory = os.path.join("need_to_clean")
        for i in os.listdir(os.path.join("need_to_clean")):
            for j in extensions:
                if i.endswith(j):
                    check_folder_exist(os.path.join("need_to_clean"), extensions[j])
                    last_dir = directory + "\\" + i
                    move_dir = directory + "\\" + extensions[j]
                    move_file(last_dir,move_dir)
    else:
        messagebox.showerror(title="Lỗi", message='Chưa tạo folder với tên "need_to_clean" bên cạnh phần mềm !')

#Hàm của phần mềm
def create_folder(dir):
    os.mkdir(dir)
def check_folder_exist(dir, name):
    directory = dir + '\\' + name
    if not os.path.exists(directory):
        create_folder(directory)
def move_file(dir1, dir2):
    shutil.move(dir1, dir2)



#User Interface
customtkinter.set_appearance_mode("dark")


windows = customtkinter.CTk()

label_1 = customtkinter.CTkLabel(windows, text= "Mệt mỏi vì nhát dọn dẹp file ?, \nphần mềm này sẽ giúp những người lười như bạn XD", font=FONT)
label_1.grid(row= 0, column = 0)

label_2 = customtkinter.CTkLabel(windows, text= "Made by @mahiru7229", font=FONT)
label_2.grid(row= 1, column = 0)

help_button = customtkinter.CTkButton(windows, text = "Hướng dẫn cách dùng\nphần mềm", font =FONT_BUTTON, command=open_help_center)
help_button.grid(row= 0, column = 1,padx = 10, pady = 10)

move_button = customtkinter.CTkButton(windows, text = "Dọn dẹp file", font =FONT_BUTTON,command=cleaning)
move_button.grid(row= 1, column = 1,padx = 10, pady = 10)

windows.resizable(width=False, height=False)
windows.mainloop()