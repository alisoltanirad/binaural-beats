# https://github.com/alisoltanirad/Binaural_Beats
import numpy as np
from scipy.io import wavfile
from sine_wave_generator import generate_sine_wave

def export_binaural_beat(frequencies=[420,440], duration=10, sample_rate=44100):
    wavfile.write('binaural_beat_{}_hz_{}_seconds.wav'.format(
        abs(frequencies[0] - frequencies[1]), duration), sample_rate,
        generate_binaural_beat(frequencies, duration, sample_rate))


def generate_binaural_beat(frequencies=[420,440], duration=10,
                           sample_rate=44100):
    left_signal = generate_sine_wave(frequencies[0], duration, sample_rate)
    right_signal = generate_sine_wave(frequencies[1], duration, sample_rate)
    binaural_beat = np.array([left_signal, right_signal]).T
    return binaural_beat


def generate_generic_binaural_beat(frequency=20, duration=10,
                                    sample_rate=44100):
    binaural_beat = generate_binaural_beat([420, 420 + frequency], duration,
                                           sample_rate)
    return binaural_beat


if __name__ == '__main__':
    export_binaural_beat()