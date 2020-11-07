# https://github.com/alisoltanirad/Binaural_Beats
# try "python binaural_beat.py -h" in your command-line
import argparse
import numpy as np
from scipy.io import wavfile


def main():
    arguments = parse_arguments()
    export_binaural_beat(vars(arguments))


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Create and save a binaural beat file'
    )

    parser.add_argument(
        '-l',
        '--left',
        type=int,
        default=420,
        help='left channel frequency (Hz)'
    )
    parser.add_argument(
        '-r',
        '--right',
        type=int,
        default=440,
        help='right channel frequency (Hz)'
    )
    parser.add_argument(
        '-d',
        '--duration',
        type=int,
        default=10,
        help='beat duration (seconds)'
    )
    parser.add_argument(
        '-o',
        '--output_file_name',
        type=str,
        default='binaural_beat.wav',
        help='name of the output file (must end with .wav)'
    )

    arguments = parser.parse_args()
    return arguments


def export_binaural_beat(parameters):
    file_name = parameters['output_file_name']
    sample_rate = 44100
    frequencies = [parameters['left'], parameters['right']]
    duration = parameters['duration']
    beat = generate_binaural_beat(frequencies, duration)

    wavfile.write(file_name, sample_rate, beat)

    print("""* Binaural beat created:
    - file name: {}
    - duration: {} s
    - binaural beat frequency (difference between frequencies): {} Hz
    - left channel frequency: {} Hz
    - right channel frequency: {} Hz
    """.format(file_name, duration, abs(frequencies[0]-frequencies[1]),
               frequencies[0], frequencies[1]))


def generate_binaural_beat(frequencies, duration):
    left_signal = generate_sine_wave(frequencies[0], duration)
    right_signal = generate_sine_wave(frequencies[1], duration)
    binaural_beat = np.array([left_signal, right_signal]).T
    return binaural_beat


def generate_sine_wave(frequency, duration):
    sample_rate = 44100
    max_amplitude = np.iinfo(np.int16).max
    samples = np.linspace(0, duration, int(sample_rate * duration),
                           endpoint=False)
    signal = (np.sin(2 * np.pi * frequency * samples)
              * max_amplitude).astype(np.int16)
    return signal


if __name__ == '__main__':
    main()