import random, string, sys
from matplotlib import pyplot as plt

class Lotto : # Lotto 클래스 생성.
    
    graph_lotto = []
    y = []

    def exitProgram() :
        sys.exit()

    def __init__(self): # 생성자

        # 생성자에서 실행할 명령 초기화
        self.menu = {
                        1 : "프로그램 소개",
                        2 : "프로그램 시작 & 랜덤 로또 번호 그래프 확인",
                        3 : "프로그램 종료",
                    }

    def create_Random_Lotto_Number(self, lotto_num) : 

    ####
    ####
        if lotto_num == 1 :
            print("로또 번호 랜덤 생성 프로그램 입니다.")
            input_command = int(input("다른 명령 실행하기 [2. 프로그램 시작 3. 프로그램 종료] : "))


            if input_command == 2 :
                    print("☆★☆★ 로또 번호 랜덤 생성 ☆★☆★")
                    print("---------------------------------------")
                    print("게임 수를 입력하세요(숫자만 입력).")
                    input_command = "Y"

                    while(input_command == "Y"):

                        num = input("진행할 게임 횟수를 입력해 주세요 : ")
    
                        if(num.isdigit() == True):
        
                            print("---------------------------------------")
        
                            for i in range(0, int(num)):
                                lotto = random.sample(range(1, 46), 6)
                                lotto.sort()
                                graph_lotto = lotto
                                # print(lotto, graph_lotto)
                                # print(graph_lotto)
                                print(lotto)

                                y =  graph_lotto
                                x = range(len(y))
                                plt.bar(x, y, width = 0.7, color="Orange")
                                plt.show()

        
                        print("---------------------------------------")
                        print("★☆★ 로또 번호 자동 생성 완료 ★☆★")
                        input_command = input("다시 하시겠습니까(Y/N)? : ")


                    while input_command != "Y" and input_command != "N":
                        print("Y 또는 N을 입력해 주세요.")
                        print("---------------------------------------")
                        input_command = input("다시 하시겠습니까(Y/N)? : ")
                                                                                                                                                                                                                                                                                                    
                    while(input_command == "N"):
                        return False, Lotto.exitProgram

            if input_command == 3 :
                exitProgram()

    ####
    ####
        if lotto_num == 2 :
            print("☆★☆★ 로또 번호 랜덤 생성 ☆★☆★")
            print("---------------------------------------")
            print("게임 수를 입력하세요(숫자만 입력).")
            input_command = "Y"

            while(input_command == "Y"):

                num = input("진행할 게임 횟수를 입력해 주세요 : ")
    
                if(num.isdigit() == True):
        
                    print("---------------------------------------")
        
                    for i in range(0, int(num)):
                        lotto = random.sample(range(1, 46), 6)
                        lotto.sort()
                        graph_lotto = lotto
                        # print(lotto, graph_lotto)
                        # print(graph_lotto)
                        print(lotto)
                        
                        y =  graph_lotto
                        x = range(len(y))
                        plt.bar(x, y, width = 0.7, color="Orange")
                        plt.show()

        
                print("---------------------------------------")
                print("★☆★ 로또 번호 자동 생성 완료 ★☆★")
                input_command = input("다시 하시겠습니까(Y/N)? : ")
    
    
            while(input_command != "Y" and input_command != "N"):
                print("Y 또는 N을 입력해 주세요.")
                print("---------------------------------------")
                input_command = input("다시 하시겠습니까(Y/N)? : ")


            while(input_command == "N"):
                    return False, Lotto.exitProgram


class ControlLotto : 
    def __init__(self):
        self.lot = Lotto()

    def create_Random_Lotto_Number(self, lotto_num):
        self.lot.create_Random_Lotto_Number(lotto_num)


class ViewLotto : # ViewLotto 클래스 생성.
    def __init__(self):
        self.Lotto = Lotto()
        self.controLotto = ControlLotto()

    def DisplayLotto(self): # ViewLotto 클래스의 DisplayLotto() 메소드
        while True :
            
            print('1. {0} 2. {1} 3. {2}'.format(self.Lotto.menu[1], self.Lotto.menu[2], self.Lotto.menu[3]))

            lotto_num = int(input('실행할 프로그램의 명령을 입력해 주세요 : '))
            
            if lotto_num == 3 :
                break

            lotto_result = self.controLotto.create_Random_Lotto_Number(lotto_num)         


if __name__ == '__main__': 
    viewLotto = ViewLotto()
    viewLotto.DisplayLotto()
    