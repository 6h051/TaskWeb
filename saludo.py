from os import system as s

while True:
    print("Diga un saludo: ")
    a = input("")
    if a[0] == "$":
        s(f"{a[1:]}> saludo.txt")
    else:
        s(f"echo '{a}'> saludo.txt")