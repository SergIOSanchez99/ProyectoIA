class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
marca_auto = input("Marca del auto -->")
modelo_auto = input("Modelo del auto -->")
año_auto = input("Año del auto -->")
   
auto1 = Auto(marca_auto,modelo_auto,año_auto)

print("Auto 1 -- Caracteristicas:") 

print(f"Marca-->{auto1.marca}")    
print(f"Modelo-->{auto1.modelo}")    
print(f"Año-->{auto1.año}")    
        
        
        