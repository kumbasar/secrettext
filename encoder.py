#!/usr/bin/env python3

import base64
import string
import argparse

caesar_shift = 7

parser = argparse.ArgumentParser(description='Encoder Help.')
parser.add_argument(
    '--shift',
    type=int,
    default=7,
    help='set ceaser chiper shift value (default: ' + str(caesar_shift) + ')'
)
parser.add_argument('input', type=str, help='Input plain text. Example: \'Hello World! 1 2 3\'')

encoder_parm = parser.parse_args()

caesar_shift = encoder_parm.shift
plain_string = encoder_parm.input

print("Caesar Shift value: " + str(encoder_parm.shift))
print("Plain String: " + plain_string)

def caesar(text, step):

    alphabets = (string.ascii_lowercase, string.ascii_uppercase)

    def shift(alphabet):
        return alphabet[step:] + alphabet[:step]

    shifted_alphabets = tuple(map(shift, alphabets))
    joined_aphabets = ''.join(alphabets)
    joined_shifted_alphabets = ''.join(shifted_alphabets)
    table = str.maketrans(joined_aphabets, joined_shifted_alphabets)
    return text.translate(table)

# Cesar Cipher
CAESAR_STRING = caesar(plain_string , caesar_shift)
print("Caesar Cipher String: " + CAESAR_STRING)

# Bas64
encodedBytes = base64.b64encode(CAESAR_STRING.encode("utf-8"))
BASE64_STRING = str(encodedBytes)
print("BASE64 String: " + BASE64_STRING)

# Binary
BINARY_STRING = ' '.join(format(x, 'b') for x in bytearray(BASE64_STRING,'utf8'))
print("Binary String: " + BINARY_STRING)
