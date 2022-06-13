import os

def renaming_files():
    i = 0
    path = "../path_example_files/"

    for filename in os.listdir(path):

        new_name_file = "img" + str(i+1) + ".jpg"
        old_name = path + filename
        new_name_file = path + new_name_file
        os.rename(old_name, new_name_file)
        #os.remove(old_name)

        i += 1


if __name__ == "__main__":
    renaming_files()