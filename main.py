import os
import eyed3
from termcolor import colored
import ctypes

os.system('cls')


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def clrscr():
    rep = input('Press ENTER to Proceed'.center(120))
    if rep == '':
        os.system('cls')


def printer(x):
    for _ in range(0, x):
        print()


def GetPath():
    print("paste the path/dir that contains the mp3 files: ")
    return input("=> ")


def PrintList(list):
    i = 1
    for x in list:
        if i > 9:
            print(str(i) + '/ ' + colored(str(x), 'red'))
        else:
            print('0' + str(i) + '/ ' + colored(str(x), 'red'))
        i += 1


def stripper(string):
    return string.replace(" ", "")


def Edit(list, path):
    for x in list:
        os.chdir(path)
        audiofile = eyed3.load(x)
        print("File Name: " + colored(x, 'red'))
        artst = input("artist: ")
        audiofile.tag.artist = artst
        albm = input("album: ")
        audiofile.tag.album = albm
        albmartst = input("album artist: ")
        audiofile.tag.album_artist = albmartst
        ttl = input("song title: ")
        audiofile.tag.title = ttl
        tracknb = -1
        while tracknb < 1 or tracknb > 200:
            tracknb = int(input("track number: "))
        audiofile.tag.track_num = tracknb
        audiofile.tag.save()
        clrscr()


def EditSingle(list, path, TrackNb):
    os.chdir(path)
    audiofile = eyed3.load(list[TrackNb])
    print("File Name: " + colored(list[TrackNb], 'red'))
    artst = input("artist: ")
    audiofile.tag.artist = artst
    albm = input("album: ")
    audiofile.tag.album = albm
    albmartst = input("album artist: ")
    audiofile.tag.album_artist = albmartst
    ttl = input("song title: ")
    audiofile.tag.title = ttl
    tracknb = -1
    while tracknb < 1 or tracknb > 200:
        tracknb = int(input("track number: "))
    audiofile.tag.track_num = tracknb
    audiofile.tag.save()
    clrscr()


def EditAAO(list, path):
    artst = input("artist: ")
    albm = input("album: ")
    albmartst = input("album artist: ")
    ttl = input("song title: ")
    tracknb = -1
    while tracknb < 1 or tracknb > 200:
        tracknb = int(input("track number: "))
    for x in list:
        os.chdir(path)
        audiofile = eyed3.load(x)
        audiofile.tag.artist = artst
        audiofile.tag.album = albm
        audiofile.tag.album_artist = albmartst
        audiofile.tag.title = ttl
        audiofile.tag.track_num = tracknb
        audiofile.tag.save()


def EditChoice():
    choice = ''
    while choice != '1' and choice != '2' and choice != '3':
        print("Do you want to edit all the files or a single file? ")
        print()
        print(' 1-All files One by One')
        print(' 2-Single File')
        print(' 3-All files at once')
        print()
        choice = input('=> ')
    return choice


def ReqTrackNb(list):
    choice = 0
    while not (0 < choice <= len(list)):
        printer(3)
        print('Type the Number of the track that you want to edit: ')
        choice = int(input("=> "))
    return choice


def Disclaimer():
    print(
        colored("!! Note that this Tool will only work on folders that contains MP3 files only !!", 'red').center(130))
    printer(4)


def AskGuide():
    print("If you want a quick guide on how to use this tool type 'y' otherwise press ENTER")
    choice = '0'
    while choice != '' and choice != 'y':
        print()
        choice = input("=>")
    return choice


def PrintGuide():
    print(colored("Hi, thanks a lot for using this tool. ♥♥", 'magenta').center(130))
    print("""This tool gives you the ability to Add/Edit the metadata for a .mp3 file
including Artist/Artist name/Album/track number/title 

So in order to use it correctly, you'll have to enter a path of a folder that only contains .mp3 files as
shown previously in the red disclaimer message     


After, you can choose between 3 options:


1- or you can choose to edit the whole folder's content file by file
(for example, when you finish editing the first file you'll be able to do the same to the second)

2- editing a single file from that folder as a result you'll be asked for the track or file number

3- choosing the same values of the metadata to be changed for all the .mp3 files inside that folder

""")

    print(colored("     !! Note again, this will only work on folders that only contain .mp3 files !!", 'red'))
    print(colored("     !!     So keep that in mind when entering your path in the next window     !!", 'red'))
    printer(2)
    print(colored("thanks again,", 'magenta').center(30))
    printer(1)
    print(colored("Mouhib", 'magenta').center(40))
    printer(2)


def Done():
    os.system('cls')
    printer(4)
    print(colored("Everything went perfect.. ", 'red'))
    Mbox('task succeeded ', "the process completed successfully", 1)


def welcome():
    printer(2)
    print(colored("Welcome to MP3 Metedit", 'magenta').center(130))
    printer(3)


# Callers##
welcome()

Disclaimer()

gd = AskGuide()

if gd == 'y':
    os.system('cls')
    PrintGuide()
    clrscr()
else:
    os.system('cls')

path = GetPath()

list = os.listdir(path)

os.system('cls')

EditingMethod = EditChoice()
os.system('cls')

if EditingMethod == '1':
    os.system('cls')
    Edit(list, path)
    Done()
elif EditingMethod == '2':
    KeepGoing = True
    while KeepGoing:
        PrintList(list)
        tnb = ReqTrackNb(list)
        os.system('cls')
        EditSingle(list, path, tnb - 1)
        print("Wanna edit another file ? (yes/no): ")
        rep = ''
        while rep.upper() != 'YES' and rep.upper() != 'NO':
            rep = input("=> ")
        if rep.upper() == 'NO':
            KeepGoing = False
    Done()
else:
    os.system('cls')
    EditAAO(list, path)
    Done()
