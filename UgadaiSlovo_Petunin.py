#Загадали слово
#У пользователя есть попытки  для угадывания (количество попыток определите сами, сообщите об этом пользователю) 
#Пользователь вводит букву, вы сообщаете есть ли эта буква в слове или нет
#Если количество успешных попыток равно длине слова, то игра прекращается победой, и вы предлагаете пользователю ввести слово, или показываете ему слово, если он ввёл неправильное слово
#Если у пользователя закончились попытки, то поражение
#Дополнительно можно контролировать, если пользователь вводил уже такую букву, то не считать её успешной попыткой, а сообщить пользователю, что он теряет попытки,
#также если в слове  2 или более одинаковых  букв, то при успешной попытке тоже можно сообщить об этом пользователю secret_Word = input("Вводим слово: \r").lower()   # работаю в нижнем регистре






secret_Word = input("Вводим слово: ").upper()   

tries = len(secret_Word) 

disp_Secret_Word = "?" * len(secret_Word)
guess = ""

kolPrav = 0

print("Угадываем слово.")
print("Количество попыток: ", tries)

for i in range(1, tries + 1):
    print(disp_Secret_Word)
    bukva = input("Попытка "+ str(i) +": введите букву - ").upper()    

    if disp_Secret_Word.find(bukva) != -1 or guess.find(bukva) != -1:
        print("Эту букву Вы уже вводили. Вы потеряли попытку.")
    else:
        tries = secret_Word.count(bukva)
        if tries == 0:
            print("Буквы " + bukva + " нет в угадываемом слове")
            guess = guess + bukva + " "
        else:
            print("Вы угадали букву!")
            if tries > 1:
                print("Количество повторов угаданной буквы в слове:", tries)
            kolPrav += 1
            for j in range(0,len(secret_Word)):
                if secret_Word[j] == bukva:
                    disp_Secret_Word = disp_Secret_Word[:j] + bukva + disp_Secret_Word[j+1:]
                if disp_Secret_Word.find("?") == -1:
                    break
if disp_Secret_Word.find("?") == -1:
    print("Поздравляю, Вы угадали слово :", disp_Secret_Word)
else:
    print()
    print(disp_Secret_Word)
    if kolPrav > 1:
        print("Количество угаданных Вами букв в слове:", kolPrav)
    else:
        print("Вы не угадали ни одной буквы.")
    if len(guess) > 0:
        print("Буквы, которых нет в слове: ", guess)
    guess = input("У Вас есть последняя попытка угадать слово: ")
    if guess == secret_Word:
        print("Поздравляю, Вы угадали слово!")
    else:
        print("Вы не угадали слово. Загаданное слово было: ", )