import math
import random
import numpy as np
from io import StringIO
import random

import numpy as np

def accept_prob(S_old, S_new, T):

    if S_new > S_old:
        prob =  1.0
    else:
        prob = np.exp(-(S_old-S_new)/T)
    return prob

# the above function will be used as follows. this is shown just for
# your information; you don't have to change anything here
def accept(S_old, S_new, T):
    rand = random.random()
    if rand < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)

print(accept_prob(150, 140, 10))
  