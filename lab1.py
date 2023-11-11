import numpy as np
import matplotlib.pyplot as plt
# Define the parameters of the signal
f = 10 # Frequency of the sinusoid (in Hz)
fs = 100 # Sampling rate (in Hz)
t = np.arange(0, 1, 1/fs) # Time vector
x = np.sin(2*np.pi*f*t) # Generate the sinusoidal signal
# Plot the original signal
plt.subplot(3, 1, 1)
plt.plot(t, x,'r')
plt.ylim(-1.5,1.5)
plt.xlim(0,1)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Original Signal')
# Sample the signal
Ts = 1/fs # Sampling interval (in seconds)
n = np.arange(0, 1+Ts, Ts) # Sampling instants
xn = np.sin(2*np.pi*f*n) # Sampled signal
# Plot the sampled signal
plt.subplot(3, 1, 2)
plt.stem(n, xn,'r')
plt.ylim(-1.5,1.5)
plt.xlim(0,1)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sampled Signal')
# Reconstruct the analog signal using ideal reconstruction
xr = np.zeros_like(t) # Initialize the reconstructed signal
for i in range(len(n)):
    xr += xn[i]*np.sinc((t-(i*Ts))/Ts)
# Plot the reconstructed signal
plt.subplot(3, 1, 3)
plt.plot(t, xr,'r')
plt.ylim(-1.5,1.5)
plt.xlim(0,1)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Reconstructed Signal')
plt.tight_layout()
plt.show()