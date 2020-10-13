import os

directorio = "D:/Música"
count = 0

for base, dirs, files in os.walk(directorio):
  for fichero in files:
    (nombre, extension) = os.path.splitext(fichero)
    if(extension == ".mp3"):
        count += 1

print (count)

