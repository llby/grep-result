import os
import grep-result
import grep-result.grep as grep


def print_all(record):
  print record


home = os.path.abspath(os.path.dirname(__file__))
path = os.path.abspath(os.path.dirname(__file__))
keyword = "def \\w"

grep-result.init(home)

grep-result.listing(grep.grep, path, keyword)
grep-result.parse(grep.parse)
grep-result.output(print_all)

grep-result.listing(grep.git_grep, path, keyword)
grep-result.parse(grep.parse)
grep-result.output(print_all)
