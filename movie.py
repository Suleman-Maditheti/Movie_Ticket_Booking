def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Pushpa:
    def __init__(self):
        self.max_tickets = 20
        self.available_seats = [i for i in range(1, self.max_tickets + 1)]
    
    def book(self, no_of_tickets):
        if no_of_tickets <= self.max_tickets:
            
            
            print("Available seats before booking:", self.available_seats)
            self.seat_no(no_of_tickets)
            print(f'Available tickets are {self.max_tickets}')
        else:
            print('Sorry, Tickets Not available')
    
    def seat_no(self, no_of_tickets):
        seat = input('Enter seat numbers to book (separated by space): ')
        try:
            seat_list = list(map(int, seat.split()))
            if all(s in self.available_seats for s in seat_list) and no_of_tickets == len(seat_list):
                self.max_tickets -= no_of_tickets
                self.available_seats = [s for s in self.available_seats if s not in seat_list]
                print('Tickets Booked Successfully')
                print("Remaining seats:", self.available_seats)
            else:
                print("Seats are not available or the number of seats does not match the number of tickets booked")
        except ValueError:
            print("Invalid input")

@singleton
class RRR:
    def __init__(self):
        self.max_tickets = 10
        self.available_seats = [i for i in range(1, self.max_tickets + 1)]
    
    def book(self, no_of_tickets):
        if no_of_tickets <= self.max_tickets:
            
            
            print("Available seats before booking:", self.available_seats)
            self.seat_no(no_of_tickets)
            print(f'Available tickets are {self.max_tickets}')
            
        else:
            print('Sorry, Tickets Not available')
    
    def seat_no(self, no_of_tickets):
        seat = input('Enter seat numbers to book (separated by space): ')
        try:
            seat_list = list(map(int, seat.split()))
            if all(s in self.available_seats for s in seat_list) and no_of_tickets == len(seat_list):
                self.max_tickets -= no_of_tickets
                self.available_seats = [s for s in self.available_seats if s not in seat_list]
                
                print('Tickets Booked Successfully')
                
                print("Remaining seats:", self.available_seats)
            else:
                print("Seats are not available or the number of seats does not match the number of tickets booked")
        except ValueError:
            print("Invalid input")

@singleton
class Kalki:
    def __init__(self):
        self.max_tickets = 10
        self.available_seats = [i for i in range(1, self.max_tickets + 1)]
    
    def book(self, no_of_tickets):
        if no_of_tickets <= self.max_tickets:
            
            
            print("Available seats before booking:", self.available_seats)
            self.seat_no(no_of_tickets)
            print(f'Available tickets are {self.max_tickets}')
        else:
            print('Sorry, Tickets Not available')
    
    def seat_no(self, no_of_tickets):
        seat = input('Enter seat numbers to book (separated by space): ')
        try:
            seat_list = list(map(int, seat.split()))
            if all(s in self.available_seats for s in seat_list) and no_of_tickets == len(seat_list):
                self.max_tickets -= no_of_tickets
                self.available_seats = [s for s in self.available_seats if s not in seat_list]
                print('Tickets Booked Successfully')
                print("Remaining seats:", self.available_seats)
            else:
                print("Seats are not available or the number of seats does not match the number of tickets booked")
        except ValueError:
            print("Invalid input")

def paytm():
    print('1) Pushpa\n2) RRR\n3) Kalki')
    select = int(input('Enter the choice:'))

    if select == 1:
        ob = Pushpa()
        print(f'Maximum tickets are {ob.max_tickets}')
        ob.book(int(input('Enter the number of tickets you want: ')))
    elif select == 2:
        ob = RRR()
        print(f'Maximum tickets are {ob.max_tickets}')
        ob.book(int(input('Enter the number of tickets you want: ')))
    elif select == 3:
        ob = Kalki()
        print(f'Maximum tickets are {ob.max_tickets}')
        ob.book(int(input('Enter the number of tickets you want: ')))
    else:
        print('Movie you want to watch is not available')

def google_pay():
    print('1) Pushpa\n2) RRR\n3) Kalki')
    select = int(input('Enter the choice:'))

    if select == 1:
        ob = Pushpa()
        print(f'Maximum tickets are {ob.max_tickets}')
        ob.book(int(input('Enter the number of tickets you want: ')))
    elif select == 2:
        ob = RRR()
        print(f'Maximum tickets are {ob.max_tickets}')
        ob.book(int(input('Enter the number of tickets you want: ')))
    elif select == 3:
        ob = Kalki()
        print(f'Maximum tickets are {ob.max_tickets}')
        ob.book(int(input('Enter the number of tickets you want: ')))
    else:
        print('Movie you want to watch is not available')

def book_my_show():
    print('1) Pushpa\n2) RRR\n3) Kalki')
    select = int(input('Enter the choice:'))

    if select == 1:
        ob = Pushpa()
        print(f'Maximum tickets are {ob.max_tickets}')
        ob.book(int(input('Enter the number of tickets you want: ')))
    elif select == 2:
        ob = RRR()
        print(f'Maximum tickets are {ob.max_tickets}')
        ob.book(int(input('Enter the number of tickets you want: ')))
    elif select == 3:
        ob = Kalki()
        print(f'Maximum tickets are {ob.max_tickets}')
        ob.book(int(input('Enter the number of tickets you want: ')))
    else:
        print('Movie you want to watch is not available')

paytm()
google_pay()
book_my_show()
