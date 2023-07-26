from tkinter import messagebox
import os
import shutil
import customtkinter
import json
import webbrowser
#var FONT
FONT = ("Comic Sans MS", 25)
FONT_BUTTON = ("Comic Sans MS", 20)

#cho trường hợp mà người mới mới tải file về mà chưa có file extension.json thì phần mềm sẽ tự tạo ra một file default mới như vậy: 
extensions_main = {
    ".txt": "Text File",
    ".doc": "Microsoft Word Document",
    ".docx": "Microsoft Word Document",
    ".xls": "Microsoft Excel Spreadsheet",
    ".xlsx": "Microsoft Excel Spreadsheet",
    ".ppt": "Microsoft PowerPoint Presentation",
    ".pptx": "Microsoft PowerPoint Presentation",
    ".pdf": "Adobe Portable Document Format",
    ".jpg": "JPEG Image",
    ".jpeg": "JPEG Image",
    ".png": "Portable Network Graphics Image",
    ".gif": "Graphics Interchange Format Image",
    ".bmp": "Bitmap Image",
    ".mp3": "MP3 Audio File",
    ".wav": "WAV Audio File",
    ".mp4": "MP4 Video File",
    ".avi": "Audio Video Interleave Video File",
    ".mkv": "Matroska Video File",
    ".zip": "Zip Archive",
    ".rar": "RAR Archive",
    ".7z": "7-Zip Archive",
    ".exe": "Executable File",
    ".apk": "Android Package File",
    ".iso": "Disk Image File",
    ".csv": "Comma-Separated Values File",
    ".xml": "Extensible Markup Language File",
    ".json": "JavaScript Object Notation File",
    ".html": "Hypertext Markup Language File",
    ".htm": "Hypertext Markup Language File",
    ".css": "Cascading Style Sheet File",
    ".js": "JavaScript File",
    ".py": "Python Script File",
    ".cpp": "C/C++ Source Code File",
    ".c": "C/C++ Source Code File",
    ".java": "Java Source Code File",
    ".php": "PHP Script File",
    ".asp": "Active Server Page File",
    ".aspx": "Active Server Page File"
}
if not os.path.exists("extension.json"):
    with open("extension.json", "w") as f:
        json.dump(extensions_main, f, indent=4)
        f.close()
if not os.path.exists("need_to_clean"):
    os.mkdir("need_to_clean")


#Trang report
def report():
    webbrowser.open("https://github.com/mahiru7229/python-cleaning-file/issues")

#Mở trang hướng dẫn sử dụng
def open_help_center():    
    webbrowser.open("https://github.com/mahiru7229/python-cleaning-file/wiki/Cách-để-dùng-phần-mềm")
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
        messagebox.showinfo(title="Hoàn thành", message="Đã dọn dẹp tất cả các file trong thư mục vào các thư mục riêng biệt !")
    else:
        os.mkdir("need_to_clean")
        messagebox.showerror(title="Lỗi", message='Folder với tên "need_to_clean" không tồn tại !\nPhần mềm sẽ tự tạo lại folder!')


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

move_button = customtkinter.CTkButton(windows, text = "Report lỗi phần mềm", font =FONT_BUTTON,command=report)
move_button.grid(row= 2, column = 1,padx = 10, pady = 10)


windows.title("File Cleaner 1.0 :D")
windows.resizable(width=False, height=False)
windows.mainloop()