# Jupyter
### Autoreload:

```
%load_ext autoreload
%autoreload 2
```


### Standard Imports:

```
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('https://raw.githubusercontent.com/RobGeada/stylelibs/main/material.mplstyle')

%load_ext autoreload
%autoreload 2
```

# Python
## Matplotlib
```
plt.style.use('https://raw.githubusercontent.com/RobGeada/stylelibs/main/material_rh.mplstyle')
```
```
plt.style.use('https://raw.githubusercontent.com/RobGeada/stylelibs/main/material.mplstyle')
```
```
plt.style.use('https://raw.githubusercontent.com/RobGeada/stylelibs/main/material_white.mplstyle')
```

## General
### Colored printing:
```
bcolor_dict = {
    "PURPLE":   '\033[95m',
    "BLUE":     '\033[94m',
    "CYAN":     '\033[96m',
    "GREEN":    '\033[92m',
    "YELLOW":   '\033[93m',
    "RED":      '\033[91m',
    "ENDC":     '\033[0m',
    "BOLD":     '\033[1m',
    "UNDERLINE":'\033[4m'
} 
def bcolor(key, string):
    return bcolor_dict[key.upper()] + string + bcolor_dict['ENDC']
```

## Numpy

### Suppress scientific notation:
```
np.set_printoptions(suppress=True)
```
# Bash
### Print nth column
```
awk '{print $2}'
```
### Grep invert
```
grep -v 
```
