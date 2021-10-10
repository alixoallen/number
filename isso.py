c=0
soma=0
while True:
  b=int(input('digite um valor (999 para parar):'))
  if  b == 999:
    print(f'a soma dos {c} valores foi {soma} ')
    break
  c+=1
  soma+=b