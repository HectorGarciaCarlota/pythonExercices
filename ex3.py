import os

def get_valid_path():
    while True:
        user_input = input("Enter the path you want to use to change the name of the file: ")
        if os.path.exists(user_input) and os.path.isdir(user_input):
            return user_input
        else:
            print("Invalid path. Please try again.")

def get_valid_name(path):
    while True:
        user_input = input("Enter the filename of the file to change: ")
        full_path = os.path.join(path, user_input)
        if os.path.exists(full_path) and os.path.isfile(full_path):
            return full_path
        else:
            print("Invalid filename. Please try again.")

def rename_files():
    path = get_valid_path()
    filename = get_valid_name(path)
    _, file_extension = os.path.splitext(filename)
    new_filename = input("Please enter the new filename: ")
    new_file_path = os.path.join(path, new_filename + file_extension)

    try:
        os.rename(filename, new_file_path)
        print(f"File renamed to {new_file_path}")
    except OSError as e:
        print(f"Error: {e}")

def ex3():
    rename_files()

if __name__ == "__main__":
    ex3()