import numpy as np
import pandas as pd
celsius = np.array([0, 20, 30, 40])
fahrenheit = (celsius * 9/5) + 32
df = pd.DataFrame({
    "Celsius": celsius,
    "Fahrenheit": fahrenheit
})
print(df)