import numpy as np
import networkx as networkx
import dimod
import dwave_networkx as dnx

from dimod.binary_quadratic_model import BinaryQuadraticModel
from dwave.system.composites import EmbeddingComposite

import matplotlib.pyplot as plt
# magic word for producing visulizations in notebook
#%matplotlib inline
from collections import defaultdict
import itertools
import pandas as pd

from dwave.system.samplers import DWaveSampler

