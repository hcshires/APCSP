import create
import time

myAglets = create.Aglets(3, "red")
time.sleep(2)

def startAglets():
	myAglets.add(add=20)
	
startAglets()