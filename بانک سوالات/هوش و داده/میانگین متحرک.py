import numpy as np
def moving_average(data_list, window_size):
  """Calculating Moving Average from a list of numbers

  Args:
      data_list (np array): list of the data
      window_size (int): size of the window
  """
  mov_avg = np.empty([len(data_list) - window_size + 1], dtype=float)
  for i in range(len(mov_avg)):
    mov_avg[i] = sum([data_list[j] for j in range(i, i+window_size)]) / window_size
  return np.around(mov_avg, decimals=2)
