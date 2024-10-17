import pandas as pd
import numpy as np

def introduce_filthy_data(df, null_chance=0.01, outlier_chance=0.01, duplicate_chance=0.01):
    # Create a copy of the DataFrame to avoid modifying the original
    df_filthy = df.copy()

    for idx in df_filthy.index:
        # Randomly choose the type of filthy data to introduce based on given chances
        rand_val = np.random.rand()
        if rand_val < null_chance:
            # Introduce a missing value
            col = np.random.choice(df_filthy.columns)
            df_filthy.at[idx, col] = np.nan
        elif rand_val < null_chance + outlier_chance:
            # Introduce an outlier
            col = np.random.choice(df_filthy.select_dtypes(include=[np.number]).columns)
            df_filthy.at[idx, col] = df_filthy[col].mean() + 10 * df_filthy[col].std()
        elif rand_val < null_chance + outlier_chance + duplicate_chance:
            # Introduce a duplicate row
            duplicate_row = df_filthy.loc[idx]
            df_filthy = pd.concat([df_filthy, pd.DataFrame([duplicate_row])], ignore_index=True)

    return df_filthy