# Usage

```bash
kumbasar@ghost ~/g/secrettext> ./encoder.py --help
usage: encoder.py [-h] [--shift SHIFT] plain_string

Encoder Help.

positional arguments:
  plain_string   Input plain text. Example: 'Hello World! 1 2 3'

optional arguments:
  -h, --help     show this help message and exit
  --shift SHIFT  set ceaser chiper shift value (default: 7)
kumbasar@ghost ~/g/secrettext> 
```

# Example

```bash
kumbasar@ghost ~/g/secrettext> ./encoder.py --shift 3 'Hello World!! 1 2 9'
Caesar Shift value: 3
Plain String: Hello World!! 1 2 9
Caesar Cipher String: Khoor Zruog!! 1 2 9
BASE64 String: S2hvb3IgWnJ1b2chISAxIDIgOQ==
Binary String: 1010011 110010 1101000 1110110 1100010 110011 1001001 1100111 1010111 1101110 1001010 110001 1100010 110010 1100011 1101000 1001001 1010011 1000001 1111000 1001001 1000100 1001001 1100111 1001111 1010001 111101 111101
kumbasar@ghost ~/g/secrettext> 
```