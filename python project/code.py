import csv #importing csv module to perform some operations
from collections import Counter
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
violation = []
location = []
action = []
location1 = []
violation1 = []
with open("traffic.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[3] == "DENTON              ":
            violation.append(row[9]) #appending all the violations to a list
            location.append(row[5])
            action.append(row[7])
c = Counter(violation)
violation_terms = c.keys() #appending the elemnts to a list
violation_counts = c.values() #appending the elements count to a list
print("The number and type of traffic violations most common in Denton:", c.most_common, '\n')
c1 = Counter(location)
zip_numbers = c1.keys()
zip_counts = c1.values()
print("The geographic locations where more violations take place:", c1.most_common, '\n')
c2 = Counter(action)
action_terms = c2.keys()
action_counts = c2.values()
print("The actions taken by the police department in response:", c2.most_common, '\n')
with open('collect.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',') #creating a new csv file
    for row in zip(violation, location, action):
        writer.writerow(row) #writing the values into rows
with open('collect.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] == "SPEEDING IN 30 MILE HOUR ZONE           ": #checking the condition
            location1.append(row[1])
            violation1.append(row[2])
c3 = Counter(location1) #finding the frequency count of elements
c4 = Counter(violation1)
print("The geographical locations where the violation SPEEDING IN 30 MILE HOUR ZONE take place:", c3.most_common, '\n')
print("The actions taken by police department in response to the violation SPEEDING IN 30 MILE HOUR ZONE:", c4.most_common, '\n')
indexes = np.arange(len(violation_terms))
width = 0.5
plt.bar(indexes, violation_counts, width)
plt.xticks(indexes + width * 0.5, violation_terms, rotation=90) #http://stackoverflow.com/questions/22303554/words-frequency-using-pandas-and-matplotlib
plt.gcf().subplots_adjust(bottom=0.56)
plt.title("Histogram plot for most common violations in Denton") #specifying the title name to the plot
plt.show()
plt.savefig("Histogram1.jpg") #saving the figure to an image file
plt.close() #closing the plot
indexes1 = np.arange(len(zip_numbers))
width1 = 0.5
plt.bar(indexes1, zip_counts, width1)
plt.xticks(indexes1 + width1 * 0.5, zip_numbers, rotation=90) 
plt.gcf().subplots_adjust(bottom=0.56)
plt.title("Histogram plot for geographical locations where more violations take place") 
plt.show()
plt.savefig("Histogram2.jpg")
plt.close()
indexes2 = np.arange(len(action_terms))
width2 = 0.5
plt.bar(indexes2, action_counts, width2)
plt.xticks(indexes2 + width2 * 0.5, action_terms, rotation=90) 
plt.gcf().subplots_adjust(bottom=0.56)
plt.title("Histogram plot for actions taken by police department in response") 
plt.show()
plt.savefig("Histogram3.jpg")
plt.close()
print("Histograms are generated and saved as .jpg files")