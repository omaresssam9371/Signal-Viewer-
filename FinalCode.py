from tkinter import * 
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import time
import pandas as pd
import numpy as np
import math
import ntpath
import os 
from tkinter import ttk
import pdfkit
from matplotlib.backends.backend_pdf import PdfPages
import PIL 
from skimage.exposure import rescale_intensity
import PyPDF2 
from matplotlib.widgets import Slider

files =[]
filenum=0

def UploadAction1(event=None):
    global filenum
    global filename1
    filename1 = filedialog.askopenfilename()
    filenum = filenum+1  
    print('Selected:', filename1)
    files.append(os.path.basename(filename1))
    print(filenum)
    if (filenum==4):
        filenum=1
        
def UploadAction2(event=None):
    global filenum
    global filename2
    filename2 = filedialog.askopenfilename()
    filenum = filenum+1
    print('Selected:', filename2)
    files.append(os.path.basename(filename2))
    print(filenum)
    if (filenum==4):
        filenum=1
        
def UploadAction3(event=None):
    global filenum
    global filename3
    filename3 = filedialog.askopenfilename()
    filenum = filenum+1
    print('Selected:', filename3)
    files.append(os.path.basename(filename3))
    print(filenum)
    if (filenum==4):
        filenum=1

def red1():
    global colorpicker1
    colorpicker1='r'
def red2():
    global colorpicker2
    colorpicker2='r'
def red3():
    global colorpicker3
    colorpicker3='r'
def blue1():
    global colorpicker1
    colorpicker1='b' 
def blue2():
    global colorpicker2
    colorpicker2='b'
def blue3():
    global colorpicker3
    colorpicker3='b'
def green1():
    global colorpicker1
    colorpicker1='g'    
def green2():
    global colorpicker2
    colorpicker2='g'  
def green3():
    global colorpicker3
    colorpicker3='g'  

def speedUp():
    global speed
    if speed>0.05:
        speed = speed-0.05 
def speedDown():
    global speed
    speed = speed+0.05
    
def graphing1():
    ax.clear()
    global colorpicker1
    global speed
    global filenum
    speed =0.1
    colorpicker1='r'
    global flag
    flag = True
    
    name1 = filename1.split('.')
    file1 = name1[0].split('/')  
    i = 0
    x1, y1 = [], []
    data1 = pd.read_csv(filename1)
    ax.plot(x1, y1,color=colorpicker1,label =file1[-1])
    ax.legend()
    while flag:
            x1.append(data1['x'][i])
            y1.append(data1['y'][i])
            ax.plot(x1, y1,color=colorpicker1,label =file1[-1])
            ax.set_title(file1[-1])  
            
            fig.canvas.draw()
            #counter=0.1
            ax.set_xlim(left= data1['x'][i]-0.1, right=data1['x'][i]+0.16)
            time.sleep(speed)
            i += 1
            #counter=counter+0.1
            main_window.update()
            
def graphing2():
    ax.clear()
    global colorpicker1
    global colorpicker2
    colorpicker1='r'
    colorpicker2='b'
    global speed
    global filenum
    speed =0.1
    global flag
    flag = True
    
    name1 = filename1.split('.')
    file1 = name1[0].split('/')
    name2 = filename2.split('.')
    file2 = name2[0].split('/')  
    i = 0
    x1, y1 = [],[]
    x2, y2 = [], []
    data1 = pd.read_csv(filename1)
    data2 = pd.read_csv(filename2)
    ax.plot(x1, y1,color=colorpicker1,label =file1[-1])
    ax.plot(x2, y2,color=colorpicker2,label =file2[-1])
    ax.legend()
    while flag:
        x1.append(data1['x'][i])
        y1.append(data1['y'][i])
        x2.append(data2['x'][i])
        y2.append(data2['y'][i])
        ax.plot(x1, y1,color=colorpicker1)
        ax.plot(x2, y2,color=colorpicker2)
        ax.set_title(file2[-1]+' & '+file1[-1])
        fig.canvas.draw()
        ax.set_xlim(left=max(0, data1['x'][i]-1), right=data1['x'][i]+0.1)
        time.sleep(speed)
        i += 1
        main_window.update()
        
def graphing3():
    ax.clear()
    global colorpicker1
    global colorpicker2
    global colorpicker3
    colorpicker1='r'
    colorpicker2='b'
    colorpicker3='g'
    global speed
    global filenum
    speed =0.1
    global flag
    flag = True
    
    name1 = filename1.split('.')
    file1 = name1[0].split('/')
    name2 = filename2.split('.')
    file2 = name2[0].split('/') 
    name3 = filename3.split('.')
    file3 = name3[0].split('/')  
    i = 0
    x1, y1 = [],[]
    x2, y2 = [], []
    x3, y3 = [], []
    data1 = pd.read_csv(filename1)
    data2 = pd.read_csv(filename2)
    data3 = pd.read_csv(filename3)
    ax.plot(x1, y1,color=colorpicker1,label =file1[-1])
    ax.plot(x2, y2,color=colorpicker2,label =file2[-1])
    ax.plot(x2, y2,color=colorpicker3,label =file3[-1])
    ax.legend()
    while flag:
        x1.append(data1['x'][i])
        y1.append(data1['y'][i])
        x2.append(data2['x'][i])
        y2.append(data2['y'][i])
        x3.append(data3['x'][i])
        y3.append(data3['y'][i])
        ax.plot(x1, y1,color=colorpicker1)
        ax.plot(x2, y2,color=colorpicker2)
        ax.plot(x3, y3,color=colorpicker3)
        ax.set_title(file3[-1]+' & '+file2[-1]+' & '+file1[-1])
        fig.canvas.draw()
        ax.set_xlim(left=max(0, data3['x'][i]-0.2), right=data3['x'][i]+0.1)
        time.sleep(speed)
        i += 1
        main_window.update()
        
def specto():
    ax2.clear() 
    global SpectoColor
    SpectoColor= clicked.get()
    i = 0
    z = []
    
    data = pd.read_csv(mytkcombo.get())
    while i<len(data['y']):
        z.append(data['y'][i])
        length= len(z)
        i = i+1
    plt.specgram(z,Fs=1,cmap=SpectoColor, vmin=slider1.get(),vmax=slider2.get())
    plt.title('Spectrogram')  
    fig2.canvas.draw()
    #plt.savefig('Spectogram.png')
    
def stop():
    global flag
    flag = False
           
def toggleHide1():
    if toggle1.get():
        global colorpicker1
        colorpicker1='r'
    else:
        colorpicker1='w'             
def toggleHide2():
    if toggle2.get():
        global colorpicker2
        colorpicker2='b'
    else:
        colorpicker2='w' 
def toggleHide3():
    if toggle3.get():
        global colorpicker3
        colorpicker3='g'
    else:
        colorpicker3='w'      
def show():
    ax.set_visible(True)
    ax3.set_visible(True)
    ax4.set_visible(True)    
        
#<-------------------------HOW TO DELEEEEETEEEE---------------------    
def refreshFigure():
    #ax.clear()
    ax2.clear()  
    
def updateFilelist():
    mytkcombo['values'] = files
    
    
def SavePdf1():
    data = pd.read_csv(filename1)
    mean1 =data['y'].mean()
    max1 = data['y'].max()
    min1 = data['y'].min()
    std1 = data['y'].std()
    sum1 = data['x'].max()
    stats = [{"Mean":mean1, "Max":max1, "Min":min1,"Standard Deviation":std1, "Duration":sum1}]

    m =pd.DataFrame(stats,index =['Value'])
    m.head()
    figPDF, axpdf =plt.subplots(figsize=(12,4))
    axpdf.axis('off')
    the_table = axpdf.table(cellText=m.values,colLabels=m.columns,loc='center')
    pp = PdfPages("stats1.pdf")
    pp.savefig(figPDF, bbox_inches='tight')
    fig.savefig("CurrentSignal1.pdf", bbox_inches='tight')
    fig2.savefig("CurrentSpecto1.pdf", bbox_inches='tight')
    pp.close()
    
    #import PyPDF2 
    mergeFile = PyPDF2.PdfFileMerger()
    mergeFile.append(PyPDF2.PdfFileReader('stats1.pdf', 'rb'))
    mergeFile.append(PyPDF2.PdfFileReader('CurrentSignal1.pdf', 'rb'))
    mergeFile.append(PyPDF2.PdfFileReader('CurrentSpecto1.pdf', 'rb'))
    mergeFile.write("Graph1_Data.pdf")
    os.remove("stats1.pdf")
    os.remove("CurrentSignal1.pdf")
    os.remove("CurrentSpecto1.pdf")
def SavePdf2():
    data = pd.read_csv(filename2)
    mean1 =data['y'].mean()
    max1 = data['y'].max()
    min1 = data['y'].min()
    std1 = data['y'].std()
    sum1 = data['x'].max()
    stats = [{"Mean":mean1, "Max":max1, "Min":min1,"Standard Deviation":std1, "Duration":sum1}]

    m =pd.DataFrame(stats,index =['Value'])
    m.head()
    figPDF, axpdf =plt.subplots(figsize=(12,4))
    axpdf.axis('off')
    the_table = axpdf.table(cellText=m.values,colLabels=m.columns,loc='center')
    pp = PdfPages("stats2.pdf")
    pp.savefig(figPDF, bbox_inches='tight')
    fig.savefig("CurrentSignal2.pdf", bbox_inches='tight')
    fig2.savefig("CurrentSpecto2.pdf", bbox_inches='tight')
    pp.close()
    
    #import PyPDF2 
    mergeFile = PyPDF2.PdfFileMerger()
    mergeFile.append(PyPDF2.PdfFileReader('stats2.pdf', 'rb'))
    mergeFile.append(PyPDF2.PdfFileReader('CurrentSignal2.pdf', 'rb'))
    mergeFile.append(PyPDF2.PdfFileReader('CurrentSpecto2.pdf', 'rb'))
    mergeFile.write("Graph2_Data.pdf")
    os.remove("stats2.pdf")
    os.remove("CurrentSignal2.pdf")
    os.remove("CurrentSpecto2.pdf")  
def SavePdf3():
    data = pd.read_csv(filename3)
    mean1 =data['y'].mean()
    max1 = data['y'].max()
    min1 = data['y'].min()
    std1 = data['y'].std()
    sum1 = data['x'].max()
    stats = [{"Mean":mean1, "Max":max1, "Min":min1,"Standard Deviation":std1, "Duration":sum1}]

    m =pd.DataFrame(stats,index =['Value'])
    m.head()
    figPDF, axpdf =plt.subplots(figsize=(12,4))
    axpdf.axis('off')
    the_table = axpdf.table(cellText=m.values,colLabels=m.columns,loc='center')
    pp = PdfPages("stats3.pdf")
    pp.savefig(figPDF, bbox_inches='tight')
    fig.savefig("CurrentSignal3.pdf", bbox_inches='tight')
    fig2.savefig("CurrentSpecto3.pdf", bbox_inches='tight')
    pp.close()
    
    #import PyPDF2 
    mergeFile = PyPDF2.PdfFileMerger()
    mergeFile.append(PyPDF2.PdfFileReader('stats3.pdf', 'rb'))
    mergeFile.append(PyPDF2.PdfFileReader('CurrentSignal3.pdf', 'rb'))
    mergeFile.append(PyPDF2.PdfFileReader('CurrentSpecto3.pdf', 'rb'))
    mergeFile.write("Graph3_Data.pdf")
    os.remove("stats3.pdf")
    os.remove("CurrentSignal3.pdf")
    os.remove("CurrentSpecto3.pdf") 
    
def updatex(val):
    posx = s_time.val
    ax.set_xlim([posx, posx+0.1])
    #ax.set_ylim([posy, posy+0.1])
def updatey(val):
    posy = s_data.val
    print(posy)
    #ax.set_ydata(s_data.val, s_time.val)
    ax.set_ylim([posy-1, posy+0.1])    
# ====================================Main GUI=====================================
main_window = Tk()
main_window.title("Signal Viewer")
main_window.configure(background='light green')
main_window.geometry('1020x600')

w = Label(main_window, text=" Signals Color ",fg = "red", font = ('Times',18))
w.pack()
w.place(x = 840,y = 160) 



#fig = plt.figure()
#ax = fig.add_subplot(111)
fig, ax=plt.subplots(dpi=90)

spectrocanvas = FigureCanvasTkAgg(fig, master=main_window)
spectrocanvas.get_tk_widget().place(x =10, y = 0, width = 410, height = 400)
spectrocanvas.draw()

#<------------------------------------------Test 2nd graph
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.set_title("Spectogram")
#ax2.set_xlabel("Number of readings")
canvas = FigureCanvasTkAgg(fig2, master=main_window)
canvas.get_tk_widget().place(x =420, y = 0, width = 400, height = 400)
canvas.draw()
#<-----------------------------Toolbar & PDF---------------
toolbar2 = NavigationToolbar2Tk(canvas,main_window)
toolbar2.update()

toolbar = NavigationToolbar2Tk(spectrocanvas,main_window)
toolbar.update()


ax_time = fig.add_axes([0.12, 0.03, 0.78, 0.03])
s_time = Slider(ax_time, 'Time', 0, 1, valinit=0)
s_time.on_changed(updatex)

# Make a vertically oriented slider to control the amplitude
ax_data = fig.add_axes([0.020, 0.07, 0.0225, 0.80])
s_data = Slider(ax_data,label="Data",valmin=0,valmax=1,valinit=0,orientation="vertical")
s_data.on_changed(updatey)

#scrollY = Scrollbar(spectrocanvas.get_tk_widget(), orient=VERTICAL,command=spectrocanvas.yview)
#scrollX = Scrollbar(spectrocanvas.get_tk_widget(), orient=HORIZONTAL, command=spectrocanvas.xview)
#spectrocanvas['xscrollcommand'] = scrollX.set
#spectrocanvas['yscrollcommand'] = scrollY.set 

        
#scrollbar1 = Scrollbar(spectrocanvas.get_tk_widget(), orient=HORIZONTAL)
#scrollbar1.pack(side=BOTTOM,fill=X)
#spectrocanvas.get_tk_widget().config(xscrollcommand=scrollbar1.set)

#scrollbar2 = Scrollbar(spectrocanvas.get_tk_widget(), orient=VERTICAL)
#scrollbar2.pack(side=RIGHT,fill=Y)




savepdf1 = Button(text="PDF1",width=5, height=1,command=SavePdf1)
savepdf1.pack()
savepdf1.place(x=10, y=500)

savepdf2 = Button(text="PDF2",width=5, height=1,command=SavePdf2)
savepdf2.pack()
savepdf2.place(x=100, y=500)

savepdf3 = Button(text="PDF3",width=5, height=1,command=SavePdf3)
savepdf3.pack()
savepdf3.place(x=200, y=500)
#<------------------------------Images---------------
photo = PhotoImage(file = r"play.png")
photoimage = photo.subsample(3, 3)

photo1 = PhotoImage(file = r"stop.png")
photoimage1 = photo1.subsample(17, 17)

photo2 = PhotoImage(file = r"clear.png")
photoimage2 = photo2.subsample(15, 15)

photo3 = PhotoImage(file = r"spectrometer.png")
photoimage3 = photo3.subsample(15, 15)

#<-----------------------------Change Color AND Speed---------------
red1 = Button(text="Red 1",width=4, height=1,command=red1)
red2 = Button(text="Red 2",width=4, height=1,command=red2)
red3 = Button(text="Red 3",width=4, height=1,command=red3)

red1.pack()
red2.pack()
red3.pack()

blue1 = Button(text="Blue1",width=4, height=1,command=blue1)
blue2 = Button(text="Blue2",width=4, height=1,command=blue2)
blue3= Button(text="Blue3",width=4, height=1,command=blue3)

blue1.pack()
blue2.pack()
blue3.pack()

green1 = Button(text="Green1",width=5, height=1,command=green1)
green2 = Button(text="Green2",width=5, height=1,command=green2)
green3 = Button(text="Green3",width=5, height=1,command=green3)

green1.pack()
green2.pack()
green3.pack()


speedDown = Button(text="speed-",command=speedDown)
speedDown.pack()
speedUp = Button(text="speed+",command=speedUp)
speedUp.pack()

#--------------------------------Spectogram color Dropdown menu options---------------->
options = ["viridis","rainbow","inferno","ocean","Greys"]
# datatype of menu text
clicked = StringVar()
# initial menu text
clicked.set("Spectogram Palette")
# Create Dropdown menu
drop = OptionMenu(main_window,clicked , *options )
drop.pack()
drop.place(x=840, y=300)
#--------------------------------Spectogram Dropdown menu options---------------->
mytkcombo = ttk.Combobox(main_window, values=files, postcommand = updateFilelist)
mytkcombo.set('Choose specific signal')
#Set Combobox Position in Python
mytkcombo.place(x=630, y=460, anchor='center')
mytkcombo['state'] = 'readonly'

v_min = DoubleVar()
v_max = DoubleVar()
slider1 = Scale(main_window,from_=-500,to=0,orient='horizontal',variable=v_min)
slider2 = Scale(main_window,from_=0,to=500,orient='horizontal',variable=v_max)
slider1.place(x=860, y=400)
slider2.place(x=860, y=450)


#<-------------------------------------Buttons1----------------------------------------------
Upload1 = Button(text='Upload1',width=10, height=2 ,command=UploadAction1)
Upload2 = Button(text='Upload2',width=10, height=2 ,command=UploadAction2)
Upload3 = Button(text='Upload3',width=10, height=2 ,command=UploadAction3)
start_button1 = Button(text='1     ',image = photoimage,compound = LEFT, command=graphing1)
start_button2 = Button(text='1,2   ',image = photoimage,compound = LEFT, command=graphing2)
start_button3 = Button(text='1,2,3 ',image = photoimage,compound = LEFT, command=graphing3)
Upload1.pack()
Upload2.pack()
Upload3.pack()
start_button1.pack()
start_button2.pack()
start_button3.pack()
specto = Button(text="Spectogram",image = photoimage3,compound = LEFT, command=specto)
specto.pack()
stop = Button(text="Stop",image = photoimage1,compound = LEFT,command=stop)
stop.pack()
specto2 = Button(text="Clear Graph",image = photoimage2,compound = RIGHT, command=refreshFigure)
specto2.pack()
#<-------------------------------------Toggle----------------------------------------------
toggle1 = BooleanVar()
hide1 = Checkbutton(text="Show signal 1", variable=toggle1, command=toggleHide1) 
hide1.select()
hide1.place(x=860, y=10)

toggle2 = BooleanVar()
hide2 = Checkbutton(text="Show signal 2", variable=toggle2, command=toggleHide2) 
hide2.select()
hide2.place(x=860, y=35)

toggle3 = BooleanVar()
hide3 = Checkbutton(text="Show signal 3", variable=toggle3, command=toggleHide3) 
hide3.select()
hide3.place(x=860, y=60)

specto.place(x=510, y=400)

Upload1.place(x=10, y=400)
Upload2.place(x=90, y=400)
Upload3.place(x=170, y=400)

start_button1.place(x=18, y=442)
start_button2.place(x=98, y=442)
start_button3.place(x=176, y=442)
stop.place(x=260, y=400)
specto2.place(x=640, y=400)

red1.place(x=850, y=200)
red2.place(x=850, y=230)
red3.place(x=850, y=260)

blue1.place(x=890, y=200)
blue2.place(x=890, y=230)
blue3.place(x=890, y=260)

green1.place(x=930, y=200)
green2.place(x=930, y=230)
green3.place(x=930, y=260)


speedDown.place(x=850, y=100)
speedUp.place(x=925, y=100)

main_window.mainloop()