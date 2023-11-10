import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
fs = 8000
[n, w] = sig.buttord([1000 / 4000, 2500 / 4000], [400 / 4000, 3200 / 4000], 1, 50)
[b, a] = sig.butter(n, w, btype='bandpass')
w, h = sig.freqz(b, a, 512, fs=fs)
z, p, k = sig.tf2zpk(b, a)
plt.figure(1)
plt.plot(w, np.abs(h),'r')
plt.xlabel('Frequency(HZ)')
plt.ylabel('Magnitude')
plt.figure(2)
plt.plot(w, np.unwrap(np.angle(h)),'r')
plt.xlabel('Frequency(HZ)')
plt.ylabel('Phase')
plt.figure(3)
plt.scatter(np.real(z), np.imag(z), marker='o', edgecolors='b')
plt.scatter(np.real(p), np.imag(p), marker='x', color='g')
plt.title('Poles-Zeros')
plt.xlabel('Real part')
plt.ylabel('Imaginary part')
plt.tight_layout()
plt.show()