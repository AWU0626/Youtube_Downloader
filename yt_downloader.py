import tkinter as tk
from pytube import YouTube
from tkinter import filedialog


def download_video(url, device_url):
    try:
        curr_video = YouTube(url)
        stream = curr_video.streams.filter(
            progressive=True, file_extension="mp4").get_highest_resolution()

        stream.download(output_path=device_url)
        print("Download finished")
    except Exception as err:
        print(err)
        return None


def select_file_location():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected Folder: {folder}")
    return folder


# module lock
if __name__ == "__main__":
    print("Enter 'q' or 'quit' to exit the application.\n")
    quit = False
    root = tk.Tk()
    root.withdraw()

    while (not quit):
        video_url = input("Enter YouTube Video link to download: ")
        if (video_url.upper() == "QUIT" or video_url.upper() == "Q"):
            quit = True
            break

        directory_url = select_file_location()

        if directory_url:
            print("Download began")
            download_video(video_url, directory_url)
        else:
            print("invalid file location")
