class Calculadora:
    def somar(self, a , b):
        return a + b
    
    def subtrair(self, a ,b):
        return a - b

calc= Calculadora()
print(calc.somar(5, 8))  
res= calc.subtrair(5,8)
print(res) 