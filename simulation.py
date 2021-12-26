from population import Population
from person import Person
import pandas as pd

class Simulation:

    def __init__ (self):
        self.population = Population()
        self.day = 1
        self.infectedPatientCount = 0
        self.recoveredPatientCount = 0
        self.fatalitiesCount = 0
        self.hospitalizedPatientCount = 0
        self.dailyInfected = []
        self.totalHospitalizedPatientCount = []
        self.totalFatalities = []
        self.numberOfRecoveredPeople = []

    def run(self,days):
        for self.day in range(days+1):
            for person in self.population.people:
                person.updateState(self.day)
                if person.infectedDay = 




    def saveData(self):
        data = pd.DataFrame([[i for i in range (1,self.day+1)],self.dailyInfected,self.totalFatalities,self.totalHospitalizedPatientCount,self.numberOfRecoveredPeople],columns=['Day','DailyInfectedPatients','TotalFatalities','TotalHospitalized','RecoveredPeople'])
        data.to_csv('data.csv')

    
    