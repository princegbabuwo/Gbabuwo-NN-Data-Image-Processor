#Image Processor
import numpy as np
from modules import file_io as io

def main():
    raw_path = "C:/Users/USER/OneDrive/Tech/Data Science/Data/Raw Images/"
    #arrayFile = "data.txt"

    fileIO = io.FileIO(raw_path=raw_path)
    print(fileIO)

    unprocessed_files = np.random.permutation(fileIO.unprocessed_files)
    print (unprocessed_files)

    #CODE Display unprocessed file image in console
    #CODE input image features such as cat-face, dog-face, None
    #TODO convert file to jpeg
    #CODE SHRINK OR EXPAND FILE TO 64 X 64px
    #CODE Get RGB Data of file
    #CODE Update filename based on the last file processed
    #CODE Store meta-data to processed array file

    #print (fileIO)

main()