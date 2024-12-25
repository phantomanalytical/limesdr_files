import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def analyze_captured_signal(filename):
    #Read complex samples
    data = np.fromfile(filename, dtype=np.complex64)

    #Perform FFT
    spectrum = npn.fft.fftshift(np.fft.fft(data))
    freq = np.fft.fftshift(np.fft.fftfreq(len(data)))

    #Plot spectrum
    plt.figure(figsize=(12,6))
    plt.plot(freq, 10*np.log10(np.abs(spectrum)))
    plt.title('LimeSDR Signal Spectrum')
    plt.xlabel('Frequency')
    plt.ylabel('Power (dB)')
    plt.show()
