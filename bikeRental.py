import datetime


class Bikes:
    all = []
    hour_rate = 5
    daily_rate = 20
    weekly_rate = 60
    total_bikes = 100

    def available_bikes(self):
        pass

    def family_rental(self):
        pass



class BikeRental:
    def __init__(self, stock=0):
        self.stock = stock

    def displaystock(self):
        print("We have currently {} bikes in our shop".format(self.stock))
        return self.stock

    def rentBikeOnHourlyBasis(self, n):
        assert n>0, "Number of bikes {} requested not greater than 0".format(n)
        assert n<self.stock, "Sorry! We have currently {} bikes to rent".format(self.stock)

        now = datetime.datetime.now()
        print("You have rented {} bike(s) on hourly basis today at {} hours".format(n,now.hour))
        print("You will be charged $5 for each hour per bike")
        print("We hope that you enjoy our service")

        self.stock-=n
        return now

    def rentBikeOnDailyBasis(self, n):
        assert n>0, "Number of bikes {} requested not greater than 0".format(n)
        assert n<self.stock, "Sorry! We have currently {} bikes to rent".format(self.stock)

        now = datetime.datetime.now()
        print("You have rented {} bike(s) on daily basis today at {} hours".format(n,now.hour))
        print("You will be charged $20 for each day per bike")
        print("We hope that you enjoy our service")

        self.stock-=n
        return now

    def rentBikeOnWeeklyBasis(self, n):
        assert n>0, "Number of bikes {} requested not greater than 0".format(n)
        assert n<self.stock, "Sorry! We have currently {} bikes to rent".format(self.stock)

        now = datetime.datetime.now()
        print("You have rented {} bike(s) on weekly basis today at {} hours".format(n,now.hour))
        print("You will be charged $60 for each week per bike")
        print("We hope that you enjoy our service")

        self.stock-=n
        return now

    def returnBike(self, request):
        rentalTime, rentalBasis, numOfBikes = request
        bill = 0

        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes

            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numOfBikes

            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * numOfBikes

            if (3 <=numOfBikes<=5):
                print("You are eligible for family rental offer at 30% discount")
                bill = bill * 0.7

            print("Thanks for returning bike!")
            print("That would be {}".format(bill))
            return bill

        else:
            print("Are you sure you rented bike with us?")
            return None

class Customer:
    def __init__(self):
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestBike(self):
        bikes = input("How many bikes you want to rent?") 

        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not postive integer")
            return -1

        if bikes < 1:
            print("Invalid input. Number of bikes should be greater than 0")
            return -1

        else:
            self.bikes = bikes

        return self.bikes

    def returnBike(self):
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes
        else:
            return 0,0,0   

        

        