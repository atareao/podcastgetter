1.- Borrar la base de datos actual:
	$ rm ~/.config/podcastgetter/file:///home/lorenzo/.config/podcastgetter/podcastgetter.db 
2.- Para generar md, html y m3u de todo el contenido, ejecutar:
	$ ./podcastgetter.py
NOTA: Los archivos se generan en el directorio en el que se ejecuta
3.- Para genera la lista de favoritos, ejecutar:
	$ ./podcastgetter.py lista.csv
NOTA: Los archivos se generan en el directorio en el que se ejecuta
El CSV debe ir separado por "|" no por comas tal y como está en "lista.csv"
