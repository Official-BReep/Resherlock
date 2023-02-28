import os

class FileWriter:
    def __init__(self,settings, output):
        self.settings = settings
        self.output = output

    def handle_namelist(self):
        pass

    def write_txt(self, filename):
        if os.path.exists(filename):
            os.remove(filename)
        with open(filename, "a+") as output_file:
            for line in self.output:
                output_file.write(line + "\n")