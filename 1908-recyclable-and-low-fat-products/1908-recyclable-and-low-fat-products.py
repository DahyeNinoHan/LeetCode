import pandas as pd

Products = pd.DataFrame ({
    'product_id': [0,1,2,3,4],
    'low_fats': ['Y','Y','N','Y','N'],
    'recyclable': ['N','Y','Y','Y','N']
})

def find_products(products):
    result = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return result[['product_id']]

a = find_products(Products)
print(a)