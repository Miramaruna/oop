class Appilence:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

    def use(self):
        pass

    def repaire(self):
        pass


class WashingMachine(Appilence):
    def turn_on(self):
        print("Cтиральная машина включина")

    def turn_off(self):
        print("Стиральная машина выключена")

    def use(self):
        print("Стиральная машина стирает одежду")

    def repaire(self):
        print("Стиральную машину чинят")


class MicroWave(Appilence):
    def turn_on(self):
        print("Микроволновка включена")

    def turn_off(self):
        print("Микроволновка выключена")

    def use(self):
        print("Микроволновка разгревает еду")

    def repaire(self):
        print("МикроВолновку чинят")


class Refrigerator(Appilence):
    def turn_on(self):
        print("Холодильник включен")

    def turn_off(self):
        print("Холодильник выключен")

    def use(self):
        print("Холодильник работает")
    
    def repaire(self):
        print("Холодильник чинят")


microwave = MicroWave()

refrigerator = Refrigerator()

washingmachine = WashingMachine()

microwave.turn_on()
microwave.turn_off()
microwave.use()
microwave.repaire()

refrigerator.turn_off()
refrigerator.turn_on()
refrigerator.use()
refrigerator.repaire()

washingmachine.turn_on()
washingmachine.turn_off()
washingmachine.use()
washingmachine.repaire()