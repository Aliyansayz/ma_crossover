def ema (self, array, period ):
    import numpy as np

    ema = np.empty_like(array)
    ema = np.full( ema.shape , np.nan)
    ema[0] = np.mean(array[0] , dtype=np.float32)
    alpha = 2 / (period + 1)

    for i in range(1 , len(array) ):
          ema[i] = np.array( (array[i] * alpha +  ema[i-1]  * (1-alpha) ) , dtype=np.float32 )
    
    return ema 

def ma_crossover( lower, higher, index ):

    close = self.close 
    check = np.zeros(len(close))  # Initialize an empty signal array
    large_ema = self.ema(lower)
    small_ema = self.ema(higher)
    limit = 7
    for length in range(1, limit+1): 

        if  close[index - length] < large_ema[index - length] and close[index - length] < small_ema[index - length] and close[index] > large_ema[index] and close[index] > small_ema[index]  :
            check[index] = 1  # Set the signal value to 1 for the corresponding index
            break
        elif close[index - length] > large_ema[index - length] and close[index - length] > small_ema[index - length] and close[index] < large_ema[index] and small_ema[index] < close[index] :
            check[index] = -1  # Set the signal value to -1 for the corresponding index
            break

    return check 
