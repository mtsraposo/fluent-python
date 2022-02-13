# <<< Step or Stride >>>
s = 'bicycle'
print(s[::3],
      s[::-1],
      s[::-2])

# <<< Named Slices >>>
invoice = "0.....6.................................40........52...55........"
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
print(invoice[SKU],
      invoice[DESCRIPTION])

# Ellipsis
import numpy as np
import pandas as pd

arr = np.transpose(np.array([[1, 2, 3, 4],
                             [5, 6, 7, 8]]))
df = pd.DataFrame(columns=arr[..., 0],
                  index=pd.MultiIndex.from_arrays(arr))
print(df.loc[5, ...])

