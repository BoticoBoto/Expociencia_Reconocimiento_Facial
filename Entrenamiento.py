
    for fila in listData:
        rutacompleta = Data_ruta +"/"+ fila
        print("Iniciando lectura ...")
        for archivo in os.listdir(rutacompleta): 
        
            print("imagen: ", fila + "/" + archivo)
            ids.append(id)
            rostrosData.append(cv.imread(rutacompleta + "/" + archivo, 0))
        id = id + 1
        tiempofinallectura = time()
        tiempolecturatotal = tiempofinallectura - timpoinicial
        print("Tiempo total: ", tiempolecturatotal)
    entrenamientoModelo1 = cv.face.EigenFaceRecognizer_create()
    print("Iniciando el entrenamiento ...")
    entrenamientoModelo1.train(rostrosData, np.array(ids))
    tiempofinalentrenamiento = time()
    tiempototalentrenamiento = tiempofinalentrenamiento-tiempolecturatotal
    print("Tiempo entrenamiento total ", tiempototalentrenamiento)
    entrenamientoModelo1.write("EntrenamientoEigenFaceRecognizer.xml")
    print("entrenamiento concluido")

else:
    exit()
