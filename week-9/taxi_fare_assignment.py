#Author: Chris Ibraheem

def fare_calculator(kilometers):
    '''
    Prints the total_price of the taxi ride as a double precision float.
    1. Calculates travel price by:
        - taking kilometers from argument in the function call
        - converting kilometers to meters
        - dividing the total number of meters by 140
        - multiplying that result by 0.25
    2. The BASE_PRICE of $4 is then initialized
    3. total_fare takes the sum of the base_price and travel_price
    4. formatted_fare is the same as total_fare but takes only two decimal places
    5. It then prints the result of formatted_fare
    (No return from this function)
    '''
    #calculates the amount of times they travelled 140 meters
    hundred_forty_count = int((kilometers * 1000) / 140)
    #calculate travel_price ($0.25 per 140m travelled)
    travel_price = 0.25 * hundred_forty_count
    #set BASE_PRICE constant value
    BASE_PRICE = 4
    #total_fare sums the two previous values
    total_fare = BASE_PRICE + travel_price
    #take only two decimal places here with formatted_fare
    formatted_fare = "${:.2f}".format(total_fare)
    #return the result!
    return formatted_fare