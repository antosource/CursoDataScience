#Funciones

#get_descriptives()
def get_descriptives(df, columnas_obj):
    for k, v in df.iteritems():
        if k in columnas_obj:
            print(k)
            print(v.describe())
            print('-'*100)

#get_null_cases()
def get_null_cases(df, var, print_list=False):
    tmp = df.copy()
    tmp['flagnull'] = tmp[var].isnull()
    cont_na = 0
    for i, r in tmp.iterrows():
        if r['flagnull'] == True:
            cont_na+=1
            if print_list==True:
                print(r['cname'])
    print ('Casos nulos para {}: {:.4f}'.format(var,cont_na))
    print('Porcentaje nulos para {}: {:.4f}'.format(var,cont_na/df.shape[0]))