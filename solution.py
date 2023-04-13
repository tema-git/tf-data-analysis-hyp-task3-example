import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu
chat_id = 401141478

def solution(x: np.array, y: np.array) -> bool:
    sl = 0.09
    pval = mannwhitneyu(x, y, alternative="greater").pvalue
    
    return pval < sl
