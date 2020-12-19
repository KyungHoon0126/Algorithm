# Car_Class_Ex.py

class Car:

    def __init__(self):  # 생성자, 인스턴스객체를 생성할 때 자동으로 호출
        print("Car의 생성자가 호출되었습니다.")
        self.car_name = "소나타"  # 인스턴스 멤버 car_name, 자동차의 차종, 초기값은 '소나타'로 설정.
        self.car_drv = "전륜"  # 인스턴스 멤버 car_drv, 자동차의 구동 방식, 초기 값은 '전륜'으로 설정.
        self.car_speed = 0  # 인스턴스 멤버 car_speed, 자동차의 속도, 초기 값은 0으로 설정.
        self.car_direction = "앞쪽"  # 인스턴스 멤버 car_direction, 자동차의 방향, 초기 값은 '앞쪽'으로 설정.

    # set_car_name(), get_car_name()
    def car_name_set(self, set_car_name):  # 메서드
        print("set_car_name is called!!")
        self.car_name = set_car_name
        print("차종이 [{0}]으로 변경 되었습니다.".format(self.car_name))

    def car_name_get(self):  # 메서드
        print("get_car_name is called!!")
        return self.car_name

    # set_car_drv(), get_car_drv()
    def set_car_drv(self, set_car_drv):  # 메서드
        print("set_car_drv is called!!")
        self.car_drv = set_car_drv
        print("차의 구동 방식이 [{0}]으로 변경 되었습니다.".format(self.car_drv))

    def get_car_drv(self):  # 메서드
        print("get_car_drv is called!!")
        return self.car_drv

    # set_car_speed, get_car_speed()
    def set_car_speed(self, set_speed):  # 메서드
        print("set_car_speed is called")
        self.car_speed = set_speed
        print("자동차의 속력이 시속 [{0}]km 로 변경되었습니다.".format(self.car_speed))

    def get_car_speed(self):  # 메서드
        print("get_car_speed is called!!")
        return self.car_speed

    # set_car_direction, get_car_direction
    def stop(self):  # 메서드
        self.car_direction = '정지'
        print('차가 정지 하였습니다.')

    def start(self):  # 메서드
        print('자동차가 시동이 걸렸습니다.')


sonata = Car()  # sonata 객체 생성

print(sonata.car_name_set("산타페"))
sonata.car_name_get()

print(sonata.set_car_drv("4륜"))
sonata.get_car_drv()

print(sonata.set_car_speed(100))
sonata.get_car_drv()

sonata.stop()
sonata.start()