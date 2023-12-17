#This modules has a class that handles everything on file i/o for this cat image mapper applocation

import os  #python library for file i/o
import json #import to manage json and py dictionaries#
import numpy as np

# SUMMARY
# Array Data for Processed file arranged as
# meta-data[i] = [RGB of data in 64px x 64px stored as a column vector]
# data[i] = [raw-file-name, processed-file-name, meta-data[i], is-cat, is-dog, in-NONE]
# data = [[data1], [data2], [data3], ...]

class FileIO:
    raw_path  = None
    processed_path  = "Processed Images/"
    array_file = "data.txt"
    raw_files = np.array([])
    processed_data = np.array([])
    processed_files = np.array([])
    unprocessed_files = np.array([])
    #TODO Upadte all va_r variables above to vaR variables

    def __init__(self,  raw_path=raw_path):
        self.raw_path = raw_path
        self.processed_path = raw_path + self.processed_path
        self.array_file_path = self.processed_path + self.array_file

        #TODO Consider cases where folder is empty
        self.raw_files = self.__ListRawFiles()
        self.processed_data = self.__ProcessedData()
        if np.any(self.processed_data):
            self.processed_file = self.processed_data[:, 0]
            #CODE Define UnprocessedFiles
        else:
            self.unprocessed_files = self.raw_files
        #return np.random.permutation(unprocessedFiles)

    """
    def GetUnprocessedFiles(self):
        rawFiles = self.__ListRawFiles()
        processedData = self.__ProcessedData()
        if np.any(processedData):
            processedFiles = processedData[:, 0]
            #CODE Define UnprocessedFiles
        else:
            unprocessedFiles = rawFiles
        return np.random.permutation(unprocessedFiles)
    """

    def __ListRawFiles(self): 
        arr = np.array(os.listdir(self.raw_path))
        return arr[arr != "Processed Images"]
    
    def __ProcessedData(self):
        data = np.array([])
        #check if text file exist containing array.
        if os.path.exists(self.array_file_path):
            #CODE get processed file from the list
            #print ("File found, Line 30")
            return data
        
        try:
            if not os.path.exists(self.processed_path):
                os.makedirs(self.processed_path)
            with open(self.array_file_path, 'w') as file:
                pass
            #np.savetxt(self.array_file_path, data)
            print("Array File Created")
        except Exception as e:
            #print(e)
            raise ValueError(f"Error @file_io.ListProcessedFile: {e}")
        finally:
            return data


    def __str__(self):
        _dict = {
            'raw-path': self.raw_path,
            'processed-path':  self.processed_path, 
            'array-file-path': self.array_file_path,
            'raw-files': self.raw_files.tolist(),
            'processed-data': self.processed_data.tolist(),
            'processed-files': self.processed_files.tolist(),
            'unprocessed-files': self.unprocessed_files.tolist(),
        }
        return json.dumps(_dict, indent=4)