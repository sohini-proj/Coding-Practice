# making classes

'''
class car:
    def __init__(self,colour,seats,type):
        self.colour=colour
        self.seats=seats
        self.type=type
        self.miles=0                # default val

    def enter_race_mode(self):
        self.seats=2

car_1=car("red",5,"suv")
car_2=car("white",7,"mpv")
car_3=car("navy blue",5,"sedan",)

print(car_1.colour)
print(car_3.miles)

print(car_2.seats)
car_2.enter_race_mode()
print(car_2.seats)
'''

class user:
    def __init__(self,u_id,u_name):
        self.userid=u_id
        self.username=u_name
        self.followers=0
        self.following=0
    def follow(self,user):
        user.followers+=1
        self.following+=1
    def unfollow(self,user):
        user.followers-=1
        self.following-=1

anne=user(101,"anne_2006")
billy=user(102,"bill2788927")

print(anne.followers," ",billy.following)
billy.follow(anne)
print(anne.followers," ",billy.following)
