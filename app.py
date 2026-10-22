from flask import Flask, render_template, request, json, jsonify

app= Flask(__name__)


@app.route('/API/productos', methods=['GET'])
def mostrar_tabla():
    elementos= json.load(open('API.json'))
    for clave, valor in elementos.items():
        if "status" not in valor:
            valor["status"] = "online"
    return render_template('API/tabla.html', elementos=elementos)

@app.route('/send', methods=['GET','POST'])
def nuevo():
    nombre_usuario =request.form.get ('nombre')
    correo_usuario =request.form.get ('correo')
    titulo_pagina= "EstaNoEsEstafas.com"

    return render_template ('response.html',titulo=titulo_pagina, 
        nombre_usuario=nombre_usuario, correo_usuario=correo_usuario)
#Titulo es la variable que se ocuoa en el html linea 4 
#titulo_pagina es la variable que se crea en python linea 10
#La igualacion quiere decir que se crea el valor de titulo pagina lo agrega en titulo y lo pasa al html para que se muestre en la pagina web

#####################
#VARIABLES GLOBALES

name= "Carlos Cortez"             
age= 23
activuser= False
variable1= "<div><h1>Esta es una variable que se pasa desde Python al HTML</h1></div>"

def personalInfoDetails(name, age, activuser):
    return{
        "name": name,
        "age": age,
        "active": activuser
    }


@app.route('/', methods=['GET'])
def manejar_formulario():
    ############################################################################################
    """#Variables que pasaremos desde Python al HTML
    titulo_pagina= "EstaNoEsEstafas.com"

    mensaje= None

    #Si el usuario envía el formulario (método POST)
    if request.method == 'POST':
        #Recibimos los parametros usando el atributo 'name'  del HTML
        nombre_usuario=request.form.get ('nombre')
        correo_usuario=request.form.get ('correo')

        #mensaje para mostrar el resultado en la pantalla
        mensaje = f"!Datos Recibidos! Hola {nombre_usuario}, Tu correo es: {correo_usuario}"
    
    #Pasamos las variables dentro de rednder_template para que sean accesibles desde el HTML
    """
    #####################################################################################################3####
    
    personal_info= personalInfoDetails(name, age, activuser) 
    
    return render_template ('personalDetails.html', variable1=variable1, 
                            personal_info = personal_info,q)



if __name__=='__main__':
    app.run(debug=True)