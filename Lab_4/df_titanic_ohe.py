import pandas as pd

from sklearn.preprocessing import OneHotEncoder

df_titanic = pd.read_csv(filepath_or_buffer='datasets/df_titanic.csv', sep=',')

encoder = OneHotEncoder(drop='if_binary', sparse_output=False)

sex_encoded = encoder.fit_transform(df_titanic[['Sex']])

sex_encoded_df = pd.DataFrame(sex_encoded, columns=encoder.get_feature_names_out(['Sex'])).astype(int)

df_titanic = pd.concat([df_titanic.drop(columns=['Sex']), sex_encoded_df], axis=1)

df_titanic.to_csv('datasets/df_titanic.csv', index=False)


