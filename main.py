floppy = 1,44 #Mb
pages = 100
lines = 50
sym = 25
onesym = 4 #Byte
4*25*50*100
books = int(1.44/(4*25*50*100/1024/1024))

print(f"{books} book")
