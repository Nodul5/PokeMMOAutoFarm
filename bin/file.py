class File:
    def __init__(self, name):
        self.name = name

    def overwrite(self, text):
        with open(self.name, "w") as file:
            file.write(text)

    def write(self, text):
        with open(self.name, "a") as file:
            file.write(text)

    def read(self):
        with open(self.name,"r") as file:
            return file.readlines()