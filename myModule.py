#File name myModule.py
letters = [ ["A",0],
            ["B",0],
            ["C",0],
            ["D",0],
            ["E",0],
            ["F",0],
            ["G",0],
            ["H",0],
            ["I",0],
            ["J",0],
            ["K",0],
            ["L",0],
            ["M",0],
            ["N",0],
            ["O",0],
            ["P",0],
            ["Q",0],
            ["R",0],
            ["S",0],
            ["T",0],
            ["U",0],
            ["V",0],
            ["W",0],
            ["X",0],
            ["Y",0],
            ["Z",0],
            ]


def testFunction(a,b):
    print a*str(b)

def countLetters(inStr):
    global letters
## si no se usan las funciones range y len para letters, entoces
## letter_index se hace una lista, con las funciones se puede usar para hacer
## indexacion del array

#changing the input string a upper case
    inStr =  inStr.upper()
##    inStr.upper(this)
#    print inStr
    for letter_index in range(len(letters)):
#adding the letters per each line
        letters[letter_index][1] += inStr.count(letters[letter_index][0])

def getResults():
    global letters
   # print letters[letter_index][0] + " : " + str(letters[letter_index][1])
    print letters
    return letters

def countLettersFile(inFile):
    global letters

    freq = [] # create empty list
    for line in inFile:
        countLetters(line)
    # get the output array to translate it to a list
    temp_arr =  getResults()

    for element in range(len(letters)):
        freq.append(letters[element][1])
    return freq

