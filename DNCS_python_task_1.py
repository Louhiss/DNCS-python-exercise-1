import json

# 1. tehtava

class Listcalculate:
    def __init__(self,input_list):
        self.list = input_list

    def calculate_words(self):
        calculate = 0
        for y in self.list:
            if (len(y) >= 2) and y[0] == y[-1]:
                calculate += 1
        print(calculate)

list = Listcalculate(["kasik", "jalkaj", "sormi", "rinta", "varvasv" ])
list.calculate_words()

# tehtava 2

list2 = {"type": "LoRa-sensor", "identifier": "ABC-123", "location": 15701}
print(list2)
formatted = json.dumps(list2,
                       indent = 4,
                       separators = (", " , " = "),
                       sort_keys = True
                       )

print(formatted)





f = open("written.json","w")
f.write(formatted)

f.close()

# tehtava 3

with open('weather-data.json') as weather_data_dict:
    read_content = json.load(weather_data_dict)
    weatherStations_data = read_content['weatherStations']  # making a list of a dict

    for getting_data in weatherStations_data:
        # access weatherStation

        sensorValues_access = getting_data['sensorValues']
        #

        for sensorValues_data in sensorValues_access:
            # access sensorValues
            getting_sensorvalue_data = sensorValues_data['sensorValue']


    def get_sensor_value_data():
        weatherStations_data = read_content['weatherStations']
        for getting_data in weatherStations_data:
            sensorValues_access = getting_data['sensorValues']
            for sensorValues_data in sensorValues_access:
                getting_sensorvalue_data = sensorValues_data['sensorValue']
                name_check = sensorValues_data['name']
                if name_check == 'PINTASIGNAALI_1' or name_check == 'PINTASIGNAALI_2':
                    new_data.append(getting_sensorvalue_data)


    new_data = []
    get_sensor_value_data()

    filtered_measurements = json.dumps(new_data, indent=4, separators=(",", " :"), sort_keys=True, )
    b = open('filtered_measurements.json', 'w')
    b.write(filtered_measurements)
    b.close()

    avg_sensorValue = sum(new_data) / len(filtered_measurements)
    print(avg_sensorValue)