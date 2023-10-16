#Izdrukat visus skaitlus no 15-89, kuri dalās ar 5, 3 un 2

for skaitlis in range(15, 89):
    if skaitlis % 2  == 0 and skaitlis % 3 == 0 and skaitlis % 5 == 0:
        print(skaitlis)

