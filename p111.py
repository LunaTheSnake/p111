import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("zsample.csv")
data = df["id"].tolist()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print(f' The mean value is {mean}')
print(f' The standerd deviation is {std_deviation}')

def random_mean(counter):
    dataset = []
    for i in range(0,counter):
        randomindex = random.randint(0,len(data)-1)
        value = data[randomindex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0, 1000):
    set_of_means = random_mean(100)
    mean_list.append(set_of_means)


std_deviation = statistics.stdev(mean_list)
mean=statistics.mean(mean_list)
fig = ff.create_distplot([mean_list],["id"], show_hist= False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.2], mode="lines", name="Mean"))
fig.show()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print(f' The mean value is {mean}')
print(f' The standerd deviation is {std_deviation}')

mean = statistics.mean(mean_list)
std_deviation = statistics.stdev(mean_list)

print(f' The mean value is {mean}')
print(f' The standerd deviation is {std_deviation}')