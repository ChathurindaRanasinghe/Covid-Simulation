import random


class Family:
    newid = 0

    def __init__(self):
        self.memberCount = random.randint(2,7)
        self.members = []

        self.id = Family.newid
        Family.newid += 1



        # self._infectedMemberCount
    
    def addAMember(self, member):
        self.members.append(member)

