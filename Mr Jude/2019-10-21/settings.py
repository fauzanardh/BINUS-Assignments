class Settings:
    def __init__(self, width, height, color, bulletSpeedFactor=1, botResponseTime=0.25):
        self.width = width
        self.height = height
        self.color = color
        self.bulletSpeedFactor = bulletSpeedFactor
        self.botResponseTime = botResponseTime

    def getWH(self):
        return (self.width, self.height)

    def getMidWH(self):
        return (self.width//2, self.height//2)

    def getColor(self):
        return self.color

    def getBulletSpeedFactor(self):
        return self.bulletSpeedFactor

    def getBotResponseTime(self):
        return self.botResponseTime
