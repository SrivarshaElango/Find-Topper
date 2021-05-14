import pandas as pd
url = 'https://raw.githubusercontent.com/SrivarshaElango/Find-Topper/main/Student_marks_list.csv'
df = pd.read_csv(url, index_col=0)
print(df.head(5))
