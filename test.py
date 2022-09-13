import csv
import seaborn
import matplotlib
import numpy
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog
import matplotlib
matplotlib.use("TkAgg")
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

#0-7, 0,2,4,6 are metadata
#0-1 are 18, 2-3 are 19, 4-5 are 20, 6-7 are 21
md31018 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200118\310\metadata.csv"
sm31018 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200118\310\summary.csv"
md31019 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200119\310\metadata.csv"
sm31019 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200119\310\summary.csv"
md31020 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200120\310\metadata.csv"
sm31020 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200120\310\summary.csv"
md31021 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200121\310\metadata.csv"
sm31021 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200121\310\summary.csv"


#8-15, 8, 10, 12, 14, are metadata
md31118 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200118\311\metadata.csv"
sm31118 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200118\311\summary.csv"
md31119 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200119\311\metadata.csv"
sm31119 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200119\311\summary.csv"
md31120 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200120\311\metadata.csv"
sm31120 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200120\311\summary.csv"
md31121 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200121\311\metadata.csv"
sm31121 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200121\311\summary.csv"


#16-23, 16, 18, 20, 22 are metadata
md31218 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200118\312\metadata.csv"
sm31218 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200118\312\summary.csv"
md31219 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200119\312\metadata.csv"
sm31219 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200119\312\summary.csv"
md31220 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200120\312\metadata.csv"
sm31220 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200120\312\summary.csv"
md31221 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200121\312\metadata.csv"
sm31221 = r"C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200121\312\summary.csv"

data_arr = [md31018,sm31018,md31019,sm31019,md31020,sm31020,md31021,sm31021,
            md31118,sm31118,md31119,sm31119,md31120,sm31120,md31121,sm31121,
            md31218,sm31218,md31219,sm31219,md31220,sm31220,md31221,sm31221]


#df = pd.read_csv(r'C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200118\310\metadata.csv')
df = pd.read_csv(r'C:\Users\aleis\Documents\classes\Fall2022\Software\Term_Proj\Dataset\Dataset\20200118\310\summary.csv')

#print(df)

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("csv files","*.csv*"),("all files","*.*")))    
    
                                                                                                            
    # Create the root window
    window = Tk()

    # Set window title
    window.title('File Explorer')
      
    # Set window size
    window.geometry("500x500")
      
    #Set window background color
    window.config(background = "white")
      
    # Create a File Explorer label
    label_file_explorer = Label(window, text = "File Explorer using Tkinter", width = 100, height = 4, fg = "blue")
   
    button_explore = Button(window, text = "Browse Files", command = browseFiles)
      
    button_exit = Button(window,text = "Exit", command = exit)

    label_file_explorer.grid(column = 1, row = 1)
    button_explore.grid(column = 1, row = 2)
    button_exit.grid(column = 1,row = 3)

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename)

    window.destroy()

    return filename
      
    # Let the window wait for any events
    #window.mainloop()

#a = browseFiles()
##def pltit(df):
##    #df.plot(x=df.columns[0], y=df.columns[3])
##    df.plot(x="Datetime (UTC)", y="Steps count")
##    print(participant_date)
##    print(time_zone_info)
##    print(date_interval_1)
##    print(date_interval_2)
##    plt.show()

def all_plots():

    participant_date = global_dict["participant_date"]
    time_zone_info = global_dict["time_zone_info"]
    date_interval_1 = global_dict["date_interval_1"]
    date_interval_2 = global_dict["date_interval_2"]

##    print(participant_date)
##    print(time_zone_info)
##    print(date_interval_1)
##    print(date_interval_2)

    print(participant_date)
    print(time_zone_info)
    print(date_interval_1)
    print(date_interval_2)

    total_df = []

    #all participants
    if(participant_date == 0):

        print("A", end="")

        #single date, CHECK THIS
        if((date_interval_1 == 0 and date_interval_2 != 0)
           or (date_interval_1 != 0 and date_interval_2 == 0)
           or (date_interval_1 == date_interval_2 and date_interval_1 != 0)):

            print("1")
            
            if(date_interval_1 != date_interval_2):
                date_interval = (date_interval_1 ^ date_interval_2) - 1
            else:
                date_interval = date_interval_1 - 1

            for i in range(0, 23, 8):
                total_df.append(data_arr[i + date_interval + 1])

            if(time_zone_info == 1):
                for i in range(0, 23, 8):
                    total_df.append(data_arr[i + date_interval])  


        #need one for a date range?
        elif(date_interval_1 != date_interval_2 and date_interval_1 != 0):

            print("2")

            if(date_interval_1 > date_interval_2):
                x = date_interval_1
                date_interval_1 = date_interval_2
                date_interval_2 = x


            print(date_interval_1)
            print(date_interval_2)
            for i in range(((date_interval_1-1) * 2), ((date_interval_2-1) * 2)+1, 2):
                total_df.append(data_arr[i+1])
                total_df.append(data_arr[i+9])
                total_df.append(data_arr[i+17])
            if(time_zone_info == 1):
                for i in range(((date_interval_1-1) * 2), ((date_interval_2-1) * 2)+1, 2):
                    total_df.append(data_arr[i])
                    total_df.append(data_arr[i+8])
                    total_df.append(data_arr[i+16])        
        
        #all values
        else:
            
            print("3")
            if(time_zone_info == 1):
                total_df = data_arr
            else:
                for i in range(1, 24, 2):
                    total_df.append(data_arr[i])

    #single participant
    else:

        print("B", end="")
        #single date
        if((date_interval_1 == 0 and date_interval_2 != 0)
           or (date_interval_1 != 0 and date_interval_2 == 0)
           or (date_interval_1 == date_interval_2 and date_interval_1 != 0)):

            print("1")
            
            if(date_interval_1 != date_interval_2):
                date_interval = (date_interval_1 ^ date_interval_2) - 1
            else:
                date_interval = date_interval_1 - 1

            participant = participant_date - 1
            loc = (participant * 8) + (date_interval * 2) + 1
            total_df.append(data_arr[loc])

            if(time_zone_info == 1):
                total_df.append(data_arr[loc-1])

        #all dates
        else:

            print("2")
            
            participant = participant_date - 1

            print(participant)
            for i in range((8 * participant), (8 * (participant+1)), 2):
                total_df.append(data_arr[i+1])

            if(time_zone_info == 1):
                for i in range((8 * participant), (8 * (participant+1)), 2):
                    total_df.append(data_arr[i])       

    print(total_df)
    return total_df
    

#fix ugly axis
#will send a list
def pltit(df, page):

    arr = all_plots()    
    #df.plot(x=df.columns[0], y=df.columns[3])
    #fig = Figure(figsize = (5, 5), dpi = 100)
    #ax = fig.add_subplot(111)

    fig1 = df.plot(x="Datetime (UTC)", y="Steps count", figsize=(5,3)).get_figure()
    fig2 = df.plot(x="Datetime (UTC)", y="Temp avg", figsize=(5,3)).get_figure()
    canvas = FigureCanvasTkAgg(fig1, master=page)
    canvas2 = FigureCanvasTkAgg(fig2, master=page)

    #canvas = FigureCanvasTkAgg(fig2, master=page)
    canvas.draw()
    canvas2.draw()
    
    #canvas.show()
    #canvas.get_tk_widget().pack()
    #toolbar = NavigationToolbar2Tk(canvas,
    #                              page)
    #toolbar.update()
    canvas.get_tk_widget().pack()
    canvas2.get_tk_widget().pack()
    #toolbar.pack(side=RIGHT)

def list():

    window = Tk()
    window.geometry('100x150')
    list = Listbox(window, selectmode = "multiple")
    list.pack(expand = YES, fill = "both")
    x = ["User", "Date"]
      
    for each_item in range(len(x)):
        list.insert(END, x[each_item])       
    window.mainloop()

def dropdown():

    window = Tk()
    var = StringVar(window)
    var.set("Participant")
    w = OptionMenu(window, var, "Participant", "Date")
    w.pack()

    mainloop()


def testlable():
    root = Tk()

    test = Label(root, text="Red", bg="red", fg="white")
    test.pack(side=BOTTOM)
    test = Label(root, text="Green", bg="green", fg="white")
    test.pack(side=BOTTOM)
    test = Label(root, text="Purple", bg="purple", fg="white")
    test.pack(side=BOTTOM)

    mainloop()

def buttontest():

    top = Tk()

    def helloCallBack():
       messagebox.showinfo( "Hello Python", "Hello World")

    B = Button(top, text ="Hello", command = helloCallBack)

    B.pack()
    top.mainloop()

    

def date_interval_set(var, interval):
    
    choice = var.get()
    date = 0
    
    date = times.index(choice)

    if(interval == 1):
        global_dict["date_interval_1"] = date
    if(interval == 2):
        global_dict["date_interval_2"] = date

def time_zone_set(var):

    choice = var.get()
    global_dict["time_zone_info"] = time_zones.index(choice)

def participant_date_set(var):
    
    choice = var.get()
    global_dict["participant_date"] = participants.index(choice)
    

times = ["No Date Selected", "2020-01-18",
         "2020-01-19","2020-01-20","2020-01-21"]

participants = ["Date","Participant 310", "Participant 311",
                "Participant 312"]

time_zones = ["No Time Zone Info", "Time Zone Info"]

global_dict = {"participant_date":0, "time_zone_info":0,
               "date_interval_1":0, "date_interval_2":0}

global_plt = {}





#Test multiple Pages
    
class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()
    def add_button(self, default, name_list, function):
        var = StringVar(self)
        var.set(default)
        w = OptionMenu(self, var, *name_list, command=lambda _: function(var))
        w.pack()
                    

class Page1(Page):
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Label(self, text="This is page 1")
       label.pack(side="top", fill="both", expand=True)
    

class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def plt_me(self):

        self.clean() #?
        arr = all_plots()
        df_arr = []
        
        fig, axes = plt.subplots(len(arr))
        n = 0

        for i in arr:
            if(i != md31120 and i != sm31120
               and i != md31121 and i != sm31121):
                print(i)
                df = pd.read_csv(i)

                #print(df)

                fig = df.plot(ax=axes[n], x="Datetime (UTC)",
                              y="Steps count", figsize=(5,5)).get_figure()

                n = n + 1       
        
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)

        #frame = Frame(canvas)
        #vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
        #canvas.configure(yscrollcommand=vsb.set)

        #vsb.pack(side="right", fill="y")
       # canvas.pack(side="left", fill="both", expand=True)
        #canvas.create_window((4,4), window=frame, anchor="nw")

        #frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

        
        
    def clean(self):
        for item in self.winfo_children():
            print(item)
            item.destroy()

class Page3(Page):
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Button(buttonframe, text="Page 1", command=p1.show)
        b2 = Button(buttonframe, text="Page 2", command=p2.show)
        b3 = Button(buttonframe, text="Page 3", command=p3.show)

        var1 = StringVar(p1)
        var1.set("Participant 310")
        w = OptionMenu(p1, var1, *participants, command=lambda _: participant_date_set(var1))
        w.pack()

        var2 = StringVar(p1)
        var2.set("No Time Zone Info")
        x = OptionMenu(p1, var2, *time_zones, command=lambda _: time_zone_set(var2))
        x.pack()

        var3 = StringVar(p1)
        var3.set("No Date Selected")
        y = OptionMenu(p1, var3, *times, command=lambda _: date_interval_set(var3, 1))
        y.pack()

        var4 = StringVar(p1)
        var4.set("No Date Selected")
        z = OptionMenu(p1, var4, *times, command=lambda _: date_interval_set(var4, 2))
        z.pack()

        #p2.plt_me()

        #remove all widgets, nice...
        p2.clean()
        
        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        #b1_1 = Button(p1, text="Graph Me!", command=lambda : pltit(df, p2))
        b1_1 = Button(p1, text="Graph Me!", command=lambda : p2.plt_me())

        b1_1.pack()


        p1.show()

if __name__ == "__main__":
    
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()
