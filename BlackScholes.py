import numpy as np
from scipy.stats import norm
from numpy import log, sqrt, exp  

def black_scholes_call(s, x, sigma, r, t):
    d1 = (log(s/x) + (r + (sigma**2)/2) * t ) / (sigma * sqrt(t))
    d2 = d1 - (sigma * sqrt(t))
    call = s * norm.cdf(d1) - x * exp(-r*t) * norm.cdf(d2)
    return call

print(black_scholes_call(100, 100, 0.3, 0.05, 1))