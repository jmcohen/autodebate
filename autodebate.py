import random
import re
import urllib2
import pickle

class Corpus(object):    
    def __init__(self, filename):
        self.triples = {}
        file = open(filename)
        text = file.read()
        file.close()
        self.digestText(text)
        
    def digestText(self, text):
        words = text.split()
        for i in range(0, len(words) - 2):
            key = (words[i], words[i+1])
            next = words[i+2]
            if key in self.triples:
                self.triples[key].append(next)
            else:
                self.triples[key] = [next]
                
    def generate(self, seed, numSentences=5):
        sentenceCount = 0
        (a, b) = random.choice([key for key in self.triples.keys() if key[0] == seed]) 
        generatedText = [a, b]
        while sentenceCount < 5:
            options = self.triples[(a, b)]
            a, b = b, random.choice(options)
            generatedText.append(b)
            if b.endswith('.'):
                sentenceCount += 1
            
        return ' '.join(generatedText)