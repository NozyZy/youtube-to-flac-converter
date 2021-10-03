import os
import youtube_dl

# Downloading new versions of the packages
print("Downloading new pip and youtube_dl...\n")
os.system("python -m pip install --upgrade pip")
os.system("pip install --upgrade youtube-dl")
os.system("cls")

stop = False

while not stop:

    # link
    link = ""
    firstTry = True
    while link[0:7] != "https://" and "youtu" not in link:
        if not firstTry:
            print(
                "ERROR - Enter a true youtube link (https://youtube.com/... or https://youtu.be/...)\n"
            )
        link = input("Enter youtube link (video or playlist) -> ")
        if link == "exit":
            quit()
        firstTry = False

    # base directory
    file_directories = open("directories.txt", "r+")
    directories = file_directories.readlines()
    file_directories.close()

    choice = 0
    if len(directories) > 0:
        firstTry = True
        print("\nChose a location to download in...\n")

        while choice <= 0 or choice > len(directories) + 1:
            if not firstTry:
                print("\nERROR - Enter a good number\n")
            for i in range(len(directories)):
                directories[i] = directories[i].replace("\n", "")
                print(f"{i+1} : {directories[i]}")

            print(f"{i+2} : new location\n")
            firstTry = False

            try:
                choice = int(input("Your choice -> "))
            except:
                if choice == "exit":
                    quit()
                print("\nERROR - Enter only a number\n")
                firstTry = True

    if len(directories) == 0 or choice == len(directories) + 1:
        path = input("New directory (ex : C:/Music) -> ")

        path.replace("\\", "/")

        if path[1:2] != ":/":
            path = "C:/" + path

        if path[-1] != "/":
            path += "/"

        double = False
        for directory in directories:
            if path == directory:
                double = True

        if not double:
            directories.append(path)

    else:
        path = directories[choice - 1].replace("\n", "")

    # new directory
    directory = input(
        "\nEnter directory location name (empty if in this directory) -> "
    )

    if directory == "exit":
        quit()

    elif len(directory) != 0 and directory[0] != "/":
        directory = "/" + directory
    directory.replace("\\", "/")

    path += directory

    # song format select
    choice = 0
    song_formats = ["flac", "mp3"]
    while not 0 < choice < len(song_formats) + 1:
        print("Choose music song format :")
        print(
            "\n".join(
                str(i + 1) + " -> " + song_formats[i] for i in range(len(song_formats))
            )
        )
        choice = int(input("Your choice -> "))
        if not 0 < choice < len(song_formats) + 1:
            print("\nERROR - Enter correct number !\n")

    # download
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": song_formats[choice - 1],
                "preferredquality": "192",
            }
        ],
        "outtmpl": path + "/%(title)s.%(ext)s",
    }

    print("Downloading... -> \033[92m", link, "\033[00m")

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        file_directories = open("directories.txt", "w+")
        for directory in directories:
            file_directories.write(directory + "\n")
        file_directories.close()

    except:
        print("\nERROR - Check if the directory or the link is good.\n")

    choice = input("\nDo you wanna continue downloading ? (y/n) -> ")

    if choice.lower() != "y":
        stop = True
    else:
        os.system("cls")
