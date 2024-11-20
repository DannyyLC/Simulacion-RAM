#Metodo que se usa para cargar los archivos de estilo al programa

def load_stylesheets(*paths):
    styles = ""
    for path in paths: #Iteramos sobre la lista de archivos
        with open(path, "r") as file:
            styles += file.read() # Abrimos los archivos
    return styles
