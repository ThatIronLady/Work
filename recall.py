import random

class column:
  def __init__(self,order,line):
    self.__order=order
    self.line=line

def main():
  arr=[]
  plaintext=input("Enter message to be encrypted: ")
  size=input("Enter encryption factor: ")
  b=True
  newarr=[]
  rando_store=[]
  while b!=True:
    a=plaintext[:size]
    plaintext=plaintext[size:]
    rando_check=False
    rando=random.randint(1,size)
    while rando in rando_store:
        rando=random.randint(1,size)
    rando_store.append(rando)
    for i in range(len(a):
      newerarr.append(a[:i:])
    newarr.append(column(rando,newerarr))
    if plaintext=='':
      b=False
  for i in range(len(newarr)):
    for j in range(len(i.line)):
      print(i.line[j])

    
    
    
