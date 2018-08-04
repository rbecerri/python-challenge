import os
import re
import numpy as np

file = open("raw_data/paragraph_1.txt","r").read()
#file = open("raw_data/paragraph_2.txt","r").read()
#file = "Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident - a blot of black upon a world of crimson and gold."

words = re.split('\W* ', file)

sentences = re.split("(?<=[.!?]) +", file)

wordsInSentences = [len(re.split('\W* ', x)) for x in sentences]

print("Paragraph Analysis")
print("-----------------")
print("Approximate Word Count: " + str(len(words)))
print("Approximate Sentence Count: " + str(len(sentences)))
print("Average Letter Count: " + str(np.mean([len(x) for x in words])))
print("Average Sentence Length: " + str(np.mean(wordsInSentences)))