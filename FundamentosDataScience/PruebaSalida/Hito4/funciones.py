from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


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

option_yn = {'yes': 1, 'no': 0}


def mf(df, var_obj):
    """Genera la fórmula del modelo logit con todos sus atributos y variable objetivo.
    Args:
        df (dataframe): Conjunto de datos
        var_obj (string): variable objetivo
    Returns:
        string: formula total
    """
    base_formula = f'{var_obj} ~ '
    for col in df.columns:
        if col != var_obj:
            base_formula += f'{col} + '
    return base_formula[:-3]


def predict_(df, var_obj):
    """Función que automatiza las predicciones por LogisticRegression.

    Args:
        df (dataframe): dataframe con todas las variables a introducir en el modelo, incluida la V.O
        var_obj (str): variable objetivo

    Returns:
        array: vector de prueba y vector de predicciones
    """
      
    mat_atr = df.drop(var_obj, axis=1)                  # separando matriz de atributos de vector objetivo
    vec_obj = df[var_obj]                               # utilizamos dataframe con variables significativas
    X_train, X_test, y_train, y_test = train_test_split(mat_atr, vec_obj, test_size=.33, random_state=1238) # split de conjuntos de entrenamiento vs prueba
    X_train_std = StandardScaler().fit_transform(X_train) # estandarizamos conjunto de entrenamiento
    X_test_std = StandardScaler().fit_transform(X_test) # ajustamos modelo sin alterar hiperparámetros
    modelo_x =  LogisticRegression().fit(X_train_std, y_train)
    y_hat = modelo_x.predict(X_test_std) # prediccion de clases y probabilidad
    
    return modelo_x, y_test, y_hat