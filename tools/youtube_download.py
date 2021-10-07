import sys
import os
import youtube_dl

WAV_OPTS = {
    'verbose': 1,
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s-%(id)s.%(ext)s',
    'noplaylist': True,
    'continue_dl': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }]
}

MP3_OPTS = {
    'verbose': 1,
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s-%(id)s.%(ext)s',
    'noplaylist': True,
    'continue_dl': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

MP4_OPTS = {
    'verbose': 1,
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': '%(title)s-%(id)s.%(ext)s',
    'noplaylist': True,
    'continue_dl': True,
    'writesubtitles': True,
    'subtitleslangs': ["en", "cn"],
    'postprocessors': [
        {'key': 'FFmpegVideoConvertor', 'preferedformat': "mp4"}
    ]
}

class YoutubeDownloader:
    """ A Youtube downloader """
    def __init__(self, url, storage_dir="./tmp", dst_format="mp4", dst_filename="default"):
        self.format = dst_format
        self.url = url
        self.data_dir = storage_dir
        self.make_datadir()

        if dst_format == "mp4":
            self.opts = MP4_OPTS
        elif dst_format == "mp3":
            self.opts = MP3_OPTS
        else:
            self.opts = WAV_OPTS
            self.format = "wav"

        if dst_filename == "default":
            self.opts['outtmpl'] = self.data_dir+'/%(title)s-%(id)s.%(ext)s'
            self.filepath = "default"
        else:
            self.opts['outtmpl'] = self.data_dir+'/'+dst_filename+'.%(ext)s'
            self.filepath = self.data_dir+'/'+dst_filename+'.'+self.format

        self.results = {"status": -1, "video": "none", "audio": "none", "media": "none"}

    def make_datadir(self):
        """ Make directory to store media data """
        try:
            if os.path.isdir(self.data_dir) == False:
                os.makedirs(self.data_dir)
        except Exception as error:
            raise RuntimeError(error)

    def run(self):
        """ Download video from channel and convert to WAV format.

        Status codes for results:
            -1: "Process initialed"
            0: "Process finished"
            1: "Fail to get content from channel"
        """
        with youtube_dl.YoutubeDL(self.opts) as ydl:
            ydl.cache.remove()
            info_dict = ydl.extract_info(self.url, download=True)
            if self.filepath == "default":
                file_name = "{}-{}.{}".format(info_dict["title"], info_dict["id"], self.format)
                self.filepath = os.path.join(self.data_dir, file_name)

        if os.path.exists(self.filepath):
            self.results["media"] = self.filepath

def download_wave_from_youtube(link, dst_filename, dst_dir="/Users/mac/Downloads/"):
    # cwd = os.getcwd()
    # tmp_dir = os.path.join(cwd, "tmp")
    ydl_p = YoutubeDownloader(link, storage_dir=dst_dir, dst_format="mp3", dst_filename=dst_filename)
    ydl_p.run()

if __name__ == "__main__":
    download_wave_from_youtube("https://www.youtube.com/watch?v=gdPFOF91xb0", "coin-sound")
