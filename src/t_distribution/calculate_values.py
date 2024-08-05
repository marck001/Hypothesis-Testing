import numpy as np
from scipy import stats

def calculate_t_value(x_bar, mean_0, deviation, size):
    
    t_value = (x_bar - mean_0) / (deviation/ np.sqrt(size))
    
    return t_value
    
    
def calculate_p_value(size, t_value):
    
    df = size - 1  
    p_value = 2 * (1 - stats.t.cdf(abs(t_value), df))
    
    return p_value, df