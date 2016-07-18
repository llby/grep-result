import pandas
import numpy
import os

def export_csv(listings, *args):
  file_path = args[0]
  os.system("rm %s"%(file_path))
  df = pandas.DataFrame()
  for data in listings:
    row = pandas.DataFrame([
      [data['path'],
       data['number'],
       data['row'],
       1]],
       columns=('path','number', 'row', 'count'))
    df = df.append(row, ignore_index=True)
  df.to_csv(file_path)

def export_html(listings, *args):
  df = pandas.DataFrame(listings)
  return df[['path','number','row']].to_html()

def count_by_path(listings):
  return pandas.pivot_table(
    listings,
    index       = "path",
    values      = "count",
    aggfunc = numpy.sum,
    fill_value = 0,
    margins    = True,
  )

def count_by_path_initial(listings):
  return listings.groupby(listings['path'].str[0:3]).apply(lambda x: x['count'].sum())

def count_by_2path(listings):
  df = listings.groupby(listings['path'].str.extract('(\w+/\w+)')).apply(lambda x: x['count'].sum())
  return pandas.DataFrame(df, columns=['count'])
  
