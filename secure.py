# =============================== #
# +++++++++++++++++++++++++++++++ #
# password manager ++++++++++++++ #
# dex4tw is very cool +++++++++++ #
# +++++++++++++++++++++++++++++++ #
# =============================== #

# [ Libraries ] - these r important ]
import os
import time
import sys

# [ On Start ] - things 2do on startup ]
deviceos = ""
if sys.platform == 'win32':
    deviceos = "Windows"
elif sys.platform == "darwin":
    deviceos = "MacOS"
elif sys.platform == "linux" or sys.platform == "linux2":
    deviceos = "Linux"

if deviceos == "Windows":
    os.system("title VexManager: Windows settings loaded")
else:
    pass

if not os.path.exists("C:/temp/Vex"):    
    os.mkdir("C:/temp/Vex")

if not os.path.exists("C:/temp/Vex/Key.dex"):
    writekey = open("C:/temp/Vex/Key.dex", "w")
    newkey = input("Master Key: ")
    writekey.write(newkey)
    writekey.close()

IIIIllllI = open("C:/temp/Vex/Key.dex", "r")
dex = IIIIllllI.read()

# [ Variables ] - variables and stuff ]
def clear():
    if deviceos == "Windows":
        os.system("cls")
    elif deviceos == "MacOS":
        os.system("clear")
    elif deviceos == "Linux":
        os.system("clear")
    else:
        print("OS unrecognized, trying to clear screen.")
        try:
            os.system("cls")
            os.system("clear")
        except:
            print("Attempts failed.")

IlllllIIIIIl = print
IllIllllllI = ":"
IlllIllllIIIIl = "w"
IlllIllllIIIII = "r"
IlllIIIll = open
idk = "idk"

# [ Password Manager ] - self explanatory ]
clear()

print("""Options:
[0]: requestpass - request a password you created
[1]: createpass - create urself a password
""")

try:
    if not os.path.exists("C:/temp/Security"):
        os.mkdir("C:/temp/Security")
    if not os.path.exists("config"):
        os.mkdir("config")
except:
    print("Sorry, the program does not have permission to create directories.")
    time.sleep(5)

option = input(f"{os.getlogin()}%> ")

def requestpass():
    clear()

    IlIIIIIIlll = input("Master Key: ")
    lIIlIlllIllIIll = input("File Name: ")

    try:
        """IlIllIllIIIllIIIlIIIIlIlllIIlI""";is_this_secure = idk;"""llIllllI""";bruhh = "digfjdiof";"""IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI"""
        if IlIIIIIIlll == dex:
            """IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI""";"""IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI"""
            """IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI""";hello=True;"""IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI"""
            """IlIllIllIIIllIIIlIII""";lol=True;"""IlIlllIIlIllIllllI""";"""IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI"""
            """IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI""";"""IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI""";"""llII""";IIIlllIllIIIlllll="C:/temp/Security/";"""IllIIIlIIIIlIlllIIlIllIllllI"""
            """IlIllIllIIIllIIIlIIIIlIlllII""";lI=IlllIIIll(IIIlllIllIIIlllll+lIIlIlllIllIIll, IlllIllllIIIII);"""lIllIllllI""";"""llIIIllIIIlIIIIlIlllIIlIllIllllI"""
            """IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI""";ll=lI.read();"""llIIIllIIIlIIIIlIlllIIlIllIllllI"""
            """IlIllI""";IlllllIIIIIl(ll);lI.close();"""llIIIllIIIlIIIIlIll""";"""lIIlIllIllllI""";"""llIIIllIIIlIIIIlIlllIIlIllIllllI"""
            
    except:
        """IlIllIllIIIllIIIlIIIIlIlllIIlI""";is_this_secure = idk;"""llIllllI""";bruhh = "digfjdiof";"""IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI"""
        if IlIIIIIIlll == dex:
            """IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI""";"""IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI"""
            """IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI""";hello=True;"""IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI"""
            """IlIllIllIIIllIIIlIII""";lol=True;"""IlIlllIIlIllIllllI""";"""IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI"""
            """IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI""";"""IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI""";"""llII""";IIIlllIllIIIlllll="C:/temp/Security/";"""IllIIIlIIIIlIlllIIlIllIllllI"""
            """IlIllIllIIIllIIIlIIIIlIlllII""";lI=IlllIIIll(IIIlllIllIIIlllll+lIIlIlllIllIIll+'.dex', IlllIllllIIIII);"""lIllIllllI""";"""llIIIllIIIlIIIIlIlllIIlIllIllllI"""
            """IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI""";ll=lI.read();"""llIIIllIIIlIIIIlIlllIIlIllIllllI"""
            """IlIllI""";IlllllIIIIIl(ll);lI.close();"""llIIIllIIIlIIIIlIll""";"""lIIlIllIllllI""";"""llIIIllIIIlIIIIlIlllIIlIllIllllI"""
            

def createpass():
    clear()
    print("""Password Creation Process

    """)
    lIIlIlllIllIIll = input("File Name: ")
    llIlIlllIllIIll = input("Username (Optional): ")
    lIIlllllIllIIll = input("Password: ")

    """IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI""";"""IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI""";"""llII""";IIIlllIllIIIlllll="C:/temp/Security/";"""IllIIIlIIIIlIlllIIlIllIllllI"""
    """IlIllIllIIIllIIIlIIIIlIlllII""";lI=IlllIIIll(IIIlllIllIIIlllll+lIIlIlllIllIIll+'.dex', IlllIllllIIIIl);"""lIllIllllI""";"""llIIIllIIIlIIIIlIlllIIlIllIllllI"""
    """IlIllIllIIIllIIIlIIIIlIlllIIlIllIllllI""";lI.write(llIlIlllIllIIll+IllIllllllI+lIIlllllIllIIll);"""llIIIllIIIlIIIIlIlllIIlIllIllllI"""
    """IlIllI""";lI.close();"""llIIIllIIIlIIIIlIlllIIlIllIllllI""";"""llIIIllIIIlIIIIlIlllIIlIllIllllI"""

    print("Process finished!")
    time.sleep(2.5)

if option.lower() == "requestpass":
    requestpass()
elif option.lower() == "createpass":
    createpass()
else:
    print("invalid.")
    time.sleep(1)
