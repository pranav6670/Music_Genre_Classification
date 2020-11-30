from os import path
from pydub import AudioSegment

# files
src = 'songs/Old Town Road Mp3 By Billy Ray Cyrus and Lil Nas X.mp3'
dst = 'predict/OTR.wav'

# convert wav to mp3
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")