import os

directorio = "D:/Desc"

for base, dirs, files in os.walk(directorio):
  for fichero in files:
    (nombre, extension) = os.path.splitext(fichero)
    if(nombre.startswith("y2mate.com - ")):
        os.rename(directorio + "/" + nombre + extension, directorio + "/" + nombre.strip("y2mate.com - ") + extension)

