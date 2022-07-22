import pandas as pd
pd.set_option('display.max_colwidth', -1)

df = pd.read_csv('jeopardy.csv')
print(df.head())

def count_rows(words, col):
  ct = 0
  for row in col:
    for word in words:
      if word in row:
        ct += 1
  return ct

ls = ["King", "England"]
count = count_rows(ls, df[' Question'])
print(count)

def clean(string):
  string = string.replace('$', '')
  string = string.replace(',', '')
  return string

def ave_val(col):
  ct = 0
  tot = 0
  for row in col:
    if row == "None":
      continue
    num = float(clean(row))
    tot += num
    ct += 1
  ave = tot / ct
  return ave

mean = ave_val(df[' Value'])
print(mean)

def unique_ans(words, col):
  ct = 0
  dt = {'num unique': 0}
  for row in col:
    for word in words:
      if word in row:
        dt['num unique'] += 1
        if row not in dt:
          dt[row] = 1
        else:
          dt[row] += 1
  return dt

ls = ["King"]
print(unique_ans(ls, df[' Answer']))
