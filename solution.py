import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 1066531890 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.02
    #count = np.array([x_success, y_success])
    #nobs = np.array([x_cnt, y_cnt])
    stat, pval = proportions_ztest(count=[x_success, y_success], 
                                   nobs=[x_cnt, y_cnt], alternative='larger')
    result = pval < alpha
    return result
