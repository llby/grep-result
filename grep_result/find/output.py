import pandas
import numpy
import os

def export_csv(datas, *args):
  df = pandas.DataFrame()
  name = args[0]
  os.system("rm %s"%(name))
  for data in datas:
    row = pandas.DataFrame([
      [data['file'],
       data['count']]],
       columns=('file', 'count'))
    df = df.append(row, ignore_index=True)
  df.to_csv(name)
