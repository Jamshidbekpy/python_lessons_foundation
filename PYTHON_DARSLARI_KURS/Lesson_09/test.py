from openpyxl import Workbook, load_workbook
from datetime import datetime
from pickle import dump, load
from os import rmdir, path, remove, listdir, getcwd, chdir, mkdir, rename

wb = Workbook()
ws = wb.active
def database_first():
    database_name  = 'database.dat'
        
    