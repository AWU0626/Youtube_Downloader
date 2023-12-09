import tkinter as tk
from pytube import YouTube
from tkinter import filedialog, ttk


class Downloader():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("YouTube Downloader")
        self.centerApp(500, 300)

        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.pack()

        self.link_label = ttk.Label(
            self.frame, text="Paste Youtube Link Here:")
        self.link_label.pack(fill='x', expand=True)

        self.link_entry = ttk.Entry(self.frame)
        self.link_entry.pack(fill='x', expand=True)
        self.link_entry.focus()

        # Download Button
        download_button = ttk.Button(
            self.frame, text="Download mp4", command=self.download_video)
        download_button.pack()

        # Quit Button
        quit_button = ttk.Button(self.frame, text="Quit",
                                 command=self.root.destroy)
        quit_button.pack()

        self.root.mainloop()

    def download_video(self):
        try:
            url = self.link_entry.get()
            folder = filedialog.askdirectory()
            if folder:
                print(f"Selected Folder: {folder}")

                curr_video = YouTube(url)
                stream = curr_video.streams.filter(
                    progressive=True, file_extension="mp4").get_highest_resolution()
                print("Downloading...")
                stream.download(output_path=folder)
                print("Download finished")
        except Exception as err:
            print(err)
            return None

    def centerApp(self, default_width, default_height):
        beginX = self.root.winfo_screenwidth() / 2 - (default_width / 2)
        beginY = self.root.winfo_screenheight() / 2 - (default_height / 2)
        geometry_param = "{}x{}+{}+{}".format(default_width,
                                              default_height, int(beginX), int(beginY))
        self.root.geometry(geometry_param)
        return


if (__name__ == '__main__'):
    downloader = Downloader()
