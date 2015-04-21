#!/usr/bin/python -tt
##filename countletters.py
import myModule
import matplotlib.pyplot as plt
## Java was written in such way that making bad code were difficult, python
## is written in a way that makes writting good code easy

####################################################
def raw_VS_input():
    #differencia entre raw_input y input
    #dar como para metro de entrada range(0,10,1)
    print "it works"
    inStr = raw_input("raw text: ");
    print inStr
    inStr = input("exec text: ");
    print inStr

####################################################
def fileOp():
    textFile = open("testText.txt", "r+") # open the file in read and write, the FP is at the end
    print type(textFile)
    
    #check the status of the file object
    if(textFile.closed == True):
        print "El archivo esta cerrado"
    else:
        print "el archivo esta abierto"

    print "imprime el modo en que se abrio el archivo"
    print textFile.mode

    print "imprime el nombre del archivo"
    print textFile.name
    
    # REMEMBER TO ALWAYS CLOSE THE FILE EXPLICITLITY IF POSSIBLE
    textFile.close()
####################################################
def readLines():
    #textFile = open("testText.txt", "r+") # open the file in read and write, the FP is at the end
    textFile = open("DerTorUndDerTod.txt", "r+") # open the file in read and write, the FP is at the end
    lineCount = 0
    #for lines in textFile.linecount():
    for lines in textFile:
        lineCount += 1
        print lines, #the comma at the end avoids the new line
    #also
        print lines.strip('\n'), #the comma at the end avoids the new line
    print type(lines)
    textFile.close()
    return lineCount

####################################################
if __name__ == "__main__":
    #raw_VS_input()
    #fileOp()
   # lineCount = readLines()
   # print "Line count: " + str(lineCount)
    myModule.testFunction(4,4)
    ## this function receives a file object
    textFile = open("DerTorUndDerTod.txt", "r+") # open the file in read and write, the FP is at the end
    #plot.hist( myModule.countLettersFile(textFile))

    data = myModule.countLettersFile(textFile)
    type(data)
    plt.plot(data)
    plt.show()
    textFile.close()


