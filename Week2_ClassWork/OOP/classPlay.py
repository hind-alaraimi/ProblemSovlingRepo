class Play:
    def __init__(self,name):
        self.name = name

    def toyname(self,toy):
        return(f"{self.name} play with {toy}")
    
boy = Play("Ahmed")
print(boy.toyname("ball"))
