import threading as th


#Hilos
def productor(num):
	global nelementos
	for n in range(nelementos):
		global indice
		global buffer
		global nbuffer
		item = n*n
		libre.acquire()
		mutex.acquire()
		if indice<nbuffer:
			indice += 1
			buffer[indice] = item
			print (f"productor {indice} {item} {buffer}", flush = True)
		mutex.release()
		ocupado.release()
def consumidor(num):
	item = None
	global nelementos
	for _ in range(nelementos):
		global indice
		global buffer
		ocupado.acquire()
		mutex.acquire()
		if indice>-1:
			item = buffer[indice]
			buffer[indice] = None
			print (f"consumidor {indice} {item} {buffer}", flush = True)
			indice -= 1
		mutex.release()
		libre.release()
#Variables del programa
fhilos = [productor, consumidor]
nbuffer = 5
buffer = [None]*nbuffer
indice = -1
nelementos = 4
libre = th.Semaphore(value = nbuffer)#Casillas libres
ocupado = th.Semaphore(value = 0)#Casillas ocupadas
mutex = th.Semaphore(value = 1)


#Crear lista de hilos
hilos = [th.Thread(target = fhilos[n], args = (n,)) for n in range(len(fhilos))]

#Empezar Hilos
for hilo in hilos:
    hilo.start()






