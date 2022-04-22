class Familia():
    def __init__(self,papa,mama,hijos):
        self.papa = papa
        self.mama = mama
        self.hijos = hijos

    def __str__(self):
        return f"Papa: {self.papa} \nMama: {self.mama} \nHijos: {self.hijos}"



familia  = Familia("Rodrigo", "Laura", ["Juan","Pedro","Maria"] )
print(familia)