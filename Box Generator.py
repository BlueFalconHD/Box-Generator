confirminput = " "
askedtext = True
textlength = 0
lengthnew = 0
lengthnewhalf = 0
halfspaceamt = "placeholder"
boxl1 = "placeholder"
boxl2 = "placeholder"
boxl3 = "placeholder"
boxfull = "placeholder"
class wall:
        topleft = "╭"
        topright = "╮"
        bottomleft = "╰"
        bottomright = "╯"
        wallhorizontal = "─"
        wallvertical = "│"


# Boxdraw
def drawbox(length, text):
    global lengthnew, lengthnewhalf, halfspaceamt, boxl1, boxl2, boxl3, wall, boxfull
    boxl1 = [wall.topleft]
    boxl2 = [wall.wallvertical]
    boxl3 = [wall.bottomleft]
    lengthnew = length + 2

    #halflength
    lengthnewhalf = lengthnew / 2
    halfspaceamt = []
    for i in range(int(lengthnewhalf)):
        halfspaceamt.append(" ")

    #Line 1

    for i in range(lengthnew + length):
        boxl1.append(wall.wallhorizontal)
    boxl1.append(wall.topright)

    #Line 2



    boxl2.append(''.join(halfspaceamt))
    boxl2.append(text)
    if (length % 2) == 0:
        boxl2.append(''.join(halfspaceamt))
    else:
        halfspaceamt.append(" ")
        boxl2.append(''.join(halfspaceamt))
    boxl2.append(wall.wallvertical)

    #Line 3

    for i in range(lengthnew + length):
        boxl3.append(wall.wallhorizontal)
    boxl3.append(wall.bottomright)

    #Compile

    lengthnew =+ 1
    print(''.join(boxl1) + "\n" + ''.join(boxl2) + "\n" + ''.join(boxl3))
    boxfull = ''.join(boxl1) + "\n" + ''.join(boxl2) + "\n" + ''.join(boxl3)
    


            
        
    
    





#####################
#    SUBPROGRAMS    #
#####################

def asktext():
    global askedtext
    askedtext = input("What would you want your text to be? > ")
    confirm()
def textconfirmed():
    global textlength, askedtext
    # textlength + 4 (2 spaces on either side of text before border.)
    textlength = len(askedtext)
    print("Length:" + str(textlength))
    drawbox(textlength, askedtext)
def confirm():
    global askedtext, confirminput
    # 'Are you sure you want your text to be "' + askedtext + '"? (y/n) > '
    confirminput = input('Are you sure you want your text to be "' + askedtext + '"? (y/n) > ')
    if confirminput == "Y" or confirminput == "y":
        print("Confirmed!")
        textconfirmed()
    elif confirminput == "N" or confirminput == "n":
        asktext()
    else:
        print("ERROR - Expected : [Y,y,N,n]")
        print("Restart program please. If the error persists, email me! hjdombro@icloud.com - Hayes D.")
#####################




asktext()
confirm()
input("Thanks for using box generator! - Hayes D.")
    
