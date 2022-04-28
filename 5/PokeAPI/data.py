from string import Template
validacion_pokemon = 'Por favor ingrese nombre valido de algún pokemon : '

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

single_card = '''<div class="column2">
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

'''
