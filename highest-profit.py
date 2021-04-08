import pandas as pd

# suppress SettingWithCopy warning
pd.options.mode.chained_assignment = None

df = pd.read_csv('data.csv')

print('Number of rows:',len(df))

profit_feat = df.columns.values[-1]

def is_float(x):
    try:
        float(x)
    except ValueError:
        return False
    return True

filtered_df = df[df[profit_feat].apply(lambda x: is_float(x))]
print('\nNumber of rows with only numeric profit:', len(filtered_df))

filtered_df[profit_feat] = filtered_df[profit_feat].astype(float)
filtered_df.to_json(orient='records',path_or_buf='data2.json')
sorted_df = filtered_df.sort_values(by=profit_feat, ascending=False)
print('\nTop 20 rows with highest profit values:')
print(sorted_df[:20].to_string(index=False))
