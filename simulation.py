from population import Population
from person import Person
import pandas as pd


class Simulation:

    def __init__(self):
        self.population = Population()
        self.day = 1
        self.infectedPatientCount = 0
        self.recoveredPatientCount = 0
        self.fatalitiesCount = 0
        self.hospitalizedPatientCount = 0
        self.dailyInfected = []
        self.totalHospitalizedPatient = []
        self.totalFatalities = []
        self.recoveredPeopleCount = []

    def run(self, days):
        for self.day in range(days + 1):
            daily_infected_patient_count = 0
            for person in self.population.people:
                person.update_state(self.day)
                if person.infectedDay == self.day:
                    self.infectedPatientCount += 1
                    daily_infected_patient_count += 1
                if self.day - person.infectedDay == 5:
                    self.hospitalizedPatientCount += 1
                if person.fatalDay == self.day:
                    self.fatalitiesCount += 1
                if person.isFatal is False and person.isRecovered is True and self.day - person.infectedDay == 15:
                    self.recoveredPatientCount += 1
            self.dailyInfected.append(daily_infected_patient_count)
            self.totalHospitalizedPatient.append(self.hospitalizedPatientCount)
            self.totalFatalities.append(self.fatalitiesCount)
            self.recoveredPeopleCount.append(self.recoveredPatientCount)

    def save_data(self):
        data = pd.DataFrame([[i for i in range(1, self.day + 1)], self.dailyInfected, self.totalFatalities,
                             self.totalHospitalizedPatient, self.recoveredPeopleCount],
                            columns=['Day', 'DailyInfectedPatients', 'TotalFatalities', 'TotalHospitalized',
                                     'RecoveredPeople'])
        data.to_csv('data.csv')
