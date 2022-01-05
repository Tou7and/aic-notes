""" Convert mp3 to nightcore version.

Requirements:
    FFmpeg installed.
    > pip install nightcore


Usage:
    python mp3_to_nightcore [MP3 PATH] [NC PATH]

"""
import sys
import nightcore as nc

def mp3_to_nightcore(mp3_path, nightcore_path):
    nc_audio = mp3_path @ nc.Tones(1)
    nc_audio.export(nightcore_path)
    return 


if __name__ == "__main__":
    mp3_p = sys.argv[1]
    nc_p = sys.argv[2]

    mp3_to_nightcore(
        mp3_p,
        nc_p
    )
