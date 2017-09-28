import sys
import os
import json

arguments = sys.argv


def check_arguments(arguments):
    if(len(arguments) < 2):
        return (False, 'Script requires a mount path argument.')
    elif(os.path.isdir(arguments[1]) is False):
        return (False, '{} does not exist or is not a directory.'.format(arguments[1]))
    else:
        return (True, 'No errors found.')

error_check_results = check_arguments(arguments)

if(error_check_results[0] is False):
    print(error_check_results[1])
    quit()

mount_loc = arguments[1]

file_dict = {}
file_value_array = []
for root, directories, files in os.walk(mount_loc):
    for f in files:
        file_path = str(os.path.join(root, f))
        file_size = os.path.getsize(file_path)
        file_value_array.append({file_path.replace('\\','/'): file_size})

file_dict.update({"files": file_value_array})

file_size_json = json.dumps(file_dict,indent = 4)

print(file_size_json)

with open('data.json', 'w') as outfile:
    outfile.write(file_size_json)

print('Data saved to data.json in script directory.')
