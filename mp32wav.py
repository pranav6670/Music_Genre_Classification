from os import path
from pydub import AudioSegment

# files
src = 'predict/Coldplay - Viva La Vida (Acoustic Cover).mp3'
dst = 'predict/test.wav'

# convert wav to mp3
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")