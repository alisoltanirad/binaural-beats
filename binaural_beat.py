# https://github.com/alisoltanirad/Binaural_Beats
import argparse
import numpy as np
from scipy.io import wavfile

class BinauralBeat():

    def __init__(self, parameters=None):
        try:
            self.__set_variables(parameters)
        except TypeError:
            self.__set_variables(self.__get_default_variables())

        self.__beat = self.__generate_beat()


    def __set_variables(self, parameters):
        self.sample_rate = 44100
        self.file_name = parameters['output_file_name']
        self.duration = parameters['duration']
        self.frequency_left = parameters['left']
        self.frequency_right = parameters['right']
        self.bb_frequency = abs(self.frequency_left - self.frequency_right)


    def __get_default_variables(self):
        default_variables = {
            'output_file_name': 'binaural_beat.wav',
            'duration': 10,
            'left': 420,
            'right': 440
        }
        return default_variables


    def export(self):
        wavfile.write(self.file_name, self.sample_rate, self.__beat)

        print("""* Binaural beat created:
            - file name: {}
            - duration: {} s
            - binaural beat frequency (difference between frequencies): {} Hz
            - left channel frequency: {} Hz
            - right channel frequency: {} Hz
            """.format(
                self.file_name,
                self.duration,
                self.bb_frequency,
                self.frequency_left,
                self.frequency_right
            )
        )


    def __generate_beat(self):
        left = self.__generate_sine_wave(self.frequency_left)
        right = self.__generate_sine_wave(self.frequency_right)
        return np.array([left, right]).T

    def __generate_sine_wave(self, frequency):
        max_amplitude = np.iinfo(np.int16).max
        samples = np.linspace(
            0,
            self.duration,
            int(self.sample_rate * self.duration),
            endpoint=False
        )
        signal = (
            np.sin(2 * np.pi * frequency * samples) * max_amplitude
        ).astype(np.int16)
        return signal


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


if __name__ == '__main__':
    BinauralBeat(vars(parse_arguments())).export()