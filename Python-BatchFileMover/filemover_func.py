# Python:       3.6.1
#
# Author:       Chris Ling
#
# Description:  F'ns for GUI for creating an automatic script to check and move files 
#               created or modified in the last 24 hours, every 24 hours, plus 
#               the option to manually run the file transfer script.

import shutil,os,time,datetime
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
import sqlite3

# This sets up the initial file paths and directories for the GUI
def initial_dir(self):
    self.dir_src = 'C:/Users/chris/Desktop/Folder A/'
    self.dir_dst = 'C:/Users/chris/Desktop/Folder B/'

    update_ent_src(self)
    update_ent_dst(self)
    update_lst_src(self)
    update_lst_dst(self)

# This allows the user to change directories and load the file contents    
def get_directory(self, location):

    if location == 'src':
        self.dir_src = fd.askdirectory()+'/'
        update_ent_src(self)
        update_lst_src(self)
        
    elif location == 'dst':
        self.dir_dst = fd.askdirectory()+'/'
        update_ent_dst(self)
        update_lst_dst(self)

# This updates the _src Entry box with the new file path
def update_ent_src(self):
    
    self.ent_src.state(['!readonly'])
    self.ent_src.delete(0,'end')
    self.ent_src.insert(0,self.dir_src)
    self.ent_src.state(['readonly'])

# This updates the _dst Entry box with the new file path
def update_ent_dst(self):

    self.ent_dst.state(['!readonly'])
    self.ent_dst.delete(0,'end')
    self.ent_dst.insert(0,self.dir_dst)
    self.ent_dst.state(['readonly'])

# This updates the _lastchk Entry box with the timestamp
def update_ent_lastchk(self):

    self.ent_lastchk.state(['!readonly'])
    self.ent_lastchk.delete(0,'end')
    self.ent_lastchk.insert(0,self.last_datestamp[0])
    self.ent_lastchk.state(['readonly'])   

# This updates the _src List box with the new file path
def update_lst_src(self):
    self.lst_src.delete(0,'end')
    self.path_src=str(self.dir_src)
    for i in os.listdir(self.path_src):
        self.lst_src.insert(0,i)

# This updates the _dst List box with the new file path
def update_lst_dst(self):
    self.lst_dst.delete(0,'end')
    self.path_dst=str(self.dir_dst)
    for i in os.listdir(self.path_dst):
        self.lst_dst.insert(0,i)

# This allows for the manual option of transferring files through the GUI
def filemove(self):

    if self.path_src == '' or self.path_dst == '' or self.path_src == self.path_dst:
        messagebox.showinfo(title="Transfer Failed", message="You need to select two different source and destination paths to transfer files!")

    else:
        filemove_bg(self)
        update_lst_src(self)
        update_lst_dst(self)

# This is the stripped-down file transfer script that can run in the background if the GUI closes
def filemove_bg(self):
    self.unix=time.time()
    self.datestamp=datetime.datetime.fromtimestamp(self.unix).strftime('%Y-%m-%d, %H:%M:%S')
    for i in os.listdir(self.path_src):

        if (self.unix - os.path.getctime(self.path_src+i) <= 86400) or (self.unix - os.path.getmtime(self.path_src+i) <= 86400):

            print('Moving: \''+self.path_src+i+'\'')
            print('To:     \''+self.path_dst+i+'\'')
            shutil.move(self.path_src+i,self.path_dst)

    print ('\n*Complete for '+self.datestamp+'*')
    save_timestamp(self)

def save_timestamp(self):
    
    conn = sqlite3.connect('timestamp.db')
    c = conn.cursor()

    c.execute ('''
        CREATE TABLE IF NOT EXISTS Filecheck
        (Unix REAL, Datestamp TEXT, Fol_A TEXT, Fol_B TEXT);
        ''')

    c.execute ('''INSERT INTO Filecheck VALUES (?,?,?,?)''', (self.unix,self.datestamp,self.path_src,self.path_dst))

    c.execute ('''SELECT MAX(Datestamp) FROM Filecheck''')
    self.last_datestamp = c.fetchone()

    conn.commit()
    conn.close()
    update_ent_lastchk(self)

def initial_timestamp(self):
    try:
        conn = sqlite3.connect('timestamp.db')
        c = conn.cursor()
        c.execute ('''SELECT MAX(Datestamp) FROM Filecheck''')
        self.last_datestamp = c.fetchone()
        conn.commit()
        conn.close()
        update_ent_lastchk(self)
    except:
        self.ent_lastchk.state(['readonly'])
    
if __name__ =='__main__':
    pass
