from simulation import Simulation
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

#data = pd.read_csv('data.csv')

# st.title("Simulating COVID-19 spread in a conceptual community")

# x = st.text_input("Press 1 if you wants to apply wear mask law in a time period: ")
# y = st.text_input("Press 1 if you wants to apply travel restrictions in a time period: ")

# if x=='1':
#    wearAMaskStartdate = st.text_input("Enter the start date of wearing mask law that you need to apply: ", 0)
#    wearAMaskEndtdate = st.text_input("Enter the end date of wearing mask law that you need to apply:", 0)
# else:
#    pass

# if y=='1':
#    travelReStart = st.text_input("Enter the start date of travel restrictions that you need to apply:", 0)
#    travelReEnd = st.text_input("Enter the end date of travel restrictions that you need to apply:", 0)
# else:
#    pass

print("Simulating COVID-19 spread in a conceptual community")
print()
sim = Simulation()
sim.run(100)
sim.input()
data = sim.save_data()
print()
print (data)
print()

x = data.Day
y = data.DailyInfectedPatients
plt.plot(x, y, color='red', linewidth = 0.5,
         marker='o', markerfacecolor='red', markersize=5)
plt.xlabel("Day")
plt.ylabel("Daily Infected Patients")
plt.title("Daily Infected Patients count daily")
plt.show()

x = data.Day
y = data.TotalFatalities
plt.plot(x, y, color='red', linewidth = 0.5,
         marker='o', markerfacecolor='red', markersize=5)
plt.xlabel("Day")
plt.ylabel("Total Fatalities")
plt.title("Total Fatalities count daily")
plt.show()

x = data.Day
y = data.TotalHospitalized
plt.plot(x, y, color='red', linewidth = 0.5,
         marker='o', markerfacecolor='red', markersize=5)
plt.xlabel("Day")
plt.ylabel("Total Hospitalized")
plt.title("Total Hospitalized count daily")
plt.show()

x = data.Day
y = data.RecoveredPeople
plt.plot(x, y, color='red', linewidth = 0.5,
         marker='o', markerfacecolor='red', markersize=5)
plt.xlabel("Day")
plt.ylabel("Recovered People")
plt.title("Recovered People count daily")
plt.show()
# def simulate():
#    st.write('Data')
#    data
#    dataframe1 = pd.DataFrame(data.DailyInfectedPatients,
#       )
#    #dataframe
#    st.write('Daily Infected Patients count daily')
#    st.line_chart(dataframe1)

#    dataframe2 = pd.DataFrame(data.TotalFatalities,
#       )
#    #dataframe
#    st.write('Total Fatalities count daily')
#    st.line_chart(dataframe2)

#    dataframe3 = pd.DataFrame(data.TotalHospitalized,
#       )
#    #dataframe
#    st.write('Total Hospitalized count daily')
#    st.line_chart(dataframe3)

#    dataframe4 = pd.DataFrame(data.RecoveredPeople,
#       )
#    #dataframe
#    st.write('Recovered People count daily')
#    st.line_chart(dataframe4)