import os
import sys
import zipfile
import getpass
try:
    opcion=1
    def rutas():
        ruta=input("Dame una ruta: ")
        return ruta
    def magnitudBytes():
        magnitud=int(input("Dime un tamaño de bytes: "))
        return magnitud
    #Vamos a elegir una de las opciones
    while (opcion>=1 and opcion<=5):
        print("\n")
        print("1.- Mostrar archivos superiores en tamaño a uno especificado")
        print("2.- Borrar archivos superiores en tamaño a uno especificado")
        print("3.- Comprimir un fichero o carpeta especificada")
        print("4.- Borrar los archivos temporales de nuestro navegador")
        print("5.- Cerrar el programa")
        opcion = int(input("Selecciona una opción (1-5): "))
        #elegimos la primera opcion
        if (opcion==1):
            ruta=rutas()
            os.chdir(ruta)
            magnitud= magnitudBytes()
            listaArchivos=os.listdir(".")
            f = open("registro.log", "w")
            #creamos un contador para  poder contar los archivos mayores a los bytes dados
            contador=0
            for elemento in listaArchivos:
                magnitudArchivo=os.stat(elemento).st_size
                if (magnitudArchivo)>=(magnitud):
                    contador += 1
                    print("- ",elemento)
                    f.write(elemento + "\n")
            print("Se han encontrado %i archivos de tamaño superior a %i Bytes en la carpeta actual. " %(contador,magnitud))
            f.write("Se han encontrado %i archivos de tamaño superior a %i Bytes en la carpeta actual. " %(contador,magnitud))
            f.close()
            
            
        #elegimos la opcion 2        
        if (opcion==2):
            ruta2=rutas()
            os.chdir(ruta2)
            magnitud2=magnitudBytes()
            listaArchivos2=os.listdir(".")
            contador2=0
            for elemento2 in listaArchivos2:
                magnitudArchivo2=os.stat(elemento2).st_size
                if (magnitudArchivo2)>=(magnitud2):
                    contador2 += 1
                    print("- ",elemento2)
                    os.remove(elemento2)
            print("Se han encontrado %i archivos de tamaño superior a %i Bytes en la carpeta actual, los cuales se han borrado" %(contador2,magnitud2))
        #utilizamos este código para comprimir los archivos
        if (opcion==3):
            ruta3=input("Dame una ruta: ")
            archivoZip = zipfile.ZipFile("comprimido.zip", 'w')
            for carpeta,subcarpetas,archivos in os.walk(ruta3):
                for archivo in archivos:
                    archivoZip.write(os.path.join(carpeta, archivo), os.path.relpath(os.path.join(carpeta,archivo), ruta3), compress_type = zipfile.ZIP_DEFLATED)
                
            archivoZip.close()
        #utilizamos este codgio para borrar la caché
        if (opcion==4):
            print("Por favor revise si Google chrome se encuentra cerrado")
            usuario = getpass.getuser()
            os.chdir("C:\\Users\\" + usuario + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache")
            cache = os.listdir()
            borrarcache = input("Quiere borrar la caché(S/N): ")
            for elemento in cache:
                if (borrarcache=="S"):
                    os.remove(elemento)
        
        if (opcion==5):
            print("\n")
            print("- El programa se va a cerrar")
            sys.exit()
            exit()
        if (opcion!=5):
            print("\n")
            print("¡¡¡tienes que seleccionar una de las 5 opciones!!!")
            opcion=1
except:
    if (opcion!=5):
        print("\n")
        print("¡¡¡tienes que seleccionar una de las 5 opciones!!!")
