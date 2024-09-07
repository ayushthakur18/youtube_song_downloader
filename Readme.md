# Python YouTube Audio Downloader and Player
This Python script allows you to download audio from YouTube videos and play them using pygame's mixer. It uses the yt_dlp library to download the audio and pygame to play the audio.

# Dependencies
* yt_dlp: A python package to download videos from youtube.com or other video platforms.
pygame: A set of Python modules designed for writing video games, but it is also useful for making desktop apps and sound players.

# How to Use
The script can be run from the command line with the following arguments:

--d <song_name>: This will download the audio of the song from YouTube. The audio file will be saved in the 'downloads/' directory by default.
--p <song_name>: This will play the song from the 'downloads/' directory.

# Functions
download_audio(song_name, output_path='downloads/'): This function downloads the audio of a song from YouTube. The song_name is the name of the song to download and output_path is the path to save the downloaded audio file. The default output path is 'downloads/'.

play_song(song_path): This function plays a song using pygame.mixer. The song_path is the path to the song file.

# Example
To download a song:
    `python main.py --d "song name"`

To play a downloaded song:
    `python main.py --p "song name"`

Please note that the song name should be the same as the one used for downloading.

Error Handling
If an error occurs during the download, the script will print "Download failed: song_name". If an invalid argument is passed, the script will print "Invalid args".