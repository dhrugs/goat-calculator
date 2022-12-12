type_calcul = input("Quel type de calcul voulez-vous faire ? (Addition, Multiplication, Division) : ")

if type_calcul == str('Addition'):
    addition_a = input("Entrez votre premier nombre : ")
    addition_b = input("Entrez votre deuxième nombre : ")
    print(f"Résultat : {int(addition_a)+int(addition_b)}")
    
if type_calcul == str("Multiplication"):
        multiplication_a = input('Entrez votre premier nombre : ')
        multiplication_b = input('Entrez votre deuxième nombre : ')
        print(f"Le résultat de votre multiplication : {int(multiplication_a) * int(multiplication_b)}")
        
if type_calcul == str("Division"):
        division_a = input('Entrez votre premier nombre : ')
        division_b = input('Entrez votre deuxième nombre : ')
        print(f"Le résultat de votre division : {float(division_a) / float(division_b)}")
    





# a = input("Entrez un nombre : ")
# b = input("Entrez un nombre : ")
# print(f'Le résultat de votre addition est {int(a) + int(b)}'