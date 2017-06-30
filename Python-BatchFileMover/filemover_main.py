# Python:       3.6.1
#
# Author:       Chris Ling
#
# Description:  GUI for creating an automatic script to check and move files 
#               created or modified in the last 24 hours, every 24 hours, plus 
#               the option to manually run the file transfer script.

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import filemover_func as fmf
import threading, time

class MainWindow:

    def __init__(self,master):

        # All variables with _src refer to "source path" while _dst refer to "destination path"
        master.minsize(500,200)
        grid_frame = ttk.Frame(master)
        grid_frame.pack()
        self.path_src = ''
        self.path_dst = ''

        # GUI buttons
        self.but_src = ttk.Button(grid_frame, text="Source Path", command=lambda: fmf.get_directory(self, 'src'))
        self.but_dst = ttk.Button(grid_frame, text="Destination", command=lambda: fmf.get_directory(self, 'dst'))
        self.but_man = ttk.Button(grid_frame, text="Manual Transfer", command=lambda: fmf.filemove(self))
        self.but_src.grid(row=0, column=0)
        self.but_dst.grid(row=0, column=3)
        self.but_man.grid(row=3, column=0, columnspan=3)

        # GUI entries
        self.ent_src = ttk.Entry(grid_frame, width=37)
        self.ent_dst = ttk.Entry(grid_frame, width=37)
        self.ent_lastchk = ttk.Entry(grid_frame, width=34)
        self.ent_src.grid(row=0, column=1)
        self.ent_dst.grid(row=0, column=4)
        self.ent_lastchk.grid(row=3,column=4, columnspan=2)

        # GUI labels
        self.lab_lastchk = ttk.Label(grid_frame, text="Last Check:")
        self.lab_lastchk.grid(row=3,column=3)

        # GUI listboxes with scrollbars
        self.scroll_src = Scrollbar(grid_frame, orient=VERTICAL)
        self.lst_src = tk.Listbox(grid_frame, width=50, yscrollcommand=self.scroll_src.set)
        self.scroll_src.config(command=self.lst_src.yview)

        self.scroll_dst = Scrollbar(grid_frame, orient=VERTICAL)
        self.lst_dst = tk.Listbox(grid_frame, width=50, yscrollcommand=self.scroll_dst.set)
        self.scroll_dst.config(command=self.lst_dst.yview)

        self.lst_src.grid(row=1,column=0,columnspan=2)
        self.scroll_src.grid(row=1,column=2, sticky=N+S)
        self.lst_dst.grid(row=1,column=3,columnspan=2)
        self.scroll_dst.grid(row=1,column=5, sticky=N+S)

        # Set up initial source and destination paths with list of files in respective paths
        fmf.initial_dir(self)
        fmf.initial_timestamp(self)
    
def main():

    root = tk.Tk()
    app = MainWindow(root)

    # Rather than using schedule, which prevents the use of the GUI while running, I created
    # a separate thread tied it to a time.sleep function = 24 hours from when the program started.
    # The thread is placed outside the GUI class so that it runs AFTER the GUI loads, and can
    # continue running after you close the GUI window, in the background.
    def daily_schedule():
        while 1:
            time.sleep(86400)
            fmf.filemove_bg(app)
    threadObj = threading.Thread(target=daily_schedule)
    threadObj.start()

    
    root.mainloop()

if __name__ == "__main__": main()
