
def parse(result, *args):
  srcs = result.split(":")
  if len(srcs) < 3:
    pass
  else:
    path = srcs.pop(0)
    number = srcs.pop(0)
    row = ':'.join(srcs)
    return {'path': path, 'number': number, 'row': row}
