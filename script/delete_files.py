import os

def delete_files():
    i = 0
    path = "../path_example_files/"

    for filename in os.listdir(path):

        file = path + filename
        os.remove(file)

        i += 1


if __name__ == "__main__":
    delete_files()