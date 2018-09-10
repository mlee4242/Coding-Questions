'''
given a csv file, calculates and prints out:
minimum, maximum, mean, std
of the csv data in 5 minute intervals/buckets
'''
def calculate_data_stats(csv_name):
    interval_dict = populate_interval_dict(csv_name) #maps an interval string to lists of 2-tuples containing the label and the value
    if interval_dict is None: #only occurs when the .csv file cannot be found
        return

    for interval in sorted(interval_dict): 
        #collect values of each label
        cpu_values = extract_label_values(interval_dict, interval, "cpu")
        memory_values = extract_label_values(interval_dict, interval, "memory")
        disk_values = extract_label_values(interval_dict, interval, "disk")

        #min values of the data
        cpu_min = min(cpu_values)
        memory_min = min(memory_values)
        disk_min = min(disk_values) 

        #max values of the data
        cpu_max = max(cpu_values)
        memory_max = max(memory_values)
        disk_max = max(disk_values)

        #mean values of the data
        cpu_mean = calculate_mean(cpu_values)
        memory_mean = calculate_mean(memory_values)
        disk_mean = calculate_mean(disk_values)

        #std values of the data
        cpu_std = calculate_std(cpu_values, cpu_mean)
        memory_std = calculate_std(memory_values, memory_mean)
        disk_std = calculate_std(disk_values, disk_mean)

        #lots of print statements to make it nice to look at in the console/terminal
        print ("\n" + interval + ":" + "\n")
        print ("CPU:")
        print ("---------------")
        print ("Max: " + str(cpu_max))
        print ("Min: " + str(cpu_min))
        print ("Mean: " + str(cpu_mean))
        print ("Std: " + str(cpu_std) + "\n")
        print ("Memory:")
        print ("---------------")
        print ("Max: " + str(memory_max))
        print ("Min: " + str(memory_min))
        print ("Mean: " + str(memory_mean))
        print ("Std: " + str(memory_std) + "\n")
        print ("Disk:")
        print ("---------------")
        print ("Max: " + str(disk_max))
        print ("Min: " + str(disk_min))
        print ("Mean: " + str(disk_mean))
        print ("Std: " + str(disk_std) + "\n")

'''
populates an interval_dict by reading
the provided csv_file, csv_name
'''
def populate_interval_dict(csv_name):
    interval_dict = {}

    try:
        csv = open(csv_name)
    except FileNotFoundError:
        print ("Cannot find " + csv_name)
        return None

    next(csv) #skip the labels on the first line
    for line in csv:
        data = line.split(',')
        label, timestamp, value = data[0], data[1], data[2][:-1] #[:-1] gets rid of the end '\n'
        bucket = determine_bucket (timestamp)
        if bucket not in interval_dict:
            interval_dict[bucket] = [(label, value)]
        else:
            interval_dict[bucket].append([label, value])       
    csv.close()

    return interval_dict

'''
given a timestamp string, 
return a string indicating 
which 5 min interval the timestamp is in
'''
def determine_bucket(timestamp):
    timestamp_split = timestamp.split(":")
    #get the ones digit of the minutes in the timestamp string 
    ones_minutes = timestamp_split[1][1] 

    if int(ones_minutes) // 5 == 1: #is in the 5:00.000 to 9:59.999 bucket
        return timestamp_split[0] + ":" + timestamp_split[1][0] + "5" + ":" + "00.000Z" + " to " + timestamp_split[0] + ":" + timestamp_split[1][0] + "9" + ":" + "59.999Z"
    else: #is in the 0:00.000 to 4:59.999 bucket
        return timestamp_split[0] + ":" + timestamp_split[1][0] + "0" + ":" + "00.000Z" + " to " + timestamp_split[0] + ":" + timestamp_split[1][0] + "4" + ":" + "59.999Z"

'''
given a dictionary, interval_dict, a string, interval, and a string, label,
return a list of values paired with that specific label in the tuple values of the dictionary
during a specified 5 min interval
'''
def extract_label_values (interval_dict, interval, label):
    return [float(i[1]) for i in interval_dict[interval] if i[0] == label]

'''
given a list of numbers,
calculates the mean
'''
def calculate_mean(num_list):
    return sum(num_list) / len(num_list)

'''
given a list of numbers and the mean of the list,
calculates the (population) standard deviation
'''
def calculate_std(num_list, mean):
    num_list_std = [(i - mean) ** 2 for i in num_list]
    return (sum(num_list_std) / len(num_list_std)) ** 0.5

if __name__ == '__main__':
    calculate_data_stats('timeseries.csv')