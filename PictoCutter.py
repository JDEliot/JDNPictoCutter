stretch = True

import tkinter as tk
from tkinter import filedialog
def PictoCutter(CodeName, CoachCount, outputfolder, stretch=True):
    import requests
    from PIL import Image
    from io import BytesIO

    css = requests.get("http://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/" + CodeName + "/assets/web/pictos-sprite.css").text.split("\n")
    ##It downloads the CSS file that contains the filenames##

    pictoAtlas = Image.open(BytesIO(requests.get("http://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/" + CodeName + "/assets/web/pictos-sprite.png", stream=True).content))
    ##It downloads the "Atlas" that has all the pictos ordered alphabeticly##
    if int(CoachCount) > 1:
        y1 = 40
        x1 = 217
    else:
        y1 = 0
        x1 = 256
    x = 256
    y = 0
    for picto in css:
        pictoName = picto.split("-")
        pictoName = pictoName[1].split("{")
        pictoName = pictoName[0]##It """parses""" the line and takes what i need that its the pictoname
        picto = pictoAtlas.crop((y,y1,x,x1))
        y = y + 256
        x = x + 256
        if (int(CoachCount) > 1) and stretch:
            picto = picto.resize((256,256))##it resizes the pictos so they work fine
        picto.save(outputfolder + pictoName + ".png")

print("Welcome to Eliott's Picto Cutter!")
CodeName = input("Write the song's CodeName (Remember the caps!): ")
CoachCount = int(input("Write the number of coaches that the song haves: "))
root = tk.Tk()
root.withdraw()
root.call('wm', 'attributes', '.', '-topmost', '1')
outputpath = filedialog.askdirectory(title="Select The Output Folder") + "/"
PictoCutter(CodeName, CoachCount, outputpath, stretch)