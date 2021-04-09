import simpleaudio as sa 
import numpy as num
import matplotlib.pyplot as pyplot
import wavio 


duration = 1 
sample_rate = 48000 #samples per second 
freq = 440 * 2 * num.pi #in radians

#need twice the sample rate of freq to have enough quality.
#generate array to hold raw 16bit values. each 16bit chunk = 1 sample
raw_audio_bits = num.linspace (0,duration,sample_rate * duration, False)

sin_wave = num.sin(freq * raw_audio_bits ) #no phase specified in hw

#2^15 - 1 = 32767 is the full amp range. I want my amplitude to be limited to a quarter this size (32767 *.25 = 8191). 
audio = sin_wave * 16384/ num.abs(sin_wave)

#convert wav to 16 bit integers
sound = audio.astype(num.int16)
print(sound)
out = num.clip(sound, -8192, 8192)
print(out)

#write to wav file
wavio.write("clipped.wav", out, sample_rate, sampwidth=2)

wav_obj = sa.WaveObject.from_wave_file("sine.wav")
playback_obj = wav_obj.play() 

if playback_obj.is_playing():
    print('still playing')

playback_obj.wait_done() 




