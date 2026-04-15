from contextlib import contextmanager

with open("C:\\Users\\MerajHussainSyed\\ctest.txt",'a') as file:
    file.write("test")

@contextmanager
def my_file_open(filename, mode='a'):
    try:
        with open(filename, mode) as file:
            print("File opened")
            yield file
    except Exception:
        print("Error opening file")
    finally:
        print("File closed")
        file.close()


with my_file_open("C:\\testcontextmanager.txt",'a') as file:
    file.write("\ntest context manager\n")


class File_Opener:
    def __init__(self, filename,mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("__Enter__")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("Error occured while closing")

        if self.file:
            self.file.close()
            print("File closed")

with File_Opener("C:\\testcontextmanagetolstyle.txt",'a') as file:
    file.write("\ntest old context manager\n")