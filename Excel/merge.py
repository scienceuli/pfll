# merge.py

import pandas as pd

df_adressen = pd.read_excel("adressen.xlsx")
df_emails = pd.read_excel("emails.xlsx")

inner_join_df = df_adressen.merge(df_emails, how="inner", on="Name")
left_join_df = df_adressen.merge(df_emails, how="left", on="Name")
right_join_df = df_adressen.merge(df_emails, how="right", on="Name")


inner_join_df.to_excel("adressen_und_emails.xlsx")
left_join_df.to_excel("alle_adressen_und_emails.xlsx")
right_join_df.to_excel("adressen_und_alle_emails.xlsx")