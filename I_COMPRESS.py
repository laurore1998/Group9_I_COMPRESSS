import os
import imghdr
import subprocess
import PIL
import tkinter.filedialog
from PIL import Image


class downiszepress:

    def __init__(self):
        self.myWidth = 0
        self.myHeight = 0
        self.myWidthtreedown = 0
        self.myHeighttreedown = 0
        self.myWidthsixdown = 0
        self.myHeightsixdown = 0
        self.myWidthninedown = 0
        self.myHeightninedown = 0
        self.myHeightfree =0
        self.myWidthfree =0
        self.newsizefree=0
        self.img = ''
        self.file_path = ''
        self.save_path = ''
        self.newsizetree=''
        self.newsizesix = ''
        self.newsizenine = ''
        self.lotopsyon=''

    def anrejistreExtension(self, id, extension):
        Image.EXTENSION[extension.lower()] = id.upper()

    Image.anrejistreExtension = anrejistreExtension

    def anrejistreExtensions(self, id, extensions):
        for extension in extensions:
            l.anrejistreExtension(id, extension)

    Image.anrejistreExtensions = anrejistreExtensions

    def tay(self):
        self.file_path = tkinter.filedialog.askopenfilename()
        self.img = PIL.Image.open(self.file_path)
        self.myHeight, self.myWidth = self.img.size
        print("Tay fichyew la se: Longè: ", self.myHeight," --> Lajè: ", self.myWidth)

        return self.myHeight, self.myWidth

    def redwiTay(self):
        tay = ""
        #print("Tay fichye w lan se :" + tay)
        ##############################################
        l.tay()
        self.myHeighttreedown = round(self.myHeight / 3)
        self.myWidthtreedown = round(self.myWidth / 3)
        self.myHeightsixdown = round(self.myHeight / 6)
        self.myWidthsixdown = round(self.myWidth / 6)
        self.myHeightninedown = round(self.myHeight / 9)
        self.myWidthninedown = round(self.myWidth / 9)

        print("\n****** KEK OPSYON POUW REDWI TAY LA: ******")
        print("A --> Longè", self.myHeighttreedown, " --> Lajè ", self.myWidthtreedown)
        print("B --> Longè", self.myHeightsixdown," --> Lajè ", self.myWidthsixdown)
        print("C --> Longè", self.myHeightninedown," --> Lajè ", self.myWidthninedown)
        print("N --> pou Antre Longè ak Lajè paw ")
        self.newsizetree=(self.myHeighttreedown, self.myWidthtreedown)
        self.newsizesix=(self.myHeightsixdown,self.myWidthsixdown)
        self.newsizenine=((self.myHeightninedown,self.myWidthninedown))
        print("\n========================")
        opsyon = input("Antre --> X pouw retounen na meni prensipal la.\n Antre sa w chwazi a: ")
        opsyon = opsyon.upper()
        try:
            if (opsyon == "A"):
                self.img = self.img.resize(self.newsizetree)
                self.save_path = tkinter.filedialog.asksaveasfilename()
                self.img.save(self.save_path+ "_nouvo.jpg")


                print("\nSuccès")
                meni = input("Antre --> X pouw retounen nan meni prensipal la: ")
                if meni == "X":
                    l.menu1()
            if (opsyon == "B"):
                self.img = self.img.resize(self.newsizesix)
                self.save_path = tkinter.filedialog.asksaveasfilename()
                self.img.save(self.save_path+ "_nouvo.jpg")
                print("\nSuccès")
                meni = input("Antre --> X pouw retounen nan meni prensipal la: ")
                if meni == "X":
                    l.menu1()
            if (opsyon == "C"):
                self.img = self.img.resize(self.newsizenine)
                self.save_path = tkinter.filedialog.asksaveasfilename()
                self.img.save(self.save_path+ "_nouvo.jpg")
                print("\nSuccès")
                meni = input("Antre --> X pouw retounen nan meni prensipal la: ")
                if meni == "X":
                    l.menu1()
            if (opsyon == "N"):
                print("\n==========================================")

               # while self.myHeightfree>self.myHeight and self.myWidthfree>self.myWidth:
                self.myHeightfree =int(input("Antre wotè ou vle imaj ou a genyen: "))
                self.myWidthfree =int(input("Antre lajè ou vle imaj ou a genyen: "))
                self.newsizefree=(self.myHeightfree,self.myWidthfree)
                self.img = self.img.resize(self.newsizefree)
                self.save_path = tkinter.filedialog.asksaveasfilename()
                self.img.save(self.save_path + "_nouvo.jpg")
                print("\nSuccès")

                meni = input("Antre --> X pouw retounen nan meni prensipal la: ")
                if meni == "X":
                    l.menu1()
        except (UnboundLocalError,ValueError):
            pass

    def menuImaj(self):

        print("\nKonprese imaj la(diminye nan tay li) --> K")
        print("\n=================================================")
        print("                                                  ")
        chwa2 = input("Antre --> X pouw retounen nan meni prensipal la.\n Antre sa w chwazi a: ")
        chwa2 = chwa2.upper()

        if (chwa2 == "K"):
            print("\nKonprese imaj a")
            l.redwiTay()
        if chwa2 == "X":
            l.menu1()


    def menu1(self):
        print(
            "\n                           __________________________________________________________________________________________")
        print(
            "                           |                                                                                        |")
        print(
            "                           |                                    * I_COMPRESS *                                      |  ")
        print(
            "                           |                                                                                        |")
        print(
            "                           |                               ******* HELLO *******                                    |")
        print(
            "                           |                     Bienvini nan aplikasyon ki ap pemet ou                             |")
        print(
            "                           |                                  KONPRESE IMAJ                                         |")
        print(
            "                           |                                                                                        |")
        print(
            "                           |             wap gen chans pou w konprese --> Image NAN APLIKASYON SA                   |")
        print(
            "                           |                                                                                        |")
        print(
            "                           |________________________________________________________________________________________|")

        print("\nMen sa pou w antre pouw komanse redwi fifye w yo:")
        print("          IMAGE --> I\n")
        print("===================================")
        chwa1 = input("\n Pouw kite pwogram lan antre :--> K \nAntre tip fichye ou vle konprese a: ")
        chwa1 = chwa1.upper()

        if (chwa1 == "K"):
            print(" AU REVOIR!!!")

        if (chwa1 == "I"):
            l.menuImaj()


l = downiszepress()
l.menu1()
