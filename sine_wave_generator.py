# https://github.com/alisoltanirad/Binaural_Beats
import numpy as np
from scipy.io import wavfile

def export_sine_wave(frequency=440, duration=10, sample_rate=44100):
    wavfile.write('sine_wave_{}_hz_{}_seconds.wav'.format(frequency, duration),
                  sample_rate,
                  generate_sine_wave(frequency, duration, sample_rate))


def generate_sine_wave(frequency=440, duration=10, sample_rate=44100):
    max_amplitude = np.iinfo(np.int16).max
    samples = np.linspace(0, duration, int(sample_rate * duration),
                           endpoint=False)
    signal = (np.sin(2 * np.pi * frequency * samples)
              * max_amplitude).astype(np.int16)
    return signal


if __name__ == '__main__':
    export_sine_wave()