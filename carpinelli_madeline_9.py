import urllib.request
cities = ['San Luis Obispo', 'Santa Barbara', 'San Carlos', 'Monterey']
print("Your Weather Report")
print()
print("Current Observations are available for:")
for city in cities:
    print("- " + city)                      # listing all the available cities

print()
user_input = input("Enter the city you would like a weather report for: ").title()
while user_input not in cities:
    user_input = input("No data available. Please try another city: ").title()

try:
    url_monterey = 'https://w1.weather.gov/xml/current_obs/KMRY.xml'
    url_san_luis_obispo = 'https://w1.weather.gov/xml/current_obs/KSBP.xml'
    url_santa_barbara = 'https://w1.weather.gov/xml/current_obs/KSBA.xml'
    url_san_carlos = 'https://w1.weather.gov/xml/current_obs/KSQL.xml'
    if user_input == 'Monterey':
        page = urllib.request.urlopen(url_monterey)
    elif user_input == 'San Luis Obispo':
        page = urllib.request.urlopen(url_san_luis_obispo)
    elif user_input == 'Santa Barbara':
        page = urllib.request.urlopen(url_santa_barbara)
    elif user_input == 'San Carlos':
        page = urllib.request.urlopen(url_san_carlos)
    source_code = page.read()
    source_code = source_code.decode('utf-8')
    #print(source_code)
except:
    print("problem :((((")
else:





                                                            #   sorting imported info 





## The location of the weather reading
## The current weather reading
## The current temperature reading (in degrees F)
## The current relative humidity (in %)
## The current wind conditions (direction, strength (mph), kt)
## The date and time of the weather observation

    find_begin = ['<location>', '<weather>', '<temp_f>', '<relative_humidity>', '<wind_dir>', '<wind_mph>', '<wind_kt>', '<observation_time>']
    find_ending = ['</location>', '</weather>', '</temp_f>', '</relative_humidity>', '</wind_dir>', '</wind_mph>', '</wind_kt>', '</observation_time>']
    
    conditions = {'Location': '', 'Weather': '', 'Temp (F)': '', 'Humidity': '', 'Wind Direction': '', 'Wind Speed': '', 'Wind KT': '', 'Observation Time': ''}



    for i in range(len(find_begin)):
        x = source_code.find(find_begin[i]) + len(find_begin[i])
        y = source_code.find(find_ending[i])
        condition = source_code[x:y]
        if i == 0:
            conditions['Location'] = condition
        elif i == 1:
            conditions['Weather'] = condition
        elif i == 2:
            conditions['Temp (F)'] = condition
        elif i == 3:
            conditions['Humidity'] = condition
        elif i == 4:
            conditions['Wind Direction'] = condition
        elif i == 5:
            conditions['Wind Speed'] = condition
        elif i == 6:
            conditions['Wind KT'] = condition
        elif i == 7:
            conditions['Observation Time'] = condition








                                                            #   printing the requested weather info






    print()
    options = ['location', 'weather', 'temperature', 'humidity', 'wind', 'observation']
    print("Information available:")
    for i in options:
        print('-', i)
    user_input2 = "this doesn't matter"
    while user_input2 != 'done':
        print()
        user_input2 = input('What weather information would you like? (enter "done" to end) ')
        if user_input2 not in options and user_input2 != 'done':
            print('That data is not available')
        elif user_input2 == 'location':
            print('This weather data is recorded in ' + conditions['Location'] + '.')
        elif user_input2 == 'weather':
            print('The weather in ' + user_input.title() + ' is ' + conditions['Weather'].lower() + '.')
        elif user_input2 == 'temperature':
            print('The temperature in ' + user_input.title() + ' is ' + conditions['Temp (F)'] + 'F.')
        elif user_input2 == 'humidity':
            print('The humidity in ' + user_input.title() + ' is ' + conditions['Humidity'] + '%.')
        elif user_input2 == 'wind':
            print('The wind in ' + user_input.title() + ' is ' + conditions['Wind Direction'].lower() + ' at ' + conditions['Wind Speed'] + 'mph (' + conditions['Wind KT'] + ' KT).')
        elif user_input2 == 'observation':
            print('The observation time for ' + user_input.title() + ' is ' + conditions['Observation Time'] + '.')






                                                            #   data visualization






    print()
    user_input3 = input('Would you like to export the weather report and generate a data visualization? (yes/no) ')
    if user_input3 == 'yes':
        # create weather report

        weather_report = open('weather_report', 'w')
        weather_report.write('Weather for ' + user_input.title())
        weather_report.write('\n')
        weather_report.write('\n')
        weather_report.write('Location: ' + conditions['Location'])
        weather_report.write('\n')
        weather_report.write('Weather: ' + conditions['Weather'])
        weather_report.write('\n')
        weather_report.write('Temperature: ' + conditions['Temp (F)'] + 'F')
        weather_report.write('\n')
        weather_report.write('Humidity: ' + conditions['Humidity'] + '%')
        weather_report.write('\n')
        # Wind: from the West at 9.2 gusting to 18.4 MPH (8 gusting to 16 KT)
        weather_report.write('Wind: from the ' + conditions['Wind Direction'] + ' gusting at ' + conditions['Wind Speed'] + 'mph (' + conditions['Wind KT'] + ' KT)')
        weather_report.write('\n')
        weather_report.write('Observation: ' + conditions['Observation Time'])
        weather_report.close()
        print()
        print("Check your finder, there's a surprise for you ;)")
        print()

        # generate data visualization

        print('turtle time!')
        print()

        import turtle
        turtle.setup(width=600, height=600)
        turtle.setworldcoordinates(0,0,600,600)
        weather_condition = conditions['Weather'].lower()
        turtle.tracer(0)
        def cloud(scalar, x, y):
            z = 20 * scalar
            turtle.penup()
            turtle.goto(x,y)
            turtle.pendown()
            turtle.fillcolor('grey')
            turtle.begin_fill()
            turtle.right(45)
            turtle.circle(z,180)
            turtle.right(135)
            turtle.circle(z,180)
            turtle.right(135)
            turtle.circle(z,180)
            turtle.right(135)
            counter = 0
            while counter < 2:
                turtle.circle(z,180)
                turtle.right(180)
                counter += 1
            counter = 0
            while counter < 4:
                turtle.circle(z,180)
                turtle.right(135)
                counter += 1
            counter = 0
            while counter < 3:
                turtle.circle(z,180)
                turtle.right(180)
                counter += 1
            turtle.end_fill()
            

        def raindrop(scalar):
            turtle.pencolor('blue')
            import random
            length = 5 * scalar
            x = random.randint(0,600)
            y = random.randint(0,600)
            turtle.penup()
            turtle.goto(x,y)
            turtle.pendown()
            turtle.seth(45)
            turtle.forward(length)
            
            
        if weather_condition == 'partly cloudy':
            turtle.bgcolor('light blue')
            cloud(1, 100, 400)
            cloud(1, 500, 100)
            cloud(1, 200, 300)
            cloud(1, 100, 100)
            cloud(1, 500, 400)

        elif weather_condition == 'a few clouds':
            turtle.bgcolor('light blue')
            cloud(1, 100, 400)
            cloud(1, 500, 100)

        elif weather_condition == 'fair':
            turtle.bgcolor('light blue')

        elif weather_condition == 'mostly cloudy':
            turtle.bgcolor('light grey')
            cloud(1, 100, 400)
            cloud(1, 500, 100)
            cloud(1, 200, 300)
            cloud(1, 100, 100)
            cloud(1, 500, 400)
            
        elif weather_condition == 'fog/mist':
            turtle.bgcolor('grey')
            for x in range(100):
                raindrop(1)

        elif weather_condition == 'fog':
            turtle.bgcolor('light grey')

        elif weather_condition == 'overcast':
            turtle.bgcolor('dark grey')
            cloud(1, 100, 400)
            turtle.seth(0)
            cloud(1, 500, 100)
            turtle.seth(0)
            cloud(1, 200, 300)
            turtle.seth(0)
            cloud(1, 100, 100)
            turtle.seth(0)
            cloud(1, 500, 400)

        else:
            print('visualization unavailable')
            
    
        
                  















            
        
        
