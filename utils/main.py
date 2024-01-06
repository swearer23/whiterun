import numpy as np
from scipy.stats import norm

def get_sample(mean: float, deviation: float):
  scale = (mean * deviation) / 0.6745
  distribution = norm(loc=mean, scale=scale)
  return distribution.rvs(size=1)[0]
