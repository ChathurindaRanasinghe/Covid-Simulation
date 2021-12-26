from person import Person
from family import Family
import random

class Population:
    def __init__(self):
        self.people = []
        self.families = []
        self.adults = []
        self.children = []
        self.adultCount = 0
        self.manCount = 0
        self.childCount = 0
        self.essentialServiceCount = 4000

        for i in range(100000):
            newPerson = Person()
            newPersonAge = getattr(newPerson,'age')
            newPersonId = getattr(newPerson,'id')
            if newPersonAge >= 65:
                self.adultCount += 1
                self.adults.append(newPersonId)
            elif newPersonAge <= 18:
                self.childCount += 1
                self.children.append(newPersonId)
            else:
                essentialProb = random.randint(1,100)
                if 1 <= essentialProb <= 9 and self.essentialServiceCount != 0:
                    setattr(newPerson,'isEssentialService',True)
                    self.essentialServiceCount -= 1
                self.manCount += 1
                self.adults.append(newPersonId)
            self.people.append(newPerson)
        
        self.createFamilies()
    
    def createFamilies(self):
        random.shuffle(self.adults)
        random.shuffle(self.children)
        childrenInFamiliesCount = 0
        # availablePeople = [i for i in range(1000000)]
        for i in range (10000):
            # print(f"No of People {len(self._people)}")
            newFamily = Family()
            noMembers = newFamily.memberCount
            newFamilyId = newFamily.id

            adultId = self.adults.pop()
            self.people[adultId].addToAFamily(newFamilyId)

            noMembers -= 1

            for j in range (noMembers):
                randomNo = random.randint(0,99)
                if randomNo <= 50 and len(self.children) != 0:
                    childId = self.children.pop()
                    self.people[childId].addToAFamily(newFamilyId)
                    childrenInFamiliesCount += 1
                else:
                    adultId = self.adults.pop()
                    self.people[adultId].addToAFamily(newFamilyId)

            # for j in range (noMembers):
            #     rndomIndex = random.randint(0,len(availablePeople)-1)
            #     familyMemberId = availablePeople.pop(rndomIndex)
            #     # print(f"familyMemberId {familyMemberId}")
            #     self._people[familyMemberId].addToAFamily(i)
            #     newFamily.addAMember(familyMemberId)
            self.families.append(newFamily)
        print(f"children in families = {childrenInFamiliesCount}")


