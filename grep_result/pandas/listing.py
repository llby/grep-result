import pandas
import numpy

def select(*args):
  file_path = args[0]
  return pandas.DataFrame.from_csv(file_path)
