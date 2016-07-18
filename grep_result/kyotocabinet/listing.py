from kyotocabinet import *

def select(*args):
  listings = []
  db = DB()
  file_name = args[0]
  if not db.open(file_name, DB.OWRITER | DB.OCREATE):
    print("open error: " + str(db.error()))
  else:
    cur = db.cursor()
    cur.jump()
    while True:
      rec = cur.get(True)
      if not rec: break
      listings.append(rec)
    cur.disable()
  if not db.close():
    print("close error: " + str(db.error()))
  return listings

def count(*args):
  listings = []
  db = DB()
  file_name = args[0]
  if not db.open(file_name, DB.OWRITER | DB.OCREATE):
    print("open error: " + str(db.error()))
  else:
    listings.append(["count",str(db.count())])
  if not db.close():
    print("close error: " + str(db.error()))
  return listings
