import commands

def grep(*args):
  path = args[0]
  key_word = args[1]
  return commands.getoutput("grep -rn '%s' %s"%(key_word, path)).split("\n")

def git_grep(*args):
  path = args[0]
  key_word = args[1]
  return commands.getoutput("cd %s;git grep -n '%s'"%(path, key_word)).split("\n")
