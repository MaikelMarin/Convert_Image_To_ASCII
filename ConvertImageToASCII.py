#============================================================================
# Name        : ConvertImageToASCII.py
# Author      : Maikel Marín Brenes
# Version     : 1.0
# License     : This script is openSource.
# Description : Script for convert image to ASCII.
#============================================================================
    #####                #####                 ####               ###         ###              ####     ##################       ###
    ######               #####                #####               ###         ###             ####      ##################       ###
    ######              ######                #####               ###         ###            ####       ##################       ###
    ### ###             ## ###                ######              ###         ###           ####        ###                      ###
    ###  ##            ### ###               ### ###              ###         ###          ###          ###                      ###
    ###  ##            ##  ###               ###  ###             ###         ###         ###           ###                      ###
    ###  ###           ##  ###              ###   ###             ###         ###        ###            ###                      ###
    ###   ##          ###  ###              ###    ##             ###         ###       ###             ###                      ###
    ###   ###         ##   ###              ##     ###            ###         ###      ###              ###                      ###
    ###    ##         ##   ###             ###     ###            ###         ###     ###               ###                      ###
    ###    ##        ###   ###             ###      ##            ###         ###   ####                ###                      ###
    ###    ###       ##    ###             ##       ###           ###         ###  ####                 ###                      ###
    ###     ##      ###    ###            ###       ###           ###         ########                  #################        ###
    ###     ##      ##     ###            ###        ###          ###         #######                   #################        ###
    ###      ##     ##     ###           ###         ###          ###         ########                  #################        ###
    ###      ##    ###     ###           ###          ##          ###         ###  ####                 ###                      ###
    ###      ###   ##      ###           ##           ###         ###         ###   ####                ###                      ###
    ###       ##  ###      ###          ###           ###         ###         ###    ####               ###                      ###
    ###       ##  ##       ###          #################         ###         ###     ####              ###                      ###
    ###       ### ##       ###         ###################        ###         ###      ####             ###                      ###
    ###        #####       ###         ###################        ###         ###       ####            ###                      ###
    ###        ####        ###         ##               ###       ###         ###        ####           ###                      ###
    ###         ###        ###        ###               ###       ###         ###         ####          ###                      ###
    ###                    ###        ###                ##       ###         ###          ####         ###                      ###
    ###                    ###        ##                 ###      ###         ###           ####        ###                      ###
    ###                    ###       ###                 ###      ###         ###            ####       ###                      ###
    ###                    ###       ###                  ###     ###         ###             ####      ##################       ##################
    ###                    ###      ###                   ###     ###         ###              ####     ##################       ##################
    ###                    ###      ###                   ###     ###         ###               ####    ##################       ##################


from PIL import Image

FAIL = '\033[91m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'

def readImage(pathImage):
    if pathFile != "":
        try:
            read_image = Image.open(pathImage)
            data = [list(read_image.getdata()) , read_image.size]
            read_image.close()
            print(OKGREEN , "GET DATA IMAGE READY")
            return data
        except IOError:
            print(FAIL, "\nNOT OPEN IMAGE")
            return 0
    else:
        println(FAIL,"ERROR PATH IMAGE")
        return 0


def createFile(path):
    if path != "":
        try:
            create_file = open(path, "w")
            print(OKGREEN, "\nCreate file succesfull.")
            return create_file
        except IOError:
            print(FAIL, "\nERROR TO CREATE FILE")
            return 0
    else:
        println(FAIL,"ERROR PATH")
        return 0


#  The color of the data that passes to ASCCI has to be black
def generateDataASCII(_file, dataImage, sizeImage):

    JumpLineCounter = 0
    colorLetters = (0,0,0) , (10,10,10)

    for colorPromter in dataImage:
        if colorPromter >= colorLetters[0] and colorPromter <= colorLetters[1]:
            _file.write("#")
        else:
            _file.write(" ")

        JumpLineCounter = JumpLineCounter + 1
        if JumpLineCounter == sizeImage[0]:
            _file.write("\n")
            JumpLineCounter = 0

    print(OKGREEN, "\nGenerate image to ASCII.")
    print(OKGREEN, "\nEXIT")

    _file.close()


if __name__ == '__main__':

    exitScript = 'n'
    print(OKBLUE, "The color of the letters have be: RGB(0,0,0)\n")

    while exitScript == 'n'or exitScript == 'N':
        pathImage = input("What is path to image: ")
        pathFile = input("What is path for save file: ")

        dataImage = readImage(pathImage)
        file = createFile(pathFile)

        if dataImage != 0 and file != 0 :
            generateDataASCII(file, dataImage[0] , dataImage[1])
            exitScript = input("Exit program ? n = repet and s = exit: ")
        else:
            exitScript = 's'
            print(FAIL, "\nEXIT ERROR")
