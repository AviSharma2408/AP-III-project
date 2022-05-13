import time
startTime = time.time()

import numpy as np
from PROJECT_part1 import kahlil, kahlil_unique, conditional

P = []

for i in range(len(kahlil_unique)):
    p = [conditional(kahlil,kahlil_unique[i],kahlil_unique[j]) for j in range(len(kahlil_unique))]
    p = np.array(p)
    p = p.transpose()
    P.append(p)
    
    
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))

