numerals = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero"
}


phones = input("Phone : ")    

output = ""
for phone in phones:
    output = output + numerals.get(phone,"!") + " "
print(output)
