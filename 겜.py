import random

random=random.randrange(1,11)
point=10
tong=[]

while(point>0):
	a=input("1부터 10까지 숫자 중 고르세요.")
	if(random<int(a)):
		tong.append(a)
		point=point-1
		print("그것보단 작아.")
	elif(random>int(a)):
		tong.append(a)
		point=point-1
		print("그것보단 커")
	else:
		print("마자")
		print("점수는 {}점이야".format(point))
		print("너가 틀린값은 아래에 있어")
		print(tong)
		for i in tong:
			print("너가고른 숫자는 {}야".format(i))
			
		break


