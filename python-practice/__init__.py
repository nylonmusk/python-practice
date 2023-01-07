# __init__
# init 함수에 정의된 개수만큼, self를 제외한 개수만큼을 보내주어야 객체생성이 가능함

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))


# tank = Unit("탱크")
# tank = Unit("탱크", 150)
