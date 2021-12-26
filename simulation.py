import random

from population import Population
from person import Person
import pandas as pd

class Simulation:

    def __init__(self):
        self.population = Population()
        self.day = 0
        self.infectedPatientCount = 0
        self.recoveredPatientCount = 0
        self.fatalitiesCount = 0
        self.hospitalizedPatientCount = 0
        self.dailyInfected = []
        self.totalHospitalizedPatient = []
        self.totalFatalities = []
        self.recoveredPeopleCount = []
        self.isWearAMask = False
        self.isTravelRestrictions = False
        self.wearAMaskStartdate = 0
        self.wearAMaskEndtdate = 0
        self.travelReStart = 0
        self.travelReEnd = 0


    def input(self):
        x = input("Press 1 if you wants to apply wear mask law in a time period: ")
        y = input("Press 1 if you wants to apply travel restrictions in a time period: ")
        if x=='1':
            self.wearAMaskStartdate = input("Enter the start date of wearing mask law that you need to apply: ")
            self.wearAMaskEndtdate = input("Enter the end date of wearing mask law that you need to apply:")

        else:
            pass

        if y=='1':
            self.travelReStart = input("Enter the start date of travel restrictions that you need to apply:")
            self.travelReEnd = input("Enter the end date of travel restrictions that you need to apply:")
        else:
            pass

    def run(self, days):
        random_person = random.randint(0, 99999)
        self.population.people[random_person].isInfected = True
        self.population.people[random_person].infectedDay = 0
        self.infectedPatientCount = 1

        for self.day in range(days):
            daily_infected_patient_count = 0
            if self.day == 0:
                daily_infected_patient_count = 1
            
            if self.wearAMaskStartdate <= self.day <= self.wearAMaskEndtdate :
                self.isWearAMask = True
            else: self.isWearAMask = False
            
            if self.travelReStart <= self.day <= self.travelReEnd :
                self.isTravelRestrictions = True
            else: self.isTravelRestrictions = False

            for person in self.population.people:
                family_status = False
                if person.isInAFamily:
                    for member in self.population.families[person.familyId].members:
                        if self.population.people[member].isInfected is True and self.population.people[member].isHospitalized is False and self.day - self.population.people[member].infectedDay <= 11:
                            family_status = True
                is_hospitalized = person.isHospitalized
                person.calculate_infection_probability(self.day, self.isWearAMask, self.isTravelRestrictions,
                                                       self.infectedPatientCount,family_status)
                person.update_state(self.day)
                if person.infectedDay == self.day and person.isInfected is True:
                    self.infectedPatientCount += 1
                    daily_infected_patient_count += 1
                if self.day == person.hospitalizedDay:
                    self.hospitalizedPatientCount += 1
                if person.fatalDay == self.day:
                    self.fatalitiesCount += 1
                if person.isFatal is False and person.isRecovered is True and person.recoveredDay == self.day:
                    self.recoveredPatientCount += 1
                    self.infectedPatientCount -= 1
                    if is_hospitalized is True:
                        self.hospitalizedPatientCount -= 1

            self.dailyInfected.append(daily_infected_patient_count)
            self.totalHospitalizedPatient.append(self.hospitalizedPatientCount)
            self.totalFatalities.append(self.fatalitiesCount)
            self.recoveredPeopleCount.append(self.recoveredPatientCount)

            #print(f'\nDay = {self.day}')
            #print(f'Daily infected Count  = {daily_infected_patient_count}')
            #print(f'Total hospitalized patient count  = {self.hospitalizedPatientCount}')
            #print(f'Total fatalities count = {self.fatalitiesCount}')
            #print(f'Total recovered patient count = {self.recoveredPatientCount}')


    def save_data(self):
        days = [i for i in range(0, self.day + 1)]
        dt = {'Day':days, 'DailyInfectedPatients': self.dailyInfected, 'TotalFatalities': self.totalFatalities,
              'TotalHospitalized':
                  self.totalHospitalizedPatient, 'RecoveredPeople': self.recoveredPeopleCount}
        data = pd.DataFrame(data=dt)
        #data.to_csv('data.csv')
        return data
