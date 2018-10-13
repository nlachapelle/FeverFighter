#Player Class

class Player:
    def __init__(self, X, Y, width, height, gunY, gunX):
        self._name = "" #Players Name
        self._disease = None #Players Disease
        self._X = X #Players positions X value
        self._Y = Y #Players positions Y value
        self._width = width #Players width
        self._height = height #Players height
        self._facing = "Right" #What side is player facing (initial is "Right")
		self._kills = 0 #Players kills
		self._score = 0 #Players score
		self._killScore = 10 
		self._health = 100 #Players health
		self._maxCartridge = 30 #Player cannot have more than 30 bullets
		self._cartridge = self._maxCartridge #Player initially has 30 bullets
        
        self._gunX = self._X + gunX #guns X position
        self._gunY = self._Y + gunY #guns Y position
        
    def set_name(self, name):
        self._name = name
        
    def get_name(self):
        return self._name
    
    def set_disease(self, disease):
        self._disease = disease
        
    def get_disease(self):
        return self._disease
    
    def set_X(self, X):
        self._X = X
        
    def get_X(self):
        return self._X
    
    def set_Y(self, Y):
        self._Y = Y
        
    def get_Y(self):
        return self._Y
    
    def set_width(self, width):
        self._width = width
        
    def get_width(self):
        return self._width
    
    def set_height(self, height):
        self._height = height
        
    def get_height(self):
        return self._height
    
    def move_X(self, moveX):
        self._X += moveX
        self._gunX += moveX
        
    def move_Y(self, moveY):
        self._Y += moveY
        self._gunY += moveY
        
    def get_facing(self):
        return self._facing
    
    def reverse_facing(self):
        self._facing = "Left"
        
    def set_gunX(self, X):
        self._gunX = X
        
    def get_gunX(self):
        return self._gunX
    
    def set_gunY(self, Y):
        self._gunY = Y
        
    def get_gunY(self):
        return self._gunY
    
    def jump(self, Y, y):
        X = self._X
        x = y
        while self._Y < Y: #Player goes up in this loop
            self._Y += y
            y -= 1
            if y < 0:
                y = 1
                
        while self._X > X: #Player comes down in this loop
            self._Y -= x
            x += 1
            if x > self._X:
                x = 1
	
	def set_killScore(self, killScore): #This is set for the points player gets for each kill
		self._killScore = killScore
		
	def get_killScore(self): #This is get for the points player gets for each kill
		return self._killScore
            
	def kill(self):
		self._kill += 1
		self._score += self._killScore
		
	def hit(self, health):
		self._health -= health
		
	def set_health(self, health):
		self._health = health #Initial health is 100
		
	def get_health(self):
		return self._health
		
	def set_maxCartridge(self, maxCart):
		self._maxCartridge = maxCart
		
	def get_cartridge(self):
		return self._cartridge