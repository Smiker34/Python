class TrafficLight():
    def __init__(self):
        self.__color = "red"

    def running(self):
        import time
        colors = ["red", "yellow", "green"]
        while True:
            print(self.__color)
            time.sleep(7)
            self.__color = colors[1]
            print(self.__color)
            time.sleep(2)
            self.__color = colors[2]
            colors.reverse()

traffic_light = TrafficLight()
traffic_light.running()