import os

listings = []
home = ""

def init(path):
  global listings
  global home
  listings = []
  home = path

def listing(fun, *args):
  global listings
  listings = fun(*args)
  os.system("cd %s"%(home))
  return listings

def parse(fun, *args):
  global listings
  tmps = listings
  listings = []
  for result in tmps:
    res = fun(result, *args)
    if not res: continue
    listings.append(res)
  return listings

def output(fun, *args):
  global listings
  listings = fun(listings, *args)
  os.system("cd %s"%(home))
  return listings  

