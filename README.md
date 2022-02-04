# Covid Simulation

A simulation programme made using Python with OOP design to analyze the spread of the COVID-19 virus in a conceptual community with a population of one million.

Following features can be observed in the population: There are about one hundred thousand families in the community and a family can have two to seven members. More than 30% of the population are senior citizens who is older than 65 years. Twenty percent of the population is children, who are below 18 years. It is assumed that forty thousand people involve in essential services of the country.

The chance of getting infected with the virus is 10-20%, 15 - 40%, and 35 - 60% for children, adults, and senior citizen, respectively. However, wearing face masks reduce the risk of getting infected to 5 - 10% in all the population. In the meantime, it is assume that the family members have a 40 to 80% chance of getting infected if one family member get infected.

The symptoms of the infection are visible after 5th day onwards. The virus will not spread from an infected patient from the 11th day of infection. When a patient is detected with COVID-19, that patient is hospitalized for 10 days. It is assume the fatality rate of the infection is 0.1%. There is no effect from the gender on the virus. One who get infected build the immunity for 6 to 7 months.


# Functionalities

Simulates the spread of the virus among the community daily if a one person is infected with COVID-19 in the day 1. In the simulation, user has capability to enforce ‘wear face mask’ at any point of the simulation and enforce travel restrictions at any point, as well as lift the enforcement. 

Indicates the daily number of infected patients, total hospitalized patient count, total fatalities, number of recovered people up to 50 days (by default can simulate for any number of days).

# Other assumptions

When travel restrictions are on people  15-25% less chance of infection except for people in essential services.

Depending on the number of infected patients in the population the probability of infecting increases.

Every family has at least one adult or a senior citizen.

After idenifying a person as a Covid patient he or she has 50% chance of admitting to a hospital any given day.

If person is not dead within 15 days after infecting he or she is recovered.

