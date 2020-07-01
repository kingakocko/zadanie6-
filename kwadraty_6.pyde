class Kwadrat():
    def __init__(self, bok): 
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class PasiastyKwadrat(Kwadrat):
    def sketchPasiasty(self, x, y, paski):
        Kwadrat.sketch(self, x, y) 
        space = self.bok/paski 
        _xLinii_ = 0 
        for pasek in range(0, paski): 
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
class NiebieskiPasiastyKwadrat(Kwadrat):
    def sketchNiebieskiPasiasty(self,x,y, paski):
        fill(64,224,208)
        Kwadrat.sketch(self, x, y) 
        space = self.bok/paski 
        _xLinii_ = 0 
        for pasek in range(0, paski): 
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
class CzerwonyKwadrat(Kwadrat):
    def sketchCzerwony(self,x,y):
        fill(255,0,0)
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
   
    
            
def setup():
    size(500, 500)
    background(100,100,50)
    malyKwadrat = Kwadrat(25.0)
    malyKwadrat.sketch(200,100)
    duzyKwadrat = Kwadrat(200.0)
    duzyKwadrat.sketch(200,50)
    malyKwadrat.sketch(5,200) 
    malyPasiastyKwadrat = PasiastyKwadrat(50.0) 
    malyPasiastyKwadrat.sketchPasiasty(200, 300, 10) 
    malyPasiastyKwadrat.sketchPasiasty(100,300, 1) 
    duzyPasiastyKwadrat = PasiastyKwadrat(100.0)
    duzyPasiastyKwadrat.sketchPasiasty(200, 50, 12)
    duzyPasiastyKwadrat.sketch(350, 300)
    duzyKolorowyKwadrat= NiebieskiPasiastyKwadrat (150.0)
    duzyKolorowyKwadrat.sketchNiebieskiPasiasty(10,350,30)
    malyNiebieskiPasiastyKwadrat= NiebieskiPasiastyKwadrat (40.0)
    malyNiebieskiPasiastyKwadrat.sketchNiebieskiPasiasty (450,50,3)
    duzyCzerwonyKwadrat= CzerwonyKwadrat (100.0)
    duzyCzerwonyKwadrat.sketchCzerwony(10,250)
    malyCzerwonyKwadrat= CzerwonyKwadrat (25.0)
    malyCzerwonyKwadrat.sketchCzerwony (250,250)
