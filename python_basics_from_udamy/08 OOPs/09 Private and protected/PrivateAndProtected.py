class Lamp:
    def __init__(self, name: str, model: int, version: int):
        self.name = name
        self.__model = model
        self._version = version


    def description(self):
        self.__self_maintenance()
        print(self.name,self.__model)

    def __self_maintenance(self):
        print(self.name, "is fixing itself.")


class ElectricLamp(Lamp):
    def __init__(self, name : str, model: int, version:int):
        super().__init__(name, model,version)

    def do_somthing(self):
        print(self._version)

lamp: Lamp = Lamp('Lamp', 1010,123456)
lamp.description()
lamp._Lamp__self_maintenance()

el_lamp: ElectricLamp = ElectricLamp('EL Lamp', 1010,12345)
el_lamp.do_somthing()
print(el_lamp._version)