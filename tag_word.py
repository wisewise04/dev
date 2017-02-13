import enchant
import sys,os,time,random

checker = enchant.Dict("en_US")
#참 거짓을 반환하는 checker.
#if(checker.check("hello")) 하면 참.
#checker.check("asdasd") 하면 거짓.

used_data = [] #이미사용된 단어 저장
time.sleep(1)

print("Loading dictionary ...")
print("""


    =-=-=-=-=-=-=-=-=-=-=-=-=( INFO )-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    Developer : IT_GAME
    Power By  : Python 3
    Blog      : https://medium.com/@jinkwon711
    Since     : 2017 02 07
    Version   : 1.0.0 Alpha
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=



-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
""")
a_word = ""
b_word = ""
player_a_turn = False;
while True:
    a_word = input("시작할 영단어를 입력해주세요 : ")
    if(checker.check(a_word)):
        used_data.append(a_word)
        break

while True:
    if player_a_turn:
        while True:
            a_word = input("A's Turn -- '{}' 로 시작하는 영단어를 입력해주세요: ".format(b_word[-1]))
            if(a_word[0]==b_word[-1]):
                if(checker.check(a_word)):
                    if(a_word not in used_data):
                        used_data.append(a_word)
                        player_a_turn = False
                        break
                    else:
                        print("이미 사용한 단어 입니다")
                else:
                    print("영단어가 아닙니다")
            else:
                print("{}로 시작하는 단어가 아닙니다".format(b_word[-1]))
    else:
        while True:
            b_word = input("B's Turn -- {}로 시작하는 영단어를 입력해주세요: ".format(a_word[-1]))
            if(b_word[0]==a_word[-1]):
                if(checker.check(b_word)):
                    if(b_word not in used_data):
                        used_data.append(b_word)
                        player_a_turn = True
                        break
                    else:
                        print("이미 사용된 단어 입니다")
                else:
                    print("영단어가 아닙니다")
            else:
                print("{}로 시작하는 단어가 아닙니다".format(a_word[-1]))

