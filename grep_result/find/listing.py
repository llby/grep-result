import commands

def find(*args):
  path = args[0]
  return commands.getoutput("cd %s;find . -name '*.txt' -print"%(path)).split("\n")

