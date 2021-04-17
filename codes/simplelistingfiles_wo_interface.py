import os
from pathlib import Path
from hurry.filesize import size, verbose
from csv import writer, QUOTE_NONE

'''SimpleListingFiles: This algorithm maps a directory and list its files names and sizes on a csv file (listingfiles.csv). It is called Simple because it does not have Graphic interface for users and does not use Pandas (to create DataFrame) or Numpy (to manipulate data). Its executable size created by pyinstaller is about: 6.6mb.'''

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

if __name__ == '__main__':
    listing_files()