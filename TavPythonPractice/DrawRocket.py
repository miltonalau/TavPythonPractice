#Milton Lau
#2/26/19
#Rocketship HW in Python
#This program produces an ascii rocket that can be scaled with a 
#global variable 

class drawRocket():
    
    #produces the triangle shape in the rocket
    def triangle(self):
        for i in range(n*2-1):
            for j in range((n*2-i)-1):
                print(" ", end = "")
                j+=1
            for j in range(i + 1):
                print("/", end = "")
                j+=1
            print("**", end = "")
            for j in range(i + 1):
                print("\\", end = "")
                j+=1
            print("")
            i+=1

    #produces the line separating rocket pieces
    def line(self):
        print("+", end = "")
        for i in range(n*2):
            print("=*", end = "")
            i+=1
        print("+")

    #produces the two triangular shapes in the rocket
    def pyramid(self):
        for i in range(n):
            print("|", end = "")
            for j in range(2):   
                for k in range((n-i)-1):
                    print(".", end = "")
                    k+=1
                for k in range(i+1):
                    print("/\\", end = "")
                    k+=1
                for k in range((n-i)-1):
                    print(".", end = "")
                    k+=1
                j+=1
            print("|", end = "")
            print("")
            i+=1

    #produces the two V shapes in the rocket
    def vee(self):
        for i in range(n):
            print("|", end = "")
            for j in range(2):
                for k in range(i):
                    print(".", end = "")
                    k+=1
                for k in range(n-i):
                    print("\\/", end = "") 
                    k+=1
                for k in range(i):
                    print(".", end = "")
                j+=1
            print("|", end = "")
            print("")
            i+=1

    #combines the pyramid and V shapes to form the diamond shape        
    def diamond(self):
        drawRocket.pyramid()
        drawRocket.vee()

    #combines the V and pyramid shapes to form the hourglass shape
    def hourglass(self):
        drawRocket.vee()
        drawRocket.pyramid()

drawRocket = drawRocket()
n = 5 #global constant to scale rocketship

drawRocket.triangle()
drawRocket.line()
drawRocket.diamond()
drawRocket.line()
drawRocket.hourglass()
drawRocket.line()
drawRocket.triangle()
