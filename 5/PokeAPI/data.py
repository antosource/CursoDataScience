#Plantilla HTML modificada
from string import Template

validacion_pokemon = 'Por favor ingrese nombre válido de algún pokemon: '
validacion_opcion = 'Por favor ingrese una opción valida: '

mensaje_opcion = '''Bienvenidos a la Poke-APP
    ¿Que deseas conocer del mundo Pokemon?
    
    1. Pokedex
    2. Cadena de Evolución
    0. Salir
    > '''

mensaje_pokedex = '''Ingrese el Nombre de un Pokemon para verlo en el Pokedex
Nota: Si el Pokemon tiene espacios reemplace por "-".
No coloque ningún tipo de signo de puntuación adicional.
Ejemplo: Mr. Mime, se debe ingresar como Mr-Mime o mr-mime
>'''

stats_es = {'hp': 'HP',
            'attack': 'Ataque',
            'defense': 'Defensa',
            'special-attack' : 'Ataque Especial',                      
            'special-defense' : 'Def. Especial',
            'speed' : 'Velocidad'} 

tipo_es = {'fire': 'Fuego',
           'flying': 'Volador',
           'electric':'Eléctrico',
           'water': 'Agua',
           'ground': 'Tierra',
           'steel': 'Metal',
           'ice': 'Hielo',
           'bug': 'Insecto',
           'dragon': 'Dragón',
           'ghost' : 'Fantasma',
           'fairy': 'Hada',
           'fighting': 'Luchador',
           'normal': 'Normal',
           'grass': 'Planta',
           'psychic': 'Psiquico',
           'rock': 'Roca',
           'dark': 'Siniestro',
           'poison': 'Veneno',
           'baby':'Bebé',
           'legendary': 'Legendario',
           'mythical': 'Mitico'    
           }                                 

document_template = Template(''' <!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="mystyle.css">
    </head>
<body>

$body

</body>
</html>
''')

single_card = Template('''<div class="column2">
    <div class="card">
    <h1>#$id $name</h1>
        <img src="$url" width="150" height="150">
    <div class="container">

      $etapa_previa

        <h2>Estadísticas</h2>
        <table>
            <tr>
               $table
            </tr>
        </table>
        <h3><b>Tipo</b></h3> 
            $tipos
            $tipo_especial
            
        <p>$description</p>
        
    <h3>Super efectivo contra:</h3>
        $super_ef
    <h3>Débil contra:</h3>
        $debil
    <h3>Resistente contra:</h3>
        $resistente
    <h3>Poco Eficaz contra</h3>
        $poco_ef
    <h3>Inmune contra:</h3>
        $inmune
    <h3>Ineficaz contra:</h3>
        $inef
    
    </div>
    </div>

''')
