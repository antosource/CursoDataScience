font = {'family': 'serif',
        'color':  'red',
        'weight': 'normal',
        'size': 12,
        }
        
# Diccionarios
rename = {
    'occupation': 'collars',
    'workclass': 'workclass_recod',
    'education': 'educ_recod',
    'marital-status': 'civstatus',
    'native-country': 'region'
}

occupation = {
    'Prof-specialty': 'white-collar', 
    'Exec-managerial': 'white-collar', 
    'Adm-clerical': 'white-collar', 
    'Sales': 'white-collar', 
    'Tech-support': 'white-collar',
    'Craft-repair': 'blue-collar', 
    'Machine-op-inspct': 'blue-collar', 
    'Transport-moving': 'blue-collar', 
    'Handlers-cleaners': 'blue-collar', 
    'Farming-fishing': 'blue-collar', 
    'Protective-serv': 'blue-collar', 
    'Priv-house-serv': 'blue-collar',
    'Other-service': 'others',
    'Armed-Forces': 'others'
}

workclass = {
    'Federal-gov': 'federal-gov',
    'State-gov': 'state-level-gov', 
    'Local-gov': 'state-level-gov',
    'Self-emp-inc': 'self-employed', 
    'Self-emp-not-inc': 'self-employed',
    'Never-worked': 'unemployed', 
    'Without-pay': 'unemployed',
    'Private': 'private'
}

education = {
    'Preschool': 'preschool',
    '1st-4th': 'elementary-school', 
    '5th-6th': 'elementary-school',
    '7th-8th': 'high-school', 
    '9th': 'high-school',
    '10th': 'high-school',
    '11th': 'high-school',
    '12th': 'high-school',
    'HS-grad': 'high-school',
    'Assoc-voc': 'college', 
    'Assoc-acdm': 'college', 
    'Some-college': 'college',
    'Bachelors': 'university', 
    'Masters': 'university',  
    'Prof-school': 'university', 
    'Doctorate': 'university'
}

marital = {
    'Married-civ-spouse': 'married', 
    'Married-spouse-absent': 'married',
    'Married-AF-spouse': 'married',
    'Divorced': 'divorced',
    'Separated': 'separated',
    'Widowed': 'widowed',
    'Never-married': 'never-married'
}

native_country = {
    'United-States': 'America', 
    '?': 'Unknown',
    'Peru': 'America',
    'Guatemala': 'America', 
    'Mexico': 'America',
    'Dominican-Republic': 'America',
    'Ireland': 'Europe',
    'Germany': 'Europe',
    'Philippines': 'Asia',
    'Thailand': 'Asia',
    'Haiti': 'America',
    'El-Salvador': 'America', 
    'Puerto-Rico': 'America',
    'Vietnam': 'Asia',
    'South': 'Unknown',
    'Columbia': 'America',
    'Japan': 'Asia',
    'India': 'Asia',
    'Cambodia': 'Asia',
    'Poland': 'Europe',
    'Laos': 'Asia',
    'England': 'Europe',
    'Cuba': 'America',
    'Taiwan': 'Asia',
    'Italy': 'Europe',
    'Canada': 'America',
    'Portugal': 'Europe',
    'China': 'Asia',
    'Nicaragua': 'America', 
    'Honduras': 'America',
    'Iran': 'Asia',
    'Scotland': 'Europe', 
    'Jamaica': 'America',
    'Ecuador': 'America',
    'Yugoslavia': 'Europe',
    'Hungary': 'Europe',
    'Hong': 'Asia',
    'Greece': 'Europe',
    'Trinadad&Tobago': 'America',
    'Outlying-US(Guam-USVI-etc)': 'Unknown',
    'France': 'Europe',
    'Holand-Netherlands': 'Europe'
}