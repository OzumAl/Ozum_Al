# This program calculates the total holiday cost after receiving the input from the users.


# Asks user to make a choice between 3 cities.  
city_flight = input("Choose the city you are flying to \n London \n Amsterdam \n Berlin \n: ").capitalize()

# Asks user's input for the number of the nights to stay in the hotel.
num_nights = int(input("How many nights would you like to stay?: "))

# Asks user's input for the number of the days for car rental.
rental_days = int(input("For how many days do you need to rent the car?: "))

# This function calculates the flight and returns the total cost of the flight.
def plane_cost(city_flight):
    if city_flight == "Amsterdam":
     return 65
    elif city_flight == "London": 
     return 90
    else:
     return 40
flight_total = plane_cost(city_flight)
print(f"Your return flight is £{flight_total}.")

# This function calculates the hotel stay and returns the total cost of the hotel.
def hotel_cost(num_nights):
    return num_nights * 100
hotel_total = hotel_cost(num_nights)
print(f"Your hotel stay will cost £{hotel_total}.")

# This function calculates the car rental and returns the total cost of the rental.
def car_rental(rental_days):
    return rental_days * 25
car_total = car_rental(rental_days)
print(f"Your car rental will cost £{car_total}.")

# This function to calculate the total cost of the holiday.
def holiday_cost(hotel_total, car_total, flight_total):
    return hotel_total + car_total + flight_total
total_holiday = holiday_cost(hotel_total, car_total, flight_total)
print(f"The personalised holiday package is £{total_holiday} for you!")
