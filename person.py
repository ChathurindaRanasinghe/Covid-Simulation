import random


class Person:
    new_id = 0

    def __init__(self):

        # self._age =

        age_prob = random.randint(1, 100)
        if 1 <= age_prob <= 31:
            self.age = random.randint(65, 90)
        elif 31 < age_prob <= 51:
            self.age = random.randint(1, 18)
        else:
            self.age = random.randint(19, 64)

        self.id = Person.new_id
        Person.new_id += 1

        # self._gender = "Male" if random.randint(0, 1) == 1 else "Female"

        self.isInAFamily = False
        self.familyId = -1
        self.infectionProbability = 0
        self.isEssentialService = False
        self.isInfected = False
        self.isFatal = False
        self.fatalDay = -1
        self.infectedDay = -1
        self.isHospitalized = False
        self.isRecovered = False

    def add_to_a_family(self, family_id):
        self.isInAFamily = True
        self.familyId = family_id

    def calculate_infection_probability(self, day, wear_mask, travel_restrictions):
        probability = 0
        if self.isRecovered is False and self.isHospitalized is False and self.isFatal is False \
                and self.isInfected is False:
            isTravelRestrict = False
            wearingMaskChance = (random.randint(5, 10)) / 100
            if self.age <= 18:
                if isTravelRestrict is True:
                    finalChildChance = 20/100
                else:
                    childChance = (random.randint(10, 20))/100
                    finalChildChance = childChance * wearingMaskChance
            elif self.age < 65:
                if isTravelRestrict is True:
                    finalAdultChance = 20/100
                else:
                    adultChance = (random.randint(15, 40)) / 100
                    finalAdultChance = adultChance * wearingMaskChance
            else:
                if isTravelRestrict is True:
                    finalSeniorChance = 20/100
                else:
                    seniorChance = (random.randint(35, 60)) / 100
                    finalSeniorChance = seniorChance * wearingMaskChance

        self.infectionProbability = probability

    def update_state(self, day):
        if self.isInfected and self.isRecovered is False and self.isFatal is False:
            days_after_infection = day - self.infectedDay
            if days_after_infection == 5:
                self.isHospitalized = True
            elif days_after_infection == 15:
                self.isHospitalized = False
                self.isRecovered = True
                self.infectedDay = -1