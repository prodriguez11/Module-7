
def uniqueList(li):
  uniquelist = []
  for i in li:
    if i not in uniquelist:
      uniquelist.append(i)
  return uniquelist

print(uniqueList([1, 3, 3, 3, 6, 2, 3, 5]))
