import os
from threading import Thread
from pathlib import Path
import pandas as pd
from hurry.filesize import size, verbose
from tkinter.ttk import *
from tkinter import *

'''ListingFiles_w_interface: This algorithm maps a directory and list its files names and sizes on a csv file (listingfiles.csv). It uses TKinter to create a Graphic interface for users (while processing, using threading), as well as, Pandas (to create DataFrame and CSV). Its executable size created by pyinstaller is about: 30mb.'''

def listing_files():
    # current directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files_in_dir_path = Path(dir_path).iterdir()

    # getting data
    name = []
    filesize = []
    for item in files_in_dir_path:
        if item.is_file():
            name.append(item.name)
            filesize.append(size(os.stat(item.name).st_size, system=verbose))
        else:
            pass

    # organizing data
    df_listing_all = pd.DataFrame({
        'name': name,
        'size': filesize
    })

    #saving data
    place_to_save = str(dir_path) + '\\' + 'fileslist.csv'
    df_listing_all.to_csv(place_to_save, index=False)

    file = open('fileslist.csv', 'a')
    file.write('\nListingFiles developed by: Felipe Rosa on 16.04.2021'
               '\nGit: https://github.com/rosadigital (for newest version)'
               '\nLinkedIn: https://www.linkedin.com/in/felipe-rosa/ (for suggestion)')
    file.close()

def processing_message():
    # creating window
    root = Tk()
    root.title('ListingFiles by Felipe Rosa')
    root.geometry("300x300")
    root.grid_columnconfigure(1, minsize=300)

    # formating data to be showed
    blank_space_top = Label(root, text='', height=6) #blank space need to centralize content
    message = Label(root, text='Please Wait \n listing documents', bg='brown',fg='white', font=('helvetica', 12, 'bold'), width=25)
    blank_space_center = Label(root, text='', width=25) #blank space need to centralize content
    progress_bar = Progressbar(root, orient=HORIZONTAL, length=200, mode='indeterminate')
    progress_bar.start(5) #speed of progress bar: 1 is very fast

    # adjusting data on screen
    blank_space_top.grid(row=0, column=1)
    message.grid(row=1, column=1)
    blank_space_center.grid(row=2, column=1)
    progress_bar.grid(row=3, column=1)

    #closing canvas
    root.after(1000, root.destroy)
    mainloop()

def concluded_message():
    # creating window
    root = Tk()
    root.title('ListingFiles by Felipe Rosa')
    root.geometry("300x300")
    root.grid_columnconfigure(1, minsize=300)

    # formating data to be showed
    blank_space_top = Label(root, text='', height=8) #blank space need to centralize content
    message = Label(root, text='DONE: all documents listed', fg='green', font=('helvetica', 12, 'bold'), width=30)
    blank_space_center = Label(root, text='', width=25) #blank space need to centralize content

    # adjusting data on screen
    blank_space_top.grid(row=0, column=1)
    message.grid(row=1, column=1)
    blank_space_center.grid(row=2, column=1)

    # closing canvas
    root.after(5000, root.destroy)
    mainloop()

if __name__ == '__main__':
    ##Thread used to process the listing_files and show processing message at the same time
    Thread(target=processing_message()).start()
    Thread(target=listing_files()).start()
    concluded_message()