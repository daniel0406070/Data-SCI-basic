import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from datascience import *

#huck_finn_chapters get
try:
    huck_finn_url = 'https://www.inferentialthinking.com/data/huck_finn.txt'
    huck_finn_text = requests.get(huck_finn_url)
    #print("HTML:\n", huck_finn_text.text)
except:
    print("Invalid huck_finn_url or some error occured while making the GET request to the specified huck_finn_url")

huck_finn_chapters = huck_finn_text.text.split('CHAPTER ')[44:]

#little_women_chapters get
try:
    little_women_url = 'https://www.inferentialthinking.com/data/little_women.txt'
    little_women_text = requests.get(little_women_url)
    #print("HTML:\n", huck_finn_text.text)
except:
    print("Invalid little_women_url or some error occured while making the GET request to the specified little_women_url")

little_women_chapters = little_women_text.text.split('CHAPTER ')[1:]

ta