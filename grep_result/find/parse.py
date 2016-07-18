import commands

def row_count(record, *args):
  file_name = record
  path = args[0]
  res = commands.getoutput("cd %s;wc -l %s"%(path, file_name)).split(" ")
  count = int(res[-2]) - 1
  return {'file': file_name, 'count': count}
