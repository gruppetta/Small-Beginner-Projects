'''
Code used for avocado data analysis 
'''

def filtering():
    con_type = input('Do you want organic or conventional')
    con_region = input('What region do you want to check?')
    con_year = input('What year?')
    print(
        df[df['type']==con_type]
    )