import graphviz
import json

def mostrarAFND(automata):
    automataGrafico = graphviz.Digraph()
    for transicion in automata.transiciones:
        automataGrafico.edge(tail_name="q"+transicion.origen.nombre,head_name="q"+transicion.destino.nombre,label=transicion.simbolo)


    automataGrafico.node_attr['shape'] = 'circle'
    automataGrafico.node_attr['color'] = 'lightblue'
    automataGrafico.node_attr['size'] = '1.5'
    automataGrafico.edge_attr['width'] = '2.0'
    automataGrafico.view()

def graficarConJSon(automata):
    automataGrafico = graphviz.Digraph()

    for estado in automata.get('estados'):
        if estado.get('inicial') == True:
            automataGrafico.node(estado.get('nombre'), shape = 'circle', style = 'filled', fillcolor = 'green')
        if estado.get('final') == True:
            automataGrafico.node(estado.get('nombre'), shape = 'doublecircle')
        else:
            automataGrafico.node(estado.get('nombre'))


    for estado in automata.get('estados'):
        for transicion in estado.get('transiciones'):
            automataGrafico.edge(tail_name=estado.get('nombre'), head_name = transicion.get('a'), label = transicion.get('simbolo'))



    automataGrafico.node_attr['shape'] = 'circle'
    automataGrafico.node_attr['color'] = 'blue'
    automataGrafico.node_attr['size'] = '3.0'
    automataGrafico.edge_attr['width'] = '2.0'
    automataGrafico.view()

def Interseccion(automata1, automata2):
    automataGrafico = graphviz.Digraph()
    automataResultante = {
                "estados": [
                ]
            }
    estados = []
    for estado in automata1.get('estados'):
        for estado1 in automata2.get('estados'):
            if estado.get('inicial') == True and estado1.get('inicial') == True:
                if estado.get('final') == True and estado1.get('final') == True:
                    automataGrafico.node("{0}{1}".format(estado.get('nombre'),estado1.get('nombre')), style = 'filled', fillcolor = 'green', shape = 'doublecircle')
                    estados.append({"nombre": "{0}{1}".format(estado.get('nombre'),estado1.get('nombre')), "inicial": True, "final": True, "transiciones": []})
                else:
                    automataGrafico.node("{0}{1}".format(estado.get('nombre'),estado1.get('nombre')), shape = 'circle', style = 'filled', fillcolor = 'green')
                    estados.append({"nombre": "{0}{1}".format(estado.get('nombre'),estado1.get('nombre')), "inicial": True, "final": False, "transiciones": []})
            elif estado.get('final') == True and estado1.get('final') == True:
                automataGrafico.node("{0}{1}".format(estado.get('nombre'),estado1.get('nombre')), shape = 'doublecircle')
                estados.append({"nombre": "{0}{1}".format(estado.get('nombre'),estado1.get('nombre')), "inicial": False, "final": True, "transiciones": []})
            else:
                automataGrafico.node("{0}{1}".format(estado.get('nombre'),estado1.get('nombre')))
                estados.append({"nombre": "{0}{1}".format(estado.get('nombre'),estado1.get('nombre')), "inicial": False, "final": False, "transiciones": []})




    for estado in automata1.get('estados'):
        for estado1 in automata2.get('estados'):
            for transicion in estado.get('transiciones'):
                for transicion1 in estado1.get('transiciones'):
                    if transicion.get('simbolo') == transicion1.get('simbolo'):
                        automataGrafico.edge(tail_name="{0}{1}".format(estado.get('nombre'),estado1.get('nombre')), head_name="{0}{1}".format(transicion.get('a'),transicion1.get('a')), label=transicion.get('simbolo'))
                        for estado2 in estados:
                            if estado2.get('nombre') == "{0}{1}".format(estado.get('nombre'),estado1.get('nombre')):
                                estado2.get('transiciones').append({"a": "{0}{1}".format(transicion.get('a'),transicion1.get('a')), "simbolo": transicion.get('simbolo')})

    automataGrafico.node_attr['shape'] = 'circle'
    automataGrafico.node_attr['color'] = 'blue'
    automataGrafico.node_attr['size'] = '3.0'
    automataGrafico.edge_attr['width'] = '2.0'
    automataGrafico.view()
    automataResultante["estados"] = estados
    # Nombre del archivo JSON a crear
    nombre_archivo = 'AutómataResultante.json'
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(automataResultante, archivo, ensure_ascii=False, indent=4)
    return automataGrafico


def Inverso(automata):
    automataResultante = {
                "estados": [
                ]
            }
    estados = []
    automataGrafico = graphviz.Digraph()
    finales=[]
    finaleInicial = False

    for estado in automata.get('estados'):
        if estado.get('inicial') == True:
            if estado.get('final') == True:
                finales.append(estado.get('nombre'))
                contadorFinales = 0
                for estado1 in automata.get('estados'):
                    if estado1.get('final') == True:
                        contadorFinales += 1
                if contadorFinales > 1:
                    automataGrafico.node("NuevoInicial", shape = 'circle', style = 'filled', fillcolor = 'green')
                    estados.append({"nombre": "NuevoInicial", "inicial": True, "final": False, "transiciones": []})
                    #Agregar la transicion
                    for estado1 in estados:
                        if estado1.get('nombre') == "NuevoInicial":
                            estado1.get('transiciones').append({"a": estado.get('nombre'), "simbolo": "λ"})
                else:
                    finaleInicial = True


            automataGrafico.node(estado.get('nombre'), shape = 'doublecircle')
            estados.append({"nombre": estado.get('nombre'), "inicial": False, "final": True, "transiciones": []})
        elif estado.get('final') == True:
            finales.append(estado.get('nombre'))
        else:
            automataGrafico.node(estado.get('nombre'))
            estados.append({"nombre": estado.get('nombre'), "inicial": False, "final": False, "transiciones": []})

    if len(finales) == 1:
        if finaleInicial == True:
            automataGrafico.node(finales[0], shape = 'doublecircle', style = 'filled', fillcolor = 'green')
            estados.append({"nombre": finales[0], "inicial": True, "final": False, "transiciones": []})
        else:
            automataGrafico.node(finales[0], shape = 'circle', style = 'filled', fillcolor = 'green')
            estados.append({"nombre": finales[0], "inicial": True, "final": False, "transiciones": []})
    else:
        existe = False
        for estado in estados:
            if estado.get('nombre') == "NuevoInicial":
                existe = True
        if existe == False:
            estados.append({"nombre": "NuevoInicial", "inicial": True, "final": False, "transiciones": []})
            automataGrafico.node("NuevoInicial", shape = 'circle', style = 'filled', fillcolor = 'green')
        for final in finales:
            automataGrafico.edge(tail_name="NuevoInicial", head_name=final, label="λ")
            for estado in estados:
                if estado.get('nombre') == "NuevoInicial":
                    estado.get('transiciones').append({"a": final, "simbolo": "λ"})

    for estado in automata.get('estados'):
        for transicion in estado.get('transiciones'):
            automataGrafico.edge(tail_name=transicion.get('a'), head_name = estado.get('nombre'), label = transicion.get('simbolo'))
            for estado1 in estados:
                if estado1.get('nombre') == transicion.get('a'):
                    estado1.get('transiciones').append({"a": estado.get('nombre') , "simbolo": transicion.get('simbolo')})
    


    automataGrafico.node_attr['shape'] = 'circle'
    automataGrafico.node_attr['color'] = 'blue'
    automataGrafico.node_attr['size'] = '3.0'
    automataGrafico.edge_attr['width'] = '2.0'

    llegadas=[]
    salidas=[]
    #Evaluar estado inalcanzable
    for estado in estados:
        llegadas.clear()
        salidas.clear()
        for estado1 in estados:
            for transicion in estado1.get('transiciones'):
                if transicion.get('a') == estado.get('nombre') and estado1.get('nombre') != estado.get('nombre'):
                    llegadas.append(estado1.get('nombre'))
                if estado.get('nombre') == estado1.get('nombre') :
                    salidas.append(transicion.get('a'))
            print("Llegadas de {0}: {1}".format(estado.get('nombre'), llegadas))
            print("Salidas de {0}: {1}".format(estado.get('nombre'), salidas))
        if len(llegadas) == 0 and estado.get('inicial') == False:
            automataGrafico.node(estado.get('nombre'), shape = 'circle', style = 'filled', fillcolor = 'red', label="{0} (Inalcanzable)".format(estado.get('nombre')))
            estados.remove(estado)


        

    automataGrafico.view()
    automataResultante["estados"] = estados
    nombre_archivo = 'AutómataResultante.json'
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(automataResultante, archivo, ensure_ascii=False, indent=4)
    return automataGrafico
