import time
from pathlib import Path
import constants
from typing import List
from utils import fetch

class Cache:
    def __init__(self, filename):
        self.data = {}
        self.filename = filename
        file = Path(filename)
        file.touch(exist_ok=True)
        
        file = open(filename, "r")
        for line in file.readlines():
            [city, temperature, timestamp] = line.split(' ')
            self.data[city] = {
                'temperature': float(temperature),
                'timestamp': int(timestamp),
                }

    
    def consult(self, city):
        current_timestamp = int(time.time())

        # Value in cache is valid, no need to fetch the information
        if city in self.data and current_timestamp - self.data[city]['timestamp'] < 60:
            # Update the timestamp
            self.data[city]['timestamp'] = current_timestamp
            return self.data[city]['temperature']

        # We need to fetch the data
        temperature = fetch(city)
        
        # Value is in cache but is invalid or cache is not full
        if city in self.data or len(self.data) < CACHE_SIZE:
            self.data[city] = {
                'temperature': temperature,
                'timestamp': current_timestamp
            }
        # Cache is full and city is not in the cache -> replace oldest one
        else:
            # First element
            to_remove = next(iter(self.data))

            # Iterate over all elements
            for key in self.data:
                if self.data[key]['timestamp'] < self.data[to_remove]['timestamp']:
                    to_remove = key

            # Make space for new element
            del self.data[to_remove]

            self.data[city] = {
                'temperature': temperature,
                'timestamp': current_timestamp
            }

        return self.data[city]['temperature']

    def store(self):
        f = open(self.filename, "w")
        for city in self.data:
            f.write(f"{city} {self.data[city]['temperature']} {self.data[city]['timestamp']}\n")