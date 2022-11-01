# this script renames each image with a unique id in each folder in the current directory

import os

image_folders = ['./' + folder_name + '/' for folder_name in next(os.walk('.'))[1]
                 if folder_name not in ['venv', '.idea']]

print(image_folders)

def unify_names():
    for fol_name in image_folders:
        counter = 0
        for img_file_name in os.listdir(fol_name):
            old_name = os.path.abspath(fol_name + img_file_name)
            new_name = os.path.abspath(fol_name + str(counter) + '.jpg')
            os.rename(old_name, new_name)
            counter += 1


jpg_count = {}

for fol_name in image_folders:
    jpg_count[fol_name] = len([name for name in os.listdir(fol_name) if name.endswith(".jpg")])

print(jpg_count)



