import os
import youtube_dl

print("Downloading new pip and youtube_dl...\n")
os.system("python -m pip install --upgrade pip")
os.system("pip install --upgrade youtube-dl")
os.system("cls")

stop = False

while not stop:

    link = ""
    firstTry = True
    while link[0:7] != "https://" and "youtu" not in link:
        if not firstTry:
            print("Enter a true youtube link (https://youtube.com/... or https://youtu.be/...)\n")
        link = input("Enter youtube link (video or playlist) -> ")
        if link == "exit":
            quit()
        firstTry = False


    file_directories = open("directories.txt", "r+")
    directories = file_directories.readlines()
    file_directories.close()

    choice = 0
    if len(directories) > 0:
        firstTry = True
        print("\nChose a location to download in...\n")
        
        while choice <= 0 or choice > len(directories) + 1:
            if not firstTry:
                print("\nEnter a good number\n")
            for i in range(len(directories)):
                directories[i] = directories[i].replace("\n", "")
                print(f"{i+1} : {directories[i]}")

            print(f"{i+2} : new location\n")
            firstTry = False

            try:
                choice = int(input("Your choice -> "))
            except:
                if path == "exit":
                    quit()
                print("\nEnter only a number\n")
                firstTry = True


    if len(directories) == 0 or choice == len(directories) + 1:
        path = input("New directory (ex : C:/Music) -> ")

        if path[-1] != "/" and path[-1] != "\\":
            path += "/"

        double = False
        for directory in directories:
            if path == directory:
                double = True

        if not double:
            directories.append(path)

    else:
        path = directories[choice - 1].replace("\n", "")

    path += input("\nEnter directory location name (empty if in this directory) -> ")

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
            'preferredquality': '192',
        }],
        'outtmpl': path + '/%(title)s.%(ext)s',
    }

    print("Downloading... -> ", link)

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        file_directories = open("directories.txt", "w+")
        for directory in directories:
            file_directories.write(directory + "\n")
        file_directories.close()

    except:
        print("\nAn error occured. Check if the directory or the link is good.\n")

    

    choice = input("\nDo you wanna continue downloading ? (y/n) -> ")

    if choice.lower() != "y":
        stop = True
    else:
        os.system("cls")