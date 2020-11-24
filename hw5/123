import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import rfft, rfftfreq

Time = 1
samr = 44100
nPoint = int(Time*samr)

Wx = np.linspace(0.0, 0.002, int(0.002*44100))
Wnoise = np.random.randint(low=-2**15, high=2**15, size=int(0.002*44100), dtype='int64')

plt.figure()

plt.title("Homework_5_Withe Noise")
plt.xlabel("Time index")
plt.ylabel("Amplitude")
plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
plt.plot(Wx, Wnoise, color='black', lw='0.5')

#-----------------------------------------------------------
def sinsum(x, ampl, freq, *an):
    sin_sum = 0
    order = len(an[0])
    for i in range(order):
        sin_sum = sin_sum + an[0][i]*np.sin(2*(i+1)*np.pi*freq*x)
    return (ampl/sum(an[0]))*sin_sum

funfreq = 440
A = 2**15
an_0 = [1.0]
an_1 = [1.0, 0.0, 1.0]
an_2 = [1.0, 0.5, 0.33, 0.25, 0.2, 0.1667, 0.14]
an_3 = [1.0, 0.0, 0.33, 0.0, 0.2, 0.0, 0.14]

sinx = np.linspace(0.0, Time, nPoint)

sinfx = rfftfreq(nPoint, d=1/samr)
sin_0 = np.array([sinsum(i, A, funfreq, an_0) for i in sinx], dtype='int64')
sin_1 = np.array([sinsum(i, A, funfreq, an_1) for i in sinx], dtype='int64')
sin_2 = np.array([sinsum(i, A, funfreq, an_2) for i in sinx], dtype='int64')
sin_3 = np.array([sinsum(i, A, funfreq, an_3) for i in sinx], dtype='int64')

sinf_0 = np.abs(rfft(sin_0))
sinf_1 = np.abs(rfft(sin_1))
sinf_2 = np.abs(rfft(sin_2))
sinf_3 = np.abs(rfft(sin_3))

plt.figure()

plt.subplot(211)
plt.title("Homework_5_Sum of Sinusoids")
plt.plot(sinx, sin_0, color='blue', lw='0.5', ls='--')
#plt.plot(sinx, sin_1, color='blue', lw='0.5', ls='--')
#plt.plot(sinx, sin_2, color='blue', lw='0.5', ls='--')
#plt.plot(sinx, sin_3, color='blue', lw='0.5', ls='--')
plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0)) 
plt.xlabel("Time index",labelpad=5)
plt.ylabel("Amplitude",labelpad=0)
plt.xlim(0, 200/samr)

plt.subplot(212)
plt.plot(sinfx, sinf_0, color='gray', lw='0.5')
#plt.plot(sinfx, sinf_1, color='gray', lw='0.5')
#plt.plot(sinfx, sinf_2, color='gray', lw='0.5')
#plt.plot(sinfx, sinf_3, color='gray', lw='0.5')
plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0)) 
plt.xlabel("Frequency index",labelpad=5)
plt.ylabel("Magnitude",labelpad=8)

plt.subplots_adjust(wspace =0, hspace =0.6)

#-----------------------------------------------------------

samplerate, data = wav.read(r'D:\wakasekasumi\5_演算法\ICA_08\ul1.wav')

length = data.shape[0] / samplerate
wavTime = np.linspace(0., length, data.shape[0])

print(f"samplerate = {samplerate}")
print(f"number of channels = {data.shape[0]}")
print(f"length = {length} s")

plt.figure()

plt.subplot(211)
plt.title("Homework_5_wavfile:ul1.wav")
plt.plot(wavTime, data, color='yellow', lw='0.5', ls='--')
plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0)) 
plt.xlabel("Time index",labelpad=5)
plt.ylabel("Amplitude",labelpad=0)

plt.subplot(212)
dataf = np.abs(rfft(data))
datax = rfftfreq(data.shape[0], d=1/samplerate)
plt.plot(datax, dataf, color='yellow', lw='0.5', ls='--')
plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0)) 
plt.xlabel("Frequency index",labelpad=5)
plt.ylabel("Magnitude",labelpad=8)

plt.subplots_adjust(wspace =0, hspace =0.6)

#wav.write("sin_0.wav", 44100, sin_0)
#wav.write("sin_1.wav", 44100, sin_1)
#wav.write("sin_2.wav", 44100, sin_2)
#wav.write("sin_3.wav", 44100, sin_3)
#-----------------------------------------------------------

plt.show()
