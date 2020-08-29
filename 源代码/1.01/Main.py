import tkinter, tkinter.filedialog, tkinter.messagebox
from functools import partial
str2 = "C:\\Program Files (x86)\\Thunder Network\\Thunder\\Program"
# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("禁用迅雷自动更新")
# 设置大小和位置
win.geometry("400x400+200+50")
# height表示的是显示的行数
text = tkinter.Text(win, width=50, height=2)
text.pack()
str1 = '迅雷主程序根目录：C:\\Program Files (x86)\\Thunder Network\\Thunder\\Program'
text.insert(tkinter.INSERT, str1)
def func():
    thunderdir = tkinter.filedialog.askdirectory()
    if thunderdir:
        global str2
        str2 = thunderdir.replace("/", "\\")
    str3 = "迅雷主程序根目录：" + str2
    text.delete(1.0,tkinter.END)
    text.insert(tkinter.INSERT, str3)
def run():
    thunderdir = str2
    f02=thunderdir + "\\LiveUDInstaller.exe"
    f01=thunderdir + "\\XLLiveUD.exe"
    text = tkinter.Text(win, width=50, height=2)
    scroll = tkinter.Scrollbar()
    scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    text.pack(side=tkinter.LEFT, fill=tkinter.Y)
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)
    text.pack()
    str1 = '写入空内容至更新程序……'
    text.insert(tkinter.INSERT, str1)
    f1 = open(f01, "w")
    f1.write("")
    f1.close()
    f2 = open(f02, "w")
    f2.write("")
    f2.close()
    str4 = '完成！'
    text.insert(tkinter.INSERT, str4)
    tkinter.messagebox.showinfo("完成！", "已成功禁用迅雷自动更新。")
    exit()
button1 = tkinter.Button(win, text="选择", command=func, width=10, height=1)
button1.pack()
button = tkinter.Button(win, text="开始", command=run, width=10, height=1)
button.pack()
win.mainloop()



