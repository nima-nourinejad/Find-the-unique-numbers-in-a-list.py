def dr (a):
  out=[]
  for i in a:
    if i in out:
      pass
    else:
      out.append(i)
  print (out)
  return len (out)
