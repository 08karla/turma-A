while True:
  print("qual calculadora vamos usar?")
  calculadora = int(input("[1] física  [2] matemática\n"))

  if calculadora == 1:
    newton = int(input("vamos calcular qual formula?n\[1] 2º lei de newton [2]nenhuma\n"))
   
  if newton == 1:
   print("****************************************")
   print("* calculadora da Segunda lei de Newton *")  
   print("***************** ********************\n")
   massa = int(input("qual é a massa do corpo? ")) 
   aceleracao = int(input("\nqual é a aceleração? "))
   print("\nA força é equivalente a", massa * aceleracao, "Newtons\n\n")

   continua = int(input("vamos continuar? [1] sim [2] não"))
if continua == 1:          
  continue
if continua == 2:
   break
