from datetime import datetime
import os
def read_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print(f"El archivo '{file_path}' no fue encontrado.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None
def convert_to_json_format(line):
    # Separa los elementos de la línea
    elements = line.split()

    # Obtiene la fecha y hora en el formato deseado
    date_str = " ".join(elements[:3])
    time_str = elements[3]
    datetime_str = f"{date_str} {time_str}"
    datetime_obj = datetime.strptime(datetime_str, "%d %b %Y %H:%M:%S.%f")
    formatted_datetime = datetime_obj.strftime("%d %b %Y %H:%M:%S.%f")

    # Obtiene los valores de X, Y, y Z
    x_value = float(elements[4])
    y_value = float(elements[5])
    z_value = float(elements[6])

    # Crea el diccionario en formato JSON
    json_data = {
        "Date": date_str,
        "Time": time_str,
        "X": x_value,
        "Y": y_value,
        "Z": z_value
    }
    json_dataSTR = (str(f'{{\"Date\":\"{date_str}\",\"Time\":\"{time_str}\",\"X\":{x_value},\"Y\":{y_value},\"Z\":{z_value}}}'))

    # Retorna el diccionario en formato JSON
    return json_dataSTR
def crearArchivoJS(file_name, content):
    try:
        # Obtiene la ruta del directorio actual
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        # Combina la ruta del directorio actual con el nombre del archivo
        file_path = os.path.join(current_directory, file_name)

        # Escribe el contenido en el archivo
        with open(file_path, 'w') as file:
            file.write(content)

        print(f"Contenido escrito en '{file_path}' exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error al escribir en el archivo: {e}")
#print(convert_to_json_format('07 Oct 2023 12:04:06.682   26163.1                   175472                    27627.5'))
lines = read_lines('ReportFile1.txt')
lines.remove(lines[0])
jsonLines = []
jsonLines.append(convert_to_json_format(str(lines[0])))
for line in lines[:]:
    jsonLines.append(convert_to_json_format(str(line)))
data = str(f"{{"'\"coordinates\":[\n')
for jsonline in jsonLines[:len(jsonLines)-1]:
    data = data+(f'{jsonline},\n')
data = data+(f'{jsonLines[len(jsonLines)-1]}')
data = data+']}'
crearArchivoJS('mission.json', data)