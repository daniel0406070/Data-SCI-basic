import numpy as np
import pandas as pd
from datascience import *
%matplotlib inline

path_data="/home/daniel/code_space/Data-SCI-basic/csv/"
united = Table.read_table(path_data + 'united_summer2015.csv')
united