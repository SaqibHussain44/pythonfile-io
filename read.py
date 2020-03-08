f = open("test1.txt", "r")
if f.mode == 'r':
  contents = f.read()
  print (contents)

f.close()
