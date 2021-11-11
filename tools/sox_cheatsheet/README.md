# Probe Audio
sox --info input.wav

# Format Convertion
## WAV to MP3
sox input.wav output.mp3

# WAV to mp3 with specified bitrate (256 kbps)
sox input.wav -C 256 output.mp3

# RAW PCM to WAV (16 kHz, 16bit)
sox -r 16000 -e signed-integer -b 16 input.raw output.wav

## Convert to 8k Hz
sox input.wav -r 8000 output.wav

## Convert stereo to mono
sox input.wav -c 1 output.wav

# Audio Manipulation
## Slice audio from 1.5 seconds with 2.5 seconds duration (1.5 - 4.0)
sox input.wav output.wav trim 1.5 2.5

## Combine two files by concatenation
sox a.wav b.wav c.wav concatenated.wav

## Combine two files by mixing their contents
sox -m a.wav b.wav c.wav mixed.wav


# Sound Effects
## Reduce level by 12dB
sox input.wav output.wav gain -12

## Normalise to 0dBFS.
sox input.wav output.wav norm

## 1.5X Faster with pitch shift
sox input.wav output.wav speed 1.5

## 1.5X Faster without pitch shift
sox input.wav output.wav tempo 1.5

## Add reverberation
sox input.wav output.wav reverb 50 50 50 50 10 10
- Args 
  - reverberance (range: 0 ~ 100)
  - HF-damping (range: 0 ~ 100)
  - room-scale (range: 0 ~ 100)
  - stereo-depth (range: 0 ~ 100)
  - pre-delay (0ms) (range: 0 ~ 500)
  - wet-gain (0dB) (range: -10 ~ 10)

# Generation
## Make white noise (2.5 seconds)
sox -n output.wav synth 2.5 noise

## Make sine tone (2.5 seconds, 440 Hz)
sox -n output.wav synth 2.5 sine 440


