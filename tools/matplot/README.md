# Compare error rates of 2 models at different epochs
```
import pandas as pd
print("Compare validation CER of MTL and EZC")

val_cer = dict()
val_cer['mtl'] = [46.15, 33.96, 29.81, 27.09, 25.18, 17.52]
val_cer['ezc'] = [41.98, 32.53, 29.43, 27.27, 25.42, 17.34]

df_val_cer = pd.DataFrame(val_cer)

import seaborn as sns
sns.lineplot(data=df_val_cer)
```
