def cont_chi2(col1, col2):
  contingency = pd.crosstab(col1, col2)
  print(contingency)
  chi2, p_value, dof, expected = stats.chi2_contingency(contingency)
  print("chi2 statistic", chi2)
  print("p value", p_value)
  print("degrees of freedom",dof)
  print("expected frequencies table \n", expected)

def date_split(df, col):
    df[col+'_month'] = list(df[col].dt.month)
    df[col+'_day'] = list(df[col].dt.day)
    df[col+'_year'] = list(df[col].dt.year)

def wrangle(X, hc=100):
  #copy X
  X = X.copy()

  #drop constant columns
  X = X.drop([col for col in X if X[col].nunique()==1], axis=1)

  #drop high cardinality columns
  hc = [col for col in X.describe(include='object').columns if X[col].nunique() > card]
  X = X.drop(hc, axis=1)

  #return new version 
  return X