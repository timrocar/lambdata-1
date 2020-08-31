def date_split(df, col):
    df[col+'_month'] = list(df[col].dt.month)
    df[col+'_day'] = list(df[col].dt.day)
    df[col+'_year'] = list(df[col].dt.year)