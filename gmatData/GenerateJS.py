# Abre el archivo en modo de lectura ('r')
with open('gmatData/ReportFile1.txt', 'r') as file:
    # Lee una línea a la vez
    linea = file.readline()

    while linea:
        # Procesa la línea
        print(linea.strip())  # strip() elimina los caracteres de nueva línea
        # Lee la siguiente línea
        linea = file.readline()
