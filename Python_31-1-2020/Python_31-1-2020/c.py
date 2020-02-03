class StorageArray(object):
    vendor = ""
    def __init__(self, v, c):
        self.version = v
        self.type = c

    def getLun(self, lun_no):
        l = "{}_{}".format(self.type, lun_no)
        return l

    @staticmethod
    def getSuffixForLun(p):
        return p*2

    @classmethod
    def updateVersion(cls):
        print("cls ::", cls)
        print("dir(cls) ::", dir(cls))
        print(cls.vendor)

if __name__ =="__main__":
    obj = StorageArray("12.01", "Block")
    print(obj.getLun(99))
    print("-------------------------")
    print(obj.getSuffixForLun(10))
    print("-------------------------")
    #obj.updateVersion()
    StorageArray.updateVersion()