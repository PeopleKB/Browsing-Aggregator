from pprint import pprint

from os import listdir
from itertools import groupby
from urllib.parse import unquote

types = ['raw_android_tab_list', 'processed_android_tab_list']

# Get list of input files and their types
filenames = listdir('input') #TODO handle subdirectories

def id_input_type(input_filename):
    pass

# Read Android Chrome tabs file

def process_raw_android_tab_list(filename):
    with open('input/' + filename) as f:
        lines = f.readlines()
    
    def structure_tab(group):
        lines = list(group)
        n_lines = len(lines)

        if n_lines == 0:
            return n_lines #TODO How to handle these errors properly?

        link = lines[0]
        if not link.startswith('http'):
            if link.startswith('chrome-distiller://'):
                link = unquote(link.split('url=')[1])
            elif link.startswith('file:///'):
                pass #TODO Handle local android files!!
            else:
                return n_lines #TODO How to handle these errors properly?

        if n_lines == 2:
            title = lines[1]
        else:
            title = " - ".join([line.rstrip() for line in lines[1:]])

        return {'link': link, 'title': title}

    tabs = [structure_tab(group) for test, group in groupby(lines, lambda y: y != 'Inspect\n' and y != '\n') if test]
    return tabs



process_raw_android_tab_list(filenames[0])





# Read TabsOutliner text dump

# Read TabsOutliner tree file

# Read TabsOutliner html save
