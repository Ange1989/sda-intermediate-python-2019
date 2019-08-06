"""
. - dowolny znak, który może się tu pojawić np. a lub n
.+ - jeden lub więcej znaków, które mogą sie tu pojawić
.* -zerow bądź wiele znaków, które mogą sie tu pojawić
.\ - matches a character .
\d - matches a digit (equal to[0-9],
\D - wszystkie znakie które nie są białe
\s - spacja
\S - inne znaki niź spacja
\n - przerwa pomiędzy linijkami
\w - oznacza każdy znak alfanumeryczny
\W - wszystkie inne znaki nie alfanumeryczne
^ - początek tekstu
$ - koniec tekstu
() - oznacza grupę, wszystko co jest w środku grupy zostanie zgrupowany i wyciągnięty jako dowolna grupa
(?: ) wyszukuje konkretne grupy
[] - zbiory znaków, które chcemy wziąść pod uwagę, również przedział [A-Z] [a-z]
{} - ilość wystąpień A{1 , 3} przedział od 1 do 3
\d{2} matches two digits (equal to[0-9]
"""

import re

if __name__ == '__main__':
    text1 = 'Ala ma kota'
    reg1 = r'[AU]la\sma\s(.+)'  # r-raw text
    print(r'\n')
    print('\n')
    match1 = re.search(reg1, text1)
    print(match1.groups())
    print(match1.span())

    print('*' * 20)

    text2 = 'Mój numer telfonu to 123456789'
    reg2 = r'.*(\d{9}).*'
    match2 = re.match(reg2, text2)
    if match2:
        print(match2.group(1))

    print('*' * 20)

    text3 = 'Mój numer telfonu to 123456789 lub 987654321'
    reg3 = r'\d{9}'
    match3 = re.findall(reg3, text3)
    print(match3)

    print('*' * 20)

    text4 = 'Ula ma kota i ma psa'
    reg4 = r'\sma\s'
    sub1 = re.sub(reg4, ' nie ma ', text4)
    print(sub1)
    reg5 = r'ma kota'
    sub2 = re.sub(reg5, 'nie ma kota', text4)
    print(sub2)

    print('*' * 20)

    text5 = 'Tomek, Radek, Krzysiek'
    print(text5.split(', '))
    reg6 = r'\W{2}'
    print(re.split(reg6, text5))

    print('*' * 20)

    text6 = 'TomekRadekKrzysiek'
    reg7 = r'(?=[A-Z])'
    print(re.split(reg7, text6))