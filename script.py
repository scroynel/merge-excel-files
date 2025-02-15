# script to merging excel files
import pandas as pd
import os


class MergingFiles():
    def __init__(self, path_merge, path_save):
        self.path_merge = path_merge
        self.path_save = path_save
        self.merging_files()
    
    def merging_files(self):
        files = [file for file in os.listdir(self.path_merge) if file.endswith('.xlsx')]

        dataframe_list = []
        for file in files:
            data = pd.read_excel(os.path.join(self.path_merge, file))
            dataframe_list.append(data)

        merged_data = pd.concat(dataframe_list, ignore_index=True) 

        merged_data.to_excel(os.path.join(self.path_save, 'merged_files.xlsx'))

        return print('Congrats! The merging was complited.')


if __name__ == '__main__':
    path1 = input("Enter path to the folder where there are files what i need to merge: ")
    path2 = input("Enter path to the folder where we can save that merged file: ")
    MergingFiles(path1, path2)