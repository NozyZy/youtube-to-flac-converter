# YouTube to flac music converter

A little Python script to convert your youtube videos and playlist into `.flac` audio files, without any compression (contrary to `.mp3` files)

# Install


## Requirements

- It is based on ![python badge](https://img.shields.io/badge/python-3.7-blue "python badge") or earlier -> [Download here](https://www.python.org/downloads/)
- It requires ![pip badge](https://img.shields.io/badge/pip-21.1-green "pip badge") -> check the box `pip` when installing `Python`
- It also requires ![ffmpeg badge](https://img.shields.io/badge/ffmpeg-4.3.1-orange "ffmpeg badge") or earlier -> [Download here](https://ffmpeg.org/download.html)
- Last but not least, ![youtube-dl badge](https://img.shields.io/badge/youtube--dl-2021.06.06-red "youtube-dl badge") or earlier -> write this command in Powershell/CMD : `pip install --upgrade youtube-dl`

Approximate size for a 3-4min music video : 50 MB (10x more than `.mp3`)

When everything is ready to use, the script will automatically update `pip` and `youtube-dl`


## Usage

On windows, just double click on `YouTube to flac.bat` to launch the script.
Otherwise, launch the `ytb_flac.py` with python (`python ytb_flac.py`)

First, you'll have to enter a youtube link to download, video or playlist, both work
![first step](https://cdn.discordapp.com/attachments/826575188303806476/884193179396636682/unknown.png)

Then, you'll have two type of choices :
- download your music into a saved directory
- download in a new directory, that will be saved for the next time

![second step](https://cdn.discordapp.com/attachments/826575188303806476/884194889368215572/unknown.png)

1. If you selected a pre-saved directory, you can download in a new sub-directory (as for the band), or leave it blank 

![second-step-1](https://user-images.githubusercontent.com/60878689/132142451-f1b0cbf9-92cc-4ca7-b28d-35f8b5280ba7.png)

2.  If you selected to create a new directory, you'll have to create the location (use `/` and not `\` !). After that, you'll have to do the step above.

![second-step-2](https://user-images.githubusercontent.com/60878689/132142503-393c16dc-bdb5-4ca2-abf6-37108ec2ec1d.png)

After that, the download begins...

![step-three](https://user-images.githubusercontent.com/60878689/132142568-171af48e-0f78-48ca-b272-d69f2bf47eb3.png)

And... your music/playlist is downloaded !

## Participate
It is a pretty light script, but every changes are welcome ! Don't hesitate :)
