from kyotocabinet import *

def insert(datas, *args):
  db = DB()
  file_name = args[0]
  if not db.open(file_name, DB.OWRITER | DB.OCREATE):
    print("open error: " + str(db.error()))
  else:
    for data in datas:
      key = data['path'] + ':' + data['number']
      val = data['row']
      if not db.set(key, val):
        print("set error: " + str(db.error()))
  if not db.close():
    print("close error: " + str(db.error()))
