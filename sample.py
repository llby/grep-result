import os
import grep_result
import grep_result.grep as grep


def print_all(record):
  print record


home = os.path.abspath(os.path.dirname(__file__))
path = os.path.abspath(os.path.dirname(__file__))
keyword = "def \\w"

grep_result.init(home)

grep_result.listing(grep.grep, path, keyword)
grep_result.parse(grep.parse)
grep_result.output(print_all)

grep_result.listing(grep.git_grep, path, keyword)
grep_result.parse(grep.parse)
grep_result.output(print_all)
