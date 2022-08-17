from pytube import YouTube
from tkinter import *

root = Tk()
root.configure(bg = 'Orchid')
root.geometry('500x300+500+200')
root.resizable(0,0)
root.title('Youtube Downloader')

Label(root, text = 'My Youtube Downloader', font = 'arial 15 bold',bg = 'Orchid').pack()

link = StringVar()
Label(root, text = 'Paste the video link: ', font = 'arial 15 bold',bg = 'Orchid').place(x=160,y=60)
link_enter = Entry(root,width = 70, textvariable = link).place(x = 32, y = 90)

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'Success!', font = 'arial 15').place(x=210,y=210)
    Label(root, text = f'Name video: {video.title} ', font = 'arial 15').place(x=20,y=260)


Button(root, text = "Download", font = 'areal 15 bold', bg = 'turquoise2', padx = 2, command = Downloader).place(x = 195, y = 150)

root.mainloop()

