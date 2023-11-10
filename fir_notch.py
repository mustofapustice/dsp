import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np
fs = 8000
N = 50
fc = np.array([2000, 2050])
b = sig.firwin(N + 1, fc, fs=fs, window='hamming', pass_zero='bandstop')
z, p, k = sig.tf2zpk(b, 1)
w, h_freq = sig.freqz(b, 1, fs=fs)
plt.figure(1)
plt.plot(w, np.abs(h_freq),'r')
plt.xlabel('frequency(Hz)')
plt.ylabel('Magnitude')
plt.figure(2)
plt.plot(w, np.unwrap(np.angle(h_freq)),'r')
plt.xlabel('frequency(Hz)')
plt.ylabel('Phase(angel)')
plt.figure(3)
plt.scatter(np.real(z), np.imag(z), marker='o', edgecolors='b')
plt.scatter(np.real(p), np.imag(p), marker='x', color='b')
plt.title('Poles-Zeros')
plt.xlabel('Real part')
plt.ylabel('Imaginary part)')
plt.tight_layout()
plt.show()