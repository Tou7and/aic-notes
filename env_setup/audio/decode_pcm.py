import sys
import ffmpeg

def decode_as_pcm(in_filename, out_filename, **input_kwargs):
    """ Convert any audio to PCM with 16k sample rate. """
    try:
        out, err = (ffmpeg
            .input(in_filename, **input_kwargs)
            .output(out_filename, acodec='pcm_s16le', ac=1, ar='16k')
            .global_args('-loglevel', 'error')
            .global_args('-y')
            .run()
        )
    except ffmpeg.Error as e:
        print(e.stderr, file=sys.stderr)
        sys.exit(1)
    return out

if __name__ == "__main__":
    decode_as_pcm(sys.argv[1], sys.argv[2])


