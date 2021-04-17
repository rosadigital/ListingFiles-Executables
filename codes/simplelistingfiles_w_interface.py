import os
from pathlib import Path
from hurry.filesize import size, verbose
from csv import writer, QUOTE_NONE
from tkinter.ttk import *
from tkinter import *
from threading import Thread

'''SimpleListingFiles_w_interface: This algorithm maps a directory and list its files names and sizes on a csv file (listingfiles.csv). It uses TKinter to create a Graphic interface for users (while processing, using threading), but it does not use Pandas (to create DataFrame) or Numpy (to manipulate data). Its executable size created by pyinstaller is about: 9.5mb.'''

def listing_files():
    # creating heading and saving into csv
    heading = 'name,size'
    filename = 'listingfiles.csv'
    with open(filename, 'a', encoding='utf-8', newline='') as csvfile:
        writer_object = writer(csvfile, delimiter=' ', escapechar=' ', quoting=QUOTE_NONE)
        writer_object.writerow([heading])
        csvfile.close()

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

    # creating dict data
    name_size = [name, filesize]

    # #transposing dict data
    transposing_name_size = [[name_size[j][i] for j in range(len(name_size))] for i in range(len(name_size[0]))]

    # transposed dict data to string data
    with open(filename, 'a', encoding='utf-8', newline='') as csvfile:
        for line_dict in transposing_name_size:
            newline_string = ','.join([str(line_string) for line_string in line_dict])

            writer_object = writer(csvfile, delimiter=' ', escapechar=' ', quoting=QUOTE_NONE)
            writer_object.writerow([newline_string])

        csvfile.write('\nListingFiles developed by: Felipe Rosa on 16.04.2021'
                   '\nGit: https://github.com/rosadigital (for newest version)'
                   '\nLinkedIn: https://www.linkedin.com/in/felipe-rosa/ (for suggestion)')
        csvfile.close()

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