import random

random=random.randrange(1,11)
point=10
tong=[]

while(point>0):
	a=input("1부터 10가지 숫자중 고르세요:")
	if(random<int(a)):
		tong.append(a)
		point=point-1
		print("헤헤헤헤 그것보단 작지")
	elif(random>int(a)):
		tong.append(a)
		point=point-1
		print("헤헤헤헤 그것보단 크지")
	else:
		print("잘했어")
		print("점수는 {}점이야".format(point))
		print("너가 틀린값은 아래에 있어")
		print(tong)
		for i in tong:
			print("너가 고른 틀린 값은 :{}".format(i))

		break
		
	
		
		
			
	
