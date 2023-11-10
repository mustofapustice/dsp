import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
fs = 8000 # sampling rate
N = 50 # order of filer
fc = 1200 # cutoff frequency
b = sig.firwin(N + 1, fc, fs=fs, window='hamming', pass_zero='highpass')
w, h_freq = sig.freqz(b, fs=fs)
z, p, k = sig.tf2zpk(b, 1)
plt.figure(1)
plt.plot(w, np.abs(h_freq),'r') # magnitude
plt.xlabel('frequency(Hz)')
plt.ylabel('Magnitude')
plt.figure(2)
plt.plot(w, np.unwrap(np.angle(h_freq)),'r') # phase
plt.xlabel('frequency(Hz)')
plt.ylabel('Phase(angel)')
plt.figure(3)
plt.scatter(np.real(z), np.imag(z), marker='o', edgecolors='g')
plt.scatter(np.real(p), np.imag(p), marker='x', color='b')
plt.title('Poles-Zeros')
plt.xlabel('Real part')
plt.ylabel('Imaginary part)')
plt.show()