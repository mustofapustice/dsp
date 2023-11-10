import numpy as np
import matplotlib.pyplot as plt
# Parameters for the sinusoidal signal
amplitude = 1.0
frequency = 5.0 # Hz
sampling_frequency = 20.0 * frequency # Must be greater than Nyquist rate (2 * frequency)
duration = 1.0 # seconds
# Time values for the continuous signal
t_continuous = np.linspace(0, duration, int(sampling_frequency * duration), endpoint=False)
# Generate the continuous sinusoidal signal
continuous_signal = amplitude * np.sin(2 * np.pi * frequency * t_continuous)
# Time values for the discrete samples
t_samples = np.arange(0, duration, 1 / sampling_frequency)
# Sample the continuous signal
sampled_signal = amplitude * np.sin(2 * np.pi * frequency * t_samples)
# Plot the continuous and sampled signals
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t_continuous, continuous_signal, label='Continuous Signal')
plt.title('Continuous Sinusoidal Signal')
plt.xlabel('Time (s)')
plt.grid(True)
plt.legend()
plt.subplot(2, 1, 2)
plt.stem(t_samples, sampled_signal, markerfmt='ro', linefmt='r-', basefmt='r-', label='Sampled Signal')
plt.title('Sampled Sinusoidal Signal')
plt.xlabel('Time (s)')
plt.grid(True)
plt.legend()
# Reconstruction by simply interpolating between samples
reconstructed_signal = np.interp(t_continuous, t_samples, sampled_signal)
# Plot the reconstructed signal
plt.figure(figsize=(10, 4))
plt.plot(t_continuous, continuous_signal, label='Original Signal', linestyle='dashed')
plt.plot(t_samples, sampled_signal, label='Sampled Signal', marker='o', linestyle='None')
plt.plot(t_continuous, reconstructed_signal, label='Reconstructed Signal')
plt.title('Reconstruction of Analog Signal from Samples')
plt.xlabel('Time (s)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()