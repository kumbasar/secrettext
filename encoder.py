#!/usr/bin/env python

import base64
import string
import argparse

alphabets = (string.ascii_lowercase, string.ascii_uppercase)
caesar_shift = 7
PLAIN_STRING = "Hello World!! 1 2 9"

parser = argparse.ArgumentParser(description='My example explanation')
parser.add_argument(
    '--shift',
    type=int,
    default=7,
    help='set ceaser chiper shift value (default: ' + str(caesar_shift) + ')'
)
encoder_parm = parser.parse_args()

caesar_shift = encoder_parm.shift

print("Caesar Shift value: " + str(encoder_parm.shift))


def caesar(text, step, alphabets):

    def shift(alphabet):
        return alphabet[step:] + alphabet[:step]

    shifted_alphabets = tuple(map(shift, alphabets))
    joined_aphabets = ''.join(alphabets)
    joined_shifted_alphabets = ''.join(shifted_alphabets)
    table = string.maketrans(joined_aphabets, joined_shifted_alphabets)
    return text.translate(table)

print("PLAIN_STRING:" + PLAIN_STRING)

# Cesar Cipher
CAESAR_STRING = caesar( PLAIN_STRING , caesar_shift , alphabets=alphabets)
print("CAESAR_STRING:" + CAESAR_STRING)


encodedBytes = base64.b64encode(CAESAR_STRING.encode("utf-8"))
BASE64_STRING = str(encodedBytes)

print("BASE64_STRING:" + BASE64_STRING)

BINARY_STRING = ' '.join(format(x, 'b') for x in bytearray(BASE64_STRING))

print("BINARY_STRING:" + BINARY_STRING)
