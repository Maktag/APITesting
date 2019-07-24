import pandas as pd


class ReadCSV:

    def __init__(self, filename, baseurl):
        self.filename = filename
        self.baseURL = baseurl

    def file_obj(self):
        data = pd.read_csv(self.filename)
        return data

    def get_columns_len(self):
        return len(self.file_obj().columns)

    def get_rows_len(self):
        return self.file_obj().__len__()