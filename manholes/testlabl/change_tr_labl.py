#This is a program written to edit the first value of the image's labels file by making it 0

#modules import

import os

# EXTRACTING THE SIZE OF THE FOLDER
dir_path = r'/Users/anirudhchilukuri/Downloads/manholes/testlabl'
count = sum(1 for path in os.scandir(dir_path) if path.is_file())
print('file count:', count)

# EXTRACTING THE NAME OF THE FILES
dir_list = os.listdir(dir_path)
print("Files and directories in '", dir_path, "' :")
print(dir_list)

# CHANGING FILE PATH
def edit_last_file_path(path, new_file_name):
    head, tail = os.path.split(path)
    print(f"Original directory: {head}")
    print(f"Original file name: {tail}")
    new_path = os.path.join(head, new_file_name)
    print(f"New path: {new_path}")
    return new_path

original_path = "/Users/anirudhchilukuri/Downloads/manholes/testlabl/well0_0002_jpg.rf.5fd6d3c4feff1b8c10256a74f726e3b8.txt"
new_file_name = dir_list[0] if dir_list else ""
new_path = edit_last_file_path(original_path, new_file_name)

# MODIFYING THE FIRST VALUE OF THE FILES
def edit_first_value(file_path, new_value):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        if lines:
            first_line = lines[0].split()
            if first_line:
                first_line[0] = new_value  # Set the first element to the new value
                lines[0] = ' '.join(first_line) + '\n'  # Reconstruct the first line

        with open(file_path, 'w') as file:
            file.writelines(lines)
        
        print(f"Modified file: {file_path}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# ITERATE OVER EACH FILE AND MODIFY THE FIRST VALUE
for file_name in dir_list:
    file_path = os.path.join(dir_path, file_name)
    edit_first_value(file_path, "0")


# def edit_element_in_file(file_path,  new_element, old_element=(0,1,2,3)):
#     with open(file_path, 'r') as file:
#         lines = file.readlines()

#     modified_lines = []
#     for line in lines:
#         for old_element in old_element:
#             line = line.replace(str(old_element), new_element)
#         modified_lines.append(line)
#     print(modified_lines)
#     with open(file_path, 'w') as file:
#         file.writelines(modified_lines)
    

# file_path = new_path 
# new_element = '0'
# iterate_words(file_path)

# for j in range(0, count):
#     my_file = open(new_path,"w")
#     for i in my_file:
#         print(i[j])
#     print(my_file,'......')
