import time
import hashlib


class Block():

    timestamp = time.time()

    def __init__(self, data, previousHash=""):
        self.data = data
        self.previousHash = previousHash
        self.thisBlockHash = self.computeHash()

    def computeHash(self):
        hash_string = f'{self.previousHash} {self.timestamp} {self.data}'
        self.thisBlockHash = hashlib.sha256(hash_string.encode()).hexdigest()

    def checkHash(self):
        hash_string = f'{self.previousHash} {self.timestamp} {self.data}'
        return hashlib.sha256(hash_string.encode()).hexdigest()
