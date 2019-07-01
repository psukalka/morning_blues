from memory_profiler import memory_usage
from utils.matrix import create_seq_matrix

output = memory_usage((create_seq_matrix, (5,), {}), interval=.1, timeout=1)
print(output)
print(len(output))
