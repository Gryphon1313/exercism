import random
import string
from datetime import datetime

class Robot:
    def __init__(self):
        self.name = self.generate_name()
    
    def generate_name(self):
        random.seed(datetime.now().timestamp())
        
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        digits = ''.join(random.choices(string.digits, k=3))
        
        return letters + digits

    def reset(self):
        self.name = self.generate_name()