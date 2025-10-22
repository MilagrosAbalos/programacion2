def cifrado_cesar(mensaje,despl):
    nuevo_mensaje=""
    for caracter in mensaje:
        
        if caracter.isalpha():

            if caracter.isupper():
                base=ord("A")
            else:
                base=ord("a")
            nuevo_caracter=chr((ord(caracter)- base + despl)% 26 + base)
            nuevo_mensaje+= nuevo_caracter
        else:
            nuevo_mensaje+=caracter
            
    return nuevo_mensaje
            
print("Ingrese el mensaje:")
mensaje=input()

print("Ingrese el dezplazamiento. Si quiere cifrar positivo, si quiere descifrar negativo.")
despl=int(input())
            
resultado= cifrado_cesar(mensaje, despl)
print(resultado)
