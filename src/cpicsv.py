import sys

def start(fname):
  data = []
  state = "initial"
  with open(fname) as inf:
    for line in inf:
      if state == "initial":
        if line.strip().startswith("Year"):
          headers = line.strip().split()
          headers[-2] = "Percent change Dec-Dec"
          headers[-1] = "Percent change Avg-Avg"
          data.append(headers)
          state = "body"
      elif state == "body":
        if line.strip(): # non-empty lines
          data.append(line.strip().split())
  for row in data:
    print ",".join(row)

if __name__ == '__main__':
  start(*sys.argv[1:])
