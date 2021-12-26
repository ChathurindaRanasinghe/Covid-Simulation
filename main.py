from simulation import Simulation
import pandas as pd
import streamlit as st
import pandas as pd


sim = Simulation()
sim.run(70)
data = sim.save_data()
#print(data)

#data = pd.read_csv('data.csv')

st.title("Simulating COVID-19 spread in a conceptual community")

st.write('Data')
data 

dataframe1 = pd.DataFrame(data.DailyInfectedPatients,
   )
#dataframe
st.write('Daily Infected Patients count daily')
st.line_chart(dataframe1)

dataframe2 = pd.DataFrame(data.TotalFatalities,
   )
#dataframe
st.write('Total Fatalities count daily')
st.line_chart(dataframe2)

dataframe3 = pd.DataFrame(data.TotalHospitalized,
   )
#dataframe
st.write('Total Hospitalized count daily')
st.line_chart(dataframe3)

dataframe4 = pd.DataFrame(data.RecoveredPeople,
   )
#dataframe
st.write('Recovered People count daily')
st.line_chart(dataframe4)

