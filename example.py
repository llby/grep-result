import os
import grep_result
import grep_result.grep as gr_grep
import grep_result.pandas as gr_pandas

def print_all(record):
  print record


home = os.path.abspath(os.path.dirname(__file__))
path = os.path.abspath(os.path.dirname(__file__))
keyword = "def \\w"

grep_result.init(home)

grep_result.listing(gr_grep.grep, path, keyword)
grep_result.parse(gr_grep.parse)
grep_result.output(print_all)

grep_result.listing(gr_grep.git_grep, path, keyword)
grep_result.parse(gr_grep.parse)
grep_result.output(gr_pandas.export_csv, "result.csv")

grep_result.listing(gr_pandas.select, "result.csv", "")
grep_result.output(gr_pandas.count_by_2path)
