import pandas as pd
import numpy as np
from scipy import stats
chat_id = 401141478

def solution(rvs1, rvs2) -> bool:
    sl = 0.09
    t, pval = stats.ttest_ind(rvs1, rvs2, equal_var=False)
    return pval < sl
