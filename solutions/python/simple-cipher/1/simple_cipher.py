import re
import random

class Cipher:
    def __init__(self, key=None):
        self.key = key or self._generate_random_key()

    def encode(self, text):
        result = ""
        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord(self.key[i % len(self.key)].lower()) - ord('a')
                result += chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += char
        return result

    def decode(self, text):
        result = ""
        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord(self.key[i % len(self.key)].lower()) - ord('a')
                result += chr((ord(char.lower()) - ord('a') - shift) % 26 + ord('a'))
            else:
                result += char
        return result

    def _generate_random_key(self):
        return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(500))