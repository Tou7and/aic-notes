# Create a audio player on notebook
```
import IPython.display as ipd
audio="/media/volume1/Corpus/NER_Trs_Corpus/NER-Trs-Vol6-train/Other/Wav/CX/20130430/CX_20130430_023.wav"
ipd.Audio(audio)
```

# Create many audio players
```
trans = "/media/volume1/aicasr/Label/XN2021/m8w1w2/raw/2520/trans.csv"

with open(trans, "r") as reader:
    lines = reader.readlines()

for line in lines[1:]:
    info = line.split("\t")
    # print(info[0])
    ipd.display(ipd.Audio(info[0]))
    print(info[1])
    print()
```

# Plot waveform and save it
```
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

spf = wave.open("/media/volume1/aicasr/spbr-handlers-cmuh/tests/samples/774.wav", "r")

# Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, "Int16")

# If Stereo
if spf.getnchannels() == 2:
    print("Just mono files")
    sys.exit(0)

plt.figure(1)
plt.title("Signal Wave...")
plt.plot(signal)
# plt.show()
plt.savefig("774.png")
```

