class GetData:

    def choose_file(self):
        from tkinter import filedialog, Tk
        Tk().withdraw()
        chosen_file = filedialog.askopenfilename()
        return chosen_file

    def skip_line(file_being_analyzed):
        return file_being_analyzed.readline()

    def data_in_file(file_being_analyzed):
        import csv
        return csv.reader(file_being_analyzed)

