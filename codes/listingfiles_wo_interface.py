import os
from pathlib import Path
from pandas import DataFrame
from hurry.filesize import size, verbose

'''ListingFiles_w/o_interface: This algorithm maps a directory and list its files names and sizes on a csv file (listingfiles.csv). It does not create a Graphic interface for users, but uses Pandas (to create DataFrame and CSV). Its executable size created by pyinstaller is about: 27mb.'''

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
    df_listing_all = DataFrame({
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

if __name__ == '__main__':
    listing_files()