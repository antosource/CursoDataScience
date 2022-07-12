### Para modelos de regresion lineal

#### Metodos de regularización
Formas de penalizar,  para evitar que el modelo se ajuste demasiado a la data.
Se aplican con libreria <code>sklearn</code>

#### L1 Lasso (es mas una recta)
- Separa variables (atributos) manteniendo las importante y llevando las otras a cero

#### L2 Ridgge  (es como una curva)
- Entrega valores atenuados

#### L1+L2 = Elastic Net (usa ambas normas) 

- Penaliza con norma 1 y norma 2 (separa y luego atenua)

#### Cosas de interes:

underfitting : Modelo que se no explica bien con los datos. 

overfitting : Modelo que explica tanto la data que no funciona bien con nuevos datos. (Se debe buscar mas data, no variables)

ver libreria <code>gridsearchcv</code>