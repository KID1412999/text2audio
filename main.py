import urllib
from urllib.parse import quote
from tkinter import *
import requests
import tkinter.messagebox
from tkinter.filedialog import askdirectory
def com():#英文
    s=e1.get()
    s=s.replace(' ','%20')
    url='https://fanyi.baidu.com/gettts?lan=en&text='+s+'&spd='+e2.get()+'&source=web'
    urllib.request.urlretrieve(url, filename='C://英文audio.mp3', reporthook=None, data=None)
    print('Done!')
    tkinter.messagebox.showinfo('合成信息','完成！文件在C盘')
    print(path,s)
def com_zh():#中文
    s=e1.get()
    s=quote(s)
    url='https://fanyi.baidu.com/gettts?lan=zh&text='+s+'&spd='+e2.get()+'&source=web'
    urllib.request.urlretrieve(url, filename='C://中文audio.mp3', reporthook=None, data=None)
    print('Done!')
    tkinter.messagebox.showinfo('合成信息','完成！文件在C盘')
    print(path,s)
def selectPath():
    global path_
    path_ = askdirectory()
    path.set(path_)
    
master=Tk()
master.title('语音合成 @')
path = StringVar()
Label(master, text="请输入（粘贴）文本：").grid(row=0)
Label(master, text="请输入语速（默认值为2）：").grid(row=1)
e1 = Entry(master)
e1.grid(row=0, column=1)
e2 = Entry(master)
e2.grid(row=1, column=1)
#Button(master, text = "路径选择", command = selectPath).grid(row =3, column=0)
Button(master, text='开始合成英文', command=com).grid(row=4, column=1, sticky=W, pady=4)
Button(master, text='开始合成中文', command=com_zh).grid(row=5, column=1, sticky=W, pady=4)
master.mainloop()
