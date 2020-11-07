# https://github.com/alisoltanirad/Binaural_Beats
import argparse
import numpy as np
from scipy.io import wavfile

def generate_beat(parameters):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-l',
        '--left',
        type=int,
        default=110,
        help='left channel frequency'
    )
    parser.add_argument(
        '-r',
        '--right',
        type=int,
        default=120,
        help='right channel frequency'
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
        '--output-file-name',
        type=str,
        default='binaural_beat.wav',
        help='name of the output file (must end with .wav)'
    )

    arguments = parser.parse_args()

    generate_beat(vars(arguments))