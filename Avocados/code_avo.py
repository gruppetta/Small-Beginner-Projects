'''
Code used for avocado data analysis 
'''

def filtering():
    con_type = input('Do you want organic or conventional')
    con_region = input('What region do you want to check?')
    con_year = input('What year?')
    return df[df['type']==con_type& df['region']==con_region& df['year']== con_year]