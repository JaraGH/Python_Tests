class Persona:
    
    def __init__(self, id, nombre, edad) -> None:
        self.id=id
        self.nombre=nombre
        self.edad=edad
    
    def __lt__(self, other):
        return self.edad<other.edad
    
    def __eq__(self,otro) -> bool:
        return self.edad== otro.edad
    
    def __str__(self) -> str:
        return f"id: {self.id} - nombre: {self.nombre} edad: {self.edad}"
    
personas = [Persona(1, "Jose", 53), 
            Persona(2, "Sara", 21),
            Persona(3, "Emi", 51) ]

ordenada = sorted(personas)

for p in ordenada:
    print(p)