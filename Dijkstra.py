

def dijkstra(grafico, inicio, fin):
    distancia_corta = {} #Obtener el costo de ir al nodo
    seguimiento_predecesora = {} #Guardar el camino (distancia) que va recorriendo hasta llegar al nodo
    Nodos_no_visitados = grafico #Para saber que nodos nos faltan recorrer
    infinito = 999999
    track_path =[] # Guardar la ruta optima
    
    for nodo in Nodos_no_visitados:
        distancia_corta[nodo] = infinito
    distancia_corta[inicio] = 0
    
    while Nodos_no_visitados:
        
        distancia_minima_nodo = None
        
        for nodo in Nodos_no_visitados:
            if distancia_minima_nodo is None:
                distancia_minima_nodo = nodo
            elif distancia_corta[nodo] < distancia_corta[distancia_minima_nodo]:
                distancia_minima_nodo = nodo
            
        opciones_de_ruta = grafico[distancia_minima_nodo].items()
        
        for nodo_hijo, peso in opciones_de_ruta:
            if peso + distancia_corta[distancia_minima_nodo] < distancia_corta[nodo_hijo]:
                distancia_corta[nodo_hijo] = peso + distancia_corta[distancia_minima_nodo]
                seguimiento_predecesora[nodo_hijo] = distancia_minima_nodo
        
        Nodos_no_visitados.pop(distancia_minima_nodo)
        
    nodoActual = fin
    
    while nodoActual != inicio:
        try:
            track_path.insert(0, nodoActual)
            nodoActual = seguimiento_predecesora[nodoActual]
        except KeyError:
            print("Error")
            break
        
    track_path.insert(0,inicio)
    
    if distancia_corta[fin] != infinito:
        print("La distancia más corta es: " + str(distancia_corta[fin]))
        print("Ruta optima es :" + str(track_path))

def main():
	grafico = {
	    'a': {'b': 3, 'c':4, 'd':7},
	    'b': {'c': 1, 'f':5},
	    'c': {'f': 6, 'd':2},
	    'd': {'e': 3, 'g':6},
	    'e': {'g': 3, 'h':4},
	    'f': {'e': 1, 'h':8},
	    'g': {'h': 2},
	    'h': {'g': 2}
	}
	#Distntacia del punto 0 al punto más lejano
	dijkstra(grafico,'a','h')

if __name__ == "__main__":
	main()

