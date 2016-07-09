import os
import grep_result

def grep(*args):
  import commands
  path = args[0]
  key_word = args[1]
  return commands.getoutput("grep -rn '%s' %s"%(key_word, path)).split("\n")

def parse_grep(result, *args):
  srcs = result.split(":")
  if len(srcs) < 3:
    pass
  else:
    path = srcs.pop(0)
    number = srcs.pop(0)
    row = ':'.join(srcs)
    return {'path': path, 'number': number, 'row': row}

def print_all(record):
  print record


home = os.path.abspath(os.path.dirname(__file__))
path = os.path.abspath(os.path.dirname(__file__))
keyword = "def \\w"

grep_result.init(home)

grep_result.listing(grep, path, keyword)
grep_result.parse(parse_grep)
grep_result.output(print_all)

