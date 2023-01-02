# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 17:42:19 2022

@author: Jayesh
"""

import tkinter as tk
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    #best = sp.get_best_server()
    down = str(round(sp.download()/(10**6),3))+'Mbps'
    up = str(round(sp.upload()/(10**6),3))+'Mbps'
    lab_down.config(text=down)
    lab_up.config(text=up)


sp = tk.Tk()
sp.title('Internet Speed Test')
sp.geometry('500x600')
sp.config(bg='Blue')

lab = tk.Label(sp, text='Internet Speed Test', font=('Time New Roman',30,'bold'), bg='Blue', fg="white")
lab.place(x=60, y=40, height=50, width=380)

lab = tk.Label(sp, text='Download Speed', font=('Time New Roman',30,'bold'))
lab.place(x=60, y=130, height= 50, width=380)

lab_down = tk.Label(sp, text='00', font=('Time New Roman',30,'bold'))
lab_down.place(x=60, y=200, height=50, width=380)

lab = tk.Label(sp, text='Upload Speed', font=('Time New Roman',30,'bold'))
lab.place(x=60, y=290, height=50, width=380)

lab_up = tk.Label(sp, text='00', font=('Time New Roman',30,'bold'))
lab_up.place(x=60, y=360, height=50, width=380)

button = tk.Button(sp, text= 'CHECK SPEED',font=('Time New Roman',30,'bold'), bg= 'Orange', command=speedcheck)
button.place(x=60, y=460, height=50, width=380)
                    
sp.mainloop()