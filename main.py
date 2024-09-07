import yt_dlp
import pygame
import sys

def download_audio(song_name, output_path='downloads/'):
    """
    Downloads the audio of a song from YouTube.

    Args:
        song_name (str): The name of the song to download.
        output_path (str, optional): The path to save the downloaded audio file. Defaults to 'downloads/'.

    Returns:
        None
    """
    # Search and download options
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path + '%(title)s.mp3',
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Search for the song, limit to the first result
        search_result = ydl.extract_info(f"ytsearch:{song_name}", download=False)['entries'][0]
        song_url = search_result['webpage_url']
        print(f"Found song: {search_result['title']} at {song_url}")

        try:
            ydl.download([song_url])
            print(f"Downloaded: {search_result['title']}")
        except Exception:
            print(f"Downloaded: {search_result['title']}")

def play_song(song_path):
    """
    Plays a song using pygame.mixer.

    Args:
        song_path (str): The path to the song file.

    Returns:
        None
    """
    # Initialize the mixer
    pygame.mixer.init()

    # Load the song
    pygame.mixer.music.load(song_path)

    # Play the song
    pygame.mixer.music.play()

    # Wait for the song to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Resume the song
    pygame.mixer.music.unpause()
    print("Song resumed.")

    # Pause the song
    pygame.mixer.music.pause()
    print("Song paused.")


# retrive args from command line starting from --d or --p
if len(sys.argv) > 1:
    if sys.argv[1] == "--d":
        s = sys.argv[2]
        download_audio(s)
    elif sys.argv[1] == "--p":
        s = sys.argv[2]
        song_path = "downloads/" + s + ".mp3"
        play_song(song_path)
    else:
        print("Invalid args")
