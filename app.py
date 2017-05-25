
class app:

    def __init__(self):
        self.name = ''
        self.src = ''
        self.imgsrc = ''
        self.apptype = ''
        self.lable = list()
        self.size = ''
        self.version = ''
        self.lastupdatetime = ''
        self.hot = 0
        self.desc = list()
        self.screenshot = list()

    def printf(self):
        print(self.name)
        print(self.src)
        print(self.imgsrc)
        print(self.apptype)
        print(self.lable)
        print(self.size)
        print(self.lastupdatetime)
        print(self.hot)
        print(self.version)
        print(self.desc)
        print(self.screenshot)

class AppSpecial:

    def __init__(self):
        self.name = ''
        self.desc = ''
        self.src = ''
        self.iconSrc = ''
        self.appList = list()
        self.updateTime = ''

    def printf(self):
        print(self.name)
        print(self.desc)
        print(self.src)
        print(self.iconSrc)
        print(self.appList)
        print(self.updateTime)


