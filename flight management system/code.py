#FLIGHT MANAGEMENT SYSTEM
from datetime import datetime

""" OOP Requirements
- OOP
    - 5 classes, three of them as parent or children class
    - three vars, constructor and str
    - 3 user function to add new object, delete records, and search for record

- Search and Sorting -> do list of flights
    - linear, sorted linear, and binary search
    - bubble sort, insertion sort, and selection sort

- File processing -> do departures and arrivals
    - option to write/append to a file on prompt
    - add option to save all entered data into a file
    - add option to read previously saved data and display into console

- presentation and answer oral questions

"""

class Airport:
    def __init__(self, name, code, city, country):
        self._name = None
        self._code = None
        self._city = None
        self._country = None

        self.set_name(name)
        self.set_code(code)
        self.set_city(city)
        self.set_country(country)

    def get_name(self):
        return self._name

    def get_code(self):
        return self._code
    
    def get_city(self):
        return self._city
    
    def get_country(self):
        return self._country
    
    def set_name(self, name):
        self._name = name

    def set_code(self, code):
        if type(code) is str and code.isalpha():
            if len(code) == 3:
                self._code = code
            else : 
                print('Code must be no more or less than 3 letters')

        else:
            print('Code type must be str or alphabets only')
    
    def set_city(self, city):
        self._city = city
    
    def set_country(self, country):
        self._country = country

    
    def __str__(self):
        return f"Airport {self._name} ({self._code}) is located in {self._city}, {self._country}"
    
class Terminal(Airport):
    def __init__(self, name, code, city, country, number, gate):
        super().__init__(name, code, city, country)
        self._number = 1
        self._gate = 1

        self.set_number(number)
        self.set_gate(gate)

    def get_number(self):
        return self._number
    
    def get_gate(self):
        return self._gate
    
    def set_number(self, number):
        if type(number) == int:
            self._number = number
        else :
            self._number = 1
            print('Invalid input, default value of 1 is inputted')
    
    def set_gate(self, gate):
        if type(gate) == int:
            self._gate = gate
        else:
            self._gate = 1
            print('Invalid input, default value of 1 Inputted')

    def is_big(self):
        if self._number >= 2:
            return "Airport is big and famous"
        else:
            if self._gate >= 8:
                return "Airport is big"
            else :
                return "Airport is small"

    def __str__(self):
        return f'{super().get_name()} Terminal {self._number} Gate {self._gate}'

class Airline:
    def __init__(self, name, origin_country, airline_code, age):
        self._name = None
        self._origin_country = None
        self._airline_code = None
        self._age = 0

        self.set_name(name)
        self.set_origin_country(origin_country)
        self.set_airline_code(airline_code)
        self.set_age(age)

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_origin_country(self):
        return self._origin_country
    
    def set_origin_country(self, origin_country):
        self._origin_country = origin_country

    def get_airline_code(self):
        return self._airline_code
    
    def set_airline_code(self, airline_code):
        if type(airline_code) == str and airline_code.isalnum():
            if len(airline_code) == 3 :
                self._airline_code = airline_code

            else :
                print("Airline code must not be less/more than 2 Characters")
        else:
            print("Input must be str and must consist of alphabets and numeric numbers")
    
    def get_age(self):
        return self._age
    
    def set_age(self,age):
        if type(age) == int :
            self._age = age
        else:
            print('Age must be numeric number')
    
    def is_old(self):
        if self._age > 50 :
            return "Airline company is old"
        else:
            return "Airline company is relatively young"
        
    def is_famous(self):
#using sorted linear search,check if names first char's binary is larger than element's first char binary, 
        famous_list = ['ANA',"Qantas","SingaporeAirlines",'Korean Air', 'Emirates',"Delta",'British Airways']
        famous_list = famous_list.sort()
        for i in famous_list:
            if self._name in famous_list:
                return "Airline is Famous"
            elif self._name[0] > i[0]:
                return "Airline is not Famous"
        return "Airline is not Famous"

    def __str__(self):
        return f"{self._name} ({self._airline_code}) is from {self._origin_country} and is {self._age}"
        
class Information:
    def __init__(self, terminal, date, time):
        self._port = terminal
        self._date = None
        self._time = None

        self.set_date(date)
        self.set_time(time)

    def get_port(self):
        return self._port

    def get_date(self):
        return self._date
    
    def get_time(self):
        return self._time
    
    def date_validation(self, date_str, date_format = '%d-%m-%Y'):
        try:
            datetime.strptime(date_str, date_format)
            return True
        except ValueError:
            return False
    
    def time_validation(self, time_str, time_format = '%H:%M'):
        try:
            datetime.strptime(time_str, time_format)
            return True
        except ValueError:
            return False
        

    def set_date(self, date):
        if self.date_validation(date):
            self._date = date
        else :
            print('Wrong date format')
    
    def set_time(self, time):
        #time validation
        if self.time_validation(time):
            self._time = time
        else :
            print('Wrong time format')

    def __str__(self):
        return f"Airport {self._port.get_name()} at {self._date} {self._time}"

class Departure(Information): 
    def __init__(self, terminal, date, time, num_of_passenger):
        super().__init__(terminal, date, time)
        self._num_of_passenger = 0

        self.set_num_of_passenger(num_of_passenger)
    
    def get_num_of_passenger(self):
        return self._num_of_passenger

    def set_num_of_passenger(self, num_of_passenger):
        if 0 <= num_of_passenger <= 850:
            self._num_of_passenger = num_of_passenger
        else :
            if num_of_passenger < 0:
                print('num of passenger needs to be zero or more, min value(0) assigned')
                self._num_of_passenger = 0
            elif  num_of_passenger > 850:
                print('num of passenger cannot be more than 850, max value (850) assigned')
                self._num_of_passenger = 850

    def odd_even(self):
        if self._num_of_passenger%2 == 0 :
             return "Flight has even passenger number"
        else:
            return "Flight has odd passenger number"

    def check_time(self):
        if "07:00" <= self._time < "12:00":
            return "Departure is in the morning"
        elif "12:00" <= self._time <= "18:00":
            return "Departure is in the afternoon"
        else:
            return "Departure is in the evening"

    def __str__(self):
        return f"Departure from {self._port.get_name()}, {self._port.get_city()} with {self._num_of_passenger} passanger at {self._date} {self._time}\n"
    
class Arrival(Information): 
    def __init__(self, terminal, date, time, runway):
        super().__init__(terminal, date, time)
        self._runway = None

        self.set_runway(runway)

    def get_runway(self):
        return self._runway

    def set_runway(self, runway):
        if len(runway) <= 3:
            self._runway = runway
        else:
            print('Runway must be 3 or less alphanumeric characters')

    def check_time(self):
        if "07:00" <= self._time < "12:00":
            return "Arrival is in the morning"
        elif "12:00" <= self._time <= "18:00":
            return "Arrival is in the afternoon"
        else:
            return "Arrival is in the evening"

    def __str__(self):
        return f"Arrival at {self._port.get_name()}, {self._port.get_city()} on runway {self._runway} at {self._date} {self._time}\n"

class Flight:
    def __init__(self, flightid, departure, arrival, airline):
        self._flightid = None
        self._departure = departure
        self._arrival = arrival
        self._airline = airline

        self.set_flightid(flightid)

    def get_flightid(self):
        return self._flightid
    
    def set_flightid(self, flightid):
        if len(flightid) <= 6 and flightid.isalnum():
            self._flightid = flightid
        else :
            print('Flightid must be 6 or less alphanumeric characters')
    
    def get_departure(self):
        return self._departure
    
    def get_arrival(self):
        return self._arrival
    
    def get_airline(self):
        return self._airline
    
    def get_duration(self):
        format = '%d-%m-%Y %H:%M'
        start_time = datetime.strptime(f"{self._departure._date} {self._departure._time}", format)
        end_time = datetime.strptime(f"{self._arrival._date} {self._arrival._time}", format)
        duration = end_time - start_time
        return duration
    
    def get_velocity(self):
        print('Welcome to Velocity Check')
        distance = int(input('Input flight distance [in km]]: '))
        duration = self.get_duration()
        velocity = distance/ ((duration.days*86400)+duration.seconds)
        return f"{velocity} km/s"
    
    def is_overnight(self):
        if self._arrival.get_date() > self._departure.get_date():
            return "Overnight Flight"

        else:
            return "Same day Flight"

    def __str__(self):
        return f"""Flight {self._flightid} 
Departing City: {self._departure._port._name}, {self._departure._port._city} 
Arrival City: {self._arrival._port._name}, {self._arrival._port._city} 
Departure: {self._departure.get_date()} {self._departure.get_time()}
Arrival: {self._arrival.get_date()} {self._arrival.get_time()}
Duration : {self.get_duration()}
"""
        
def add_flight():
    while True:
        try:
            flight_no = input('Input Flight ID/ Number: ')
            new_dp = addition(5)
            new_arr = addition(6)
            print(new_dp.get_date())
            print(new_arr.get_date())
            print(new_dp.get_date() < new_arr.get_date())
            if new_dp.get_date() > new_arr.get_date():
                raise ValueError('Arrival Date must not be earlier than Departure date')
            elif new_dp.get_date() == new_arr.get_date:
                if new_dp.get_time() < new_arr.get_time():
                    raise ValueError('Arrival time must not be earlier than Departure time')
                else:
                    continue
            else :
                print('Please select Airline from the list below')
                for i in range(len(airline_list)):
                    print(f'{i+1}. {airline_list[i].get_name()}')
                usr_airline_choice = int(input(f'Please make your airline selection [1-{i+1}]'))
                if usr_airline_choice<0 or usr_airline_choice> len(airline_list):
                    raise ValueError(f'Selection Error! Value must be between 1 to {len(airline_list)}')
                else :
                    if usr_airline_choice == 1:
                        usr_airline = Qantas
                    elif usr_airline_choice == 2:
                        usr_airline = KoreanAir
                    elif usr_airline_choice == 3:
                        usr_airline = SingaporeAir
                    else :
                        usr_airline = Emirates
                new_flight = Flight(flight_no, new_dp, new_arr, usr_airline)
                return new_flight
        except ValueError:
            print('Value Error, please reinput error value')

def add_date():
    while True:
        try:
            month = int(input('Please enter month [1-12]: '))
            if month <= 0 or month > 12:
                raise ValueError('month must be more than 0 or less than 12')
            date = int(input('Please enter day [1-31]: '))
            if month in [2,4,6,9,11]:
                if date<=0 or date>30:
                    raise ValueError(f'invalid date for month {month}. Date must be more than 0 or less than 30')
            else :
                if date<=0 or date > 31 :
                    raise ValueError(f'Date must be more than 0 or less than 31')
            year = int(input('Please enter year: '))
            datetime.strptime(f'{date}-{month}-{year}', '%d-%m-%Y')
            return f'{date}-{month}-{year}'
        except ValueError:
            print('Invalid format')

def add_time():
    while True:
        try:
            hour = int(input('Please enter hour [00-23]: '))
            if hour<0 or hour>24:
                raise ValueError('Hour must be positive number and less than 24')
            minutes = int(input('Please enter minutes [0-59]: '))
            if minutes < 0 or minutes > 60:
                raise ValueError('Minutes must be positive number or less than 60')
            datetime.strptime(f'{hour}:{minutes}', '%H:%M')
            return f'{hour}:{minutes}'
        except ValueError:
            print('Invalid format')

def addition(selection):
    while True:
        try :
            print('New Departure/Arrival Menu')
            print('Airport List')
            for i in range(len(terminal_list)):
                print(f'{i+1}. {terminal_list[i].get_name()}')
            new_airport_choice = int(input(f'Please make a selection of Airport[1-{i+1}]: '))
            if new_airport_choice <=0 or new_airport_choice >len(terminal_list):
                raise ValueError(f'Choice value must be more than 0 or less than {len(terminal_list)}')
            #terminal_list = [London_Terminal, Newyork_Terminal, Singapore_Terminal, Seoul_Terminal, Sydney_Terminal]
            else :
                if new_airport_choice == 1:
                    new_airport = London_Terminal
                elif new_airport_choice == 2:
                    new_airport = Newyork_Terminal
                elif new_airport_choice == 3:
                    new_airport = Singapore_Terminal
                elif new_airport_choice ==4 :
                    new_airport = Seoul_Terminal
                elif new_airport_choice == 5:
                    new_airport = Sydney_Terminal
            print("Input date")
            new_date = add_date()
            print("Input time")
            new_time = add_time()
            if selection == 5:
                dp_pass = int(input('Input passanger count: '))
                new_dp = Departure(new_airport, new_date, new_time, dp_pass)
                return new_dp
            elif selection == 6:
                arr_runway = input('Input Runway: ')
                new_arr = Arrival(new_airport, new_date, new_time, arr_runway)
                return new_arr
        except ValueError: 
            print('Value error, Please reinput')

def cont():
    c = str(input('continue/ add more? [y/n] :'))
    if c.lower() == 'y':
        return True
    elif c.lower() == 'n':
        return False
    else :
        raise ValueError('Wrong choice only y/n')

def write_to_file(file_obj, obj):
    write_choice = input('Would you like to save selection to file [y/n]: ')
    if write_choice.lower() == 'y':
        file_obj.seek(0)
        lines = file_obj.readlines()
        if str(obj) in lines:
            print('Input already exists in file, cancelling save')
        else :
            file_obj.write(str(obj))
            print('Input successfully saved')
        return True
    else :
        print('Input added to list! You can add everything later')
        return False

def text_search(target, source):
    result_list = []
    for i in source:
        if target in i:
            result_list.append(i)
    
    if len(result_list) > 0:
        return result_list
    else :
        return f"Target not found"
    
def flight_text_search(target, source, choice):
    result_list = []
    if choice ==1 :
        for i in range(0,len(source),6):
            if target in source[i+1]:
                for j in range(i,i+6):
                    result_list.append(source[j])
    elif choice == 2:
        for i in range(0,len(source),6):
            if target in source[i+2]:
                for j in range(i,i+6):
                    result_list.append(source[j])
    
    if len(result_list) > 0:
        return result_list
    else :
        return f"Target not found"

def number_search(target, source):
    #binary search
    low = 0
    high = len(source)
    while low <= high:
        mid = (low+high)//2
        if target == source[mid]:
            return True
        elif target > source[mid]:
            low = mid+1
        else:
            high = mid - 1
    return False

#Terminal
London_Terminal = Terminal("London Heathrow","LHR","London", "United Kingdom",5,10)
Newyork_Terminal = Terminal("New York JFK", "JFK", "New York", "USA",2,3)
Singapore_Terminal = Terminal("Changi Airport", "SIN", "Singapore", "Singapore",1,9)
Sydney_Terminal = Terminal("Kingsford Smith", "SYD", "Sydney", "Australia",1,7)
Seoul_Terminal= Terminal("Incheon Airport", "ICN", "Seoul", "South Korea",1,8)

terminal_list = [London_Terminal, Newyork_Terminal, Singapore_Terminal, Seoul_Terminal, Sydney_Terminal]

#Airline
Qantas = Airline('Qantas',"Australia","QFA",102)
KoreanAir = Airline('Korean Air',"South Korea","KAL",54)
SingaporeAir = Airline('Singapore Airlines',"Singapore","SIA",51)
Emirates = Airline('Emirates',"United Arab Emirates","UAE",38)

airline_list = [Qantas, KoreanAir, SingaporeAir, Emirates]

#Departure
sydney_dep = Departure(Sydney_Terminal, "01-10-2023","23:55",680)
ny_dep = Departure(Newyork_Terminal, "01-10-2023","17:00",800)
sg_dep = Departure(Singapore_Terminal,"02-10-2023","17:00",800)

#Arrival
ny_arr = Arrival(Newyork_Terminal, "03-10-2023","15:20",'12F')
sydney_arr = Arrival(Sydney_Terminal, "06-10-2023","00:30",'22R')
sg_arr = Arrival(Singapore_Terminal,"02-10-2023","00:30",'23R' )

#Flight
nysyd = Flight('QA18', ny_dep, sydney_arr, Qantas)
sgny = Flight('SQ24', sg_dep, ny_arr, SingaporeAir)
nysg = Flight('ER09', ny_dep,sg_arr, Emirates)
sydsg = Flight('QA23', sydney_dep, sg_arr, Qantas)
sydny = Flight('SQ13', sydney_dep,ny_arr, SingaporeAir)

#main code body
def main():
    con = True
    flight_file = open('flight.txt','a+')
    departure_file = open('departures.txt','a+')
    arrival_file = open('arrivals.txt','a+')

    flights_tmp = [nysg, sgny, sydsg]
    departure_tmp = []
    arrival_tmp = []

    #  a few more user defined functions in the classes
    while con:
        try : 
            print("""Welcome to Flight Management System.
    Please make a choice.
    1. Show or Search Flights
    2. Show or Search Departures
    3. Show or Search Arrivals
    4. Add Flight
    5. Add Departures
    6. Add Arrivals
    7. Delete Record
    8. Save all to file
    9. Sorting Menu""")
            usr_choice = int(input("Please make a choice :"))
            if usr_choice < 0 or usr_choice > 9:
                raise ValueError
            if usr_choice == 1: #done 
                count = 0
                fl_choice = int(input('Please make a selection\n1. Show All flight\n2. Search flight\nSelection: '))
                if fl_choice == 1:
                    fl_choice2 = int(input('Please make a selection\n1. Show Saved flight\n2. Show inputted flight\nSelection: '))
                    if fl_choice2 == 1:
                        flight_file.seek(0)
                        flights_list = flight_file.readlines()
                        for i in flights_list:
                            count += 1
                            print(i.strip('\n'))
                    elif fl_choice2 == 2:
                            fl_choice3 = int(input('Inputted Flight selection\n1. Show all\n2.Show all sorted by duration\nSelection: '))
                            if fl_choice3 == 1:
                                for i in flights_tmp:
                                    count += 1
                                    print(str(i))
                            elif fl_choice3 ==2 : #bubble sort based on duration
                                for i in range(len(flights_tmp)):
                                    for j in range(len(flights_tmp)-1):
                                        if (flights_tmp[j].get_duration().seconds + (flights_tmp[j].get_duration().days*86400)) > (flights_tmp[j+1].get_duration().seconds + (flights_tmp[j+1].get_duration().days*86400)):
                                            flights_tmp[j], flights_tmp[j+1] = flights_tmp[j+1], flights_tmp[j]
                                for i in flights_tmp:
                                    count += 1
                                    print(i)
                            else :
                                raise ValueError('Option limited to 1-2')
                    else :
                        raise ValueError('Option limited to [1-2]')

                    if count == 0:
                        print('No record found')

                elif fl_choice ==2 :
                    fl_choice2 = int(input('Please make a selection\n1. Search Saved flight\n2. Search inputted flight\nSelection: '))
                    if fl_choice2 == 1 or fl_choice2 == 2:
                        fl_choice3 = int(input('Select Search Criteria\n1. Departing City\n2. Arrival City\nSelection: '))

                        if fl_choice3 == 1:
                            option = "Departure"
                        elif fl_choice3 == 2:
                            option = "Arrival"
                        else :
                            raise ValueError('Choice must be either 1 or 2.')
                        city_choice = str(input(f'Please enter {option} city name: '))
                        if fl_choice2 == 1:
                            flight_file.seek(0)
                            flights_list = flight_file.readlines()
                            if fl_choice3 == 1:
                                result = flight_text_search(city_choice, flights_list, fl_choice3)
                            if type(result) == list:
                                for i in result:
                                    print(i.strip('\n'))
                            else:
                                print(result)
                        elif fl_choice2 == 2:
                            flights_list = []
                            for i in flights_tmp:
                                tmp = str(i).split('\n')
                                for j in tmp:
                                    if j == '':
                                        continue
                                    else:
                                        flights_list.append(j)
                            result = flight_text_search(city_choice, flights_list, fl_choice3)
                            print(result)
                            if type(result) == list:
                                for i in result:
                                        print(i.strip('\n'))
                            else:
                                print(result)

                        else :
                            print('Choice is limited to [1-2]. Please try again.')
                    else:
                        print('Choice is limited to [1-2]. Please try again.')
                else:
                    print('Choice is limited to [1-2]. Please try again.')
                
            elif usr_choice == 2:#done
                count = 0
                dep_choice = int(input('Please make a selection\n1. Show All Departure\n2. Search Departure\nSelection: '))
                if dep_choice == 1:
                    dep_choice2 = int(input('Please make a selection\n1. Show Saved Departure\n2. Show inputted Departure\nSelection: '))
                    if dep_choice2 == 1:
                        departure_file.seek(0)
                        departures_list = departure_file.readlines()
                        for i in departures_list:
                            count +=1 
                            print(i.strip('\n'))
                    elif dep_choice2 == 2:
                        for i in departure_tmp:
                            count += 1
                            print(str(i))
                    if count == 0 :
                        print('No record found')

                elif dep_choice ==2 :
                    dep_choice2 = int(input('Please make a selection\n1. Search Saved Departure\n2. Search inputted Departure\nSelection: '))
                    if dep_choice2 == 1 or dep_choice2 == 2:
                        city_choice = str(input('Please enter city name: '))
                        if dep_choice2 == 1:
                            departure_file.seek(0)
                            departures_list = departure_file.readlines()
                            result = text_search(city_choice, departures_list)
                            if type(result) == list:
                                for i in result:
                                    print(i)
                            else:
                                print(result)
                        elif dep_choice2 == 2:
                            city_list = []
                            for i in departure_tmp:
                                city_list.append(str(i))
                            result = text_search(city_choice, city_list )
                            if type(result) == list:
                                for i in result:
                                    print(i)
                            else:
                                print(result)

                    else:
                        print('Choice is limited to [1-2]. Please try again.')
                else:
                    print('Choice is limited to [1-2]. Please try again.')
                    
            elif usr_choice == 3:#done
                count = 0
                arr_choice = int(input('Please make a selection\n1. Show All arrival\n2. Search arrival\nSelection: '))
                if arr_choice == 1:
                    arr_choice2 = int(input('Please make a selection\n1. Show Saved arrival\n2. Show inputted arrival\nSelection: '))
                    if arr_choice2 == 1:
                        arrival_file.seek(0)
                        arrivals_list = arrival_file.readlines()
                        for i in arrivals_list:
                            count += 1
                            print(i.strip('\n'))
                    elif arr_choice2 == 2:
                        for i in arrival_tmp:
                            count += 1
                            print(str(i))
                    if count == 0:
                        print('No record found')
                elif arr_choice ==2 :
                    arr_choice2 = int(input('Please make a selection\n1. Search Saved arrival\n2. Search inputted arrival\nSelection: '))
                    if arr_choice2 == 1 or arr_choice2 == 2:
                        city_choice = str(input('Please enter city name: '))
                        if arr_choice2 == 1:
                            arrival_file.seek(0)
                            arrivals_list = arrival_file.readlines()
                            result = text_search(city_choice, arrivals_list)
                            if type(result) == list:
                                for i in result:
                                    print(i)
                            else:
                                print(result)
                        elif arr_choice2 == 2:
                            city_list = []
                            for i in arrival_tmp:
                                city_list.append(str(i))
                            result = text_search(city_choice, city_list)
                            if type(result) == list:
                                for i in result:
                                    print(i)
                            else:
                                print(result)

                    else:
                        print('Choice is limited to [1-2]. Please try again.')
                else:
                    print('Choice is limited to [1-2]. Please try again.')

            elif usr_choice == 4: #done
                new_flight = add_flight()
                wrt = write_to_file(flight_file, new_flight)
                if not wrt :
                    flights_tmp.append(new_flight)
            
            elif usr_choice == 5: #done
                new_departure = addition(usr_choice)
                wrt = write_to_file(departure_file, new_departure)
                if not wrt:
                    departure_tmp.append(new_departure)

            elif usr_choice == 6: #done
                new_arrival = addition(usr_choice)
                wrt = write_to_file(arrival_file, new_arrival)
                if not wrt:
                    arrival_tmp.append(new_arrival)

            elif usr_choice == 7 : # done
                dchoice = int(input('Select what you want to delete\n1. Departure\n2. Arrival\nSelection: '))
                if dchoice == 1:
                    ctype = "Departure"
                elif dchoice == 2:
                    ctype = "Arrival"
                else :
                    raise ValueError('Choice must be either 1 or 2')
                choice2 = int(input(f'Please make a selection\n1. Search Saved {ctype}\n2. Search inputted {ctype}\nSelection: '))
                if choice2 == 1 or choice2 == 2:
                    city_choice = str(input('Please enter city name: '))
                    if dchoice == 1:
                        if choice2 == 1:
                            departure_file.seek(0)
                            departures_list = departure_file.readlines()
                            result = text_search(city_choice, departures_list)
                            if type(result) == list and len(result)>=1:
                                for i in range(len(result)):
                                    print(i+1, result[i])
                                del_choice = int(input("Please select the departure record you want to delete: "))
                                if del_choice <= len(result):
                                    del_index = departures_list.index(result[del_choice-1])
                                    departures_list.pop(del_index)
                                    departure_file.seek(0)
                                    departure_file.truncate()
                                    for i in departures_list:
                                        departure_file.write(i)
                                    print('File successfully updated')
                                else:
                                    raise ValueError('No such Departures')
                                
                            else:
                                print(result)

                        elif choice2 == 2:
                            city_list = []
                            for i in departure_tmp:
                                city_list.append(str(i))
                            result = text_search(city_choice, city_list )
                            if type(result) == list and len(result)>=1:
                                for i in range(len(result)):
                                    print(i+1, result[i])
                                del_choice = int(input("Please select the departure record you want to delete: "))
                                if del_choice <= len(result):
                                    del_index = city_list.index(result[del_choice-1])
                                    departure_tmp.pop(del_index)
                                    print('List successfully updated')
                                else:
                                    raise ValueError('No such Arrival')
                            
                    elif dchoice == 2:
                        if choice2 == 1:
                            arrival_file.seek(0)
                            arrivals_list = arrival_file.readlines()
                            result = text_search(city_choice, arrivals_list)
                            if type(result) == list and len(result)>=1:
                                for i in range(len(result)):
                                    print(i+1, result[i])
                                del_choice = int(input("Please select the arrival record you want to delete: "))
                                if del_choice <= len(result):
                                    del_index = arrivals_list.index(result[del_choice-1])
                                    arrivals_list.pop(del_index)
                                    arrival_file.seek(0)
                                    arrival_file.truncate()
                                    for i in arrivals_list:
                                        arrival_file.write(i)
                                    print('File successfully updated')
                                else:
                                    raise ValueError('No such Arrival')

                        elif choice2 == 2:
                            city_list = []
                            for i in arrival_tmp:
                                city_list.append(str(i))
                            result = text_search(city_choice, city_list)
                            if type(result) == list and len(result)>=1:
                                for i in range(len(result)):
                                    print(i+1, result[i])
                                del_choice = int(input("Please select the arrival record you want to delete: "))
                                if del_choice <= len(result):
                                    del_index = city_list.index(result[del_choice-1])
                                    arrival_tmp.pop(del_index)
                                    print('List successfully updated')
                                else:
                                    raise ValueError('No such Arrival')
                            else:
                                print(result)
                else :
                    raise ValueError('Choice must be either 1 or 2')

            elif usr_choice == 8: #done
                flight_file.seek(0)
                departure_file.seek(0)
                arrival_file.seek(0)
                flines = flight_file.readlines()
                dlines = departure_file.readlines()
                alines = arrival_file.readlines()
                for i in range(len(flights_tmp)):
                    if str(flights_tmp[i].get_flightid()) not in flines:
                        flight_file.write(str(flights_tmp[i]))
                    else :
                        print(f'Flight {flights_tmp[i].get_flightid()} is in the system')
                        print('Skipping Input')
                flights_tmp = []

                for i in range(len(departure_tmp)):
                    if str(departure_tmp[i]) not in dlines:
                        departure_file.write(str(departure_tmp[i]))
                    else :
                        print(f'Departure from {departure_tmp[i].get_name()} at {departure_tmp[i].get_date()} {departure_tmp.get_time()} is in the system')
                        print('Skipping Input')
                departure_tmp = []

                for i in range(len(arrival_tmp)):
                    if str(arrival_tmp[i]) not in alines:
                        arrival_file.write(str(arrival_tmp[i]))
                    else :
                        print(f'Departure from {arrival_tmp[i].get_name()} at {arrival_tmp[i].get_date()} {arrival_tmp.get_time()} is in the system')
                        print('Skipping Input')
                arrival_tmp = []
            
            elif usr_choice == 9:
                print('Welcome to showcase of sorting algorithm')
                print("Select sorting algorithm.\n1. Selection sort of flight duration\n2. Insertion sort of airline's age\n3. Bubble sort of number of passanger in a flight")
                sorting_choice = int(input("Please make your selection [1-3]: "))
                if sorting_choice == 1:
                #selection sort
                    for i in range(len(flights_tmp)-1):
                        min_index = i
                        for j in range(i+1, len(flights_tmp)):
                            if flights_tmp[j].get_duration() < flights_tmp[i].get_duration():
                                min_index = j
                        flights_tmp[i], flights_tmp[j] = flights_tmp[j], flights_tmp[i]
                    
                    for i in flights_tmp:
                        print(i)

                elif sorting_choice ==2 :
                    #insertion sort
                    for i in range(1,len(airline_list)):
                        j = 1
                        tmp = airline_list[i]
                        while i>j and j >= 0:
                            if airline_list[i].get_age() < airline_list[j].get_age():
                                airline_list[i] = airline_list[j]
                                airline_list[j] = tmp
                                j -= 1
                    for i in airline_list:
                        print(i)


                elif sorting_choice ==3 :
                #bubble sort
                    for i in range(len(flights_tmp)):
                        for j in range(len(flights_tmp)-1):
                            if flights_tmp[j].get_departure().get_num_of_passenger() > flights_tmp[j+1].get_departure().get_num_of_passenger():
                                flights_tmp[j], flights_tmp[j+1] = flights_tmp[j+1], flights_tmp[j]
                    
                    for i in flights_tmp:
                        print(i,"Number of passanger:",i.get_departure().get_num_of_passenger())

            con = cont()
        except ValueError:
            print('Value Error! Please try Again')

if __name__ == "__main__":
    main()
