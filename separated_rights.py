# 4 юзера, 6 объектов
# чтение, запись, передача прав

from enum import Enum
import random

USERS = ['Boris', 'Victor', 'Konstantin', 'Evgeny']
OBJECTS = ['FILE 1', 'DATABASE', 'FILE 2', 'CLOUD DATABASE', 'CLOUD SERVER INSTANCE', 'CD-RW']
AccessTypes = Enum('AccessTypes', ['READ', 'WRITE', 'TRANSFER', 'FULL'])

class AccessRights:
    def __init__(self):
        self.access_matrix = []

        for _ in USERS:
            rights = []
            for _ in OBJECTS:
                rights.append(random.choice(list(AccessTypes)))
            self.access_matrix.append(rights)
        
        # create an admin
        adminIndex = random.randrange(0, len(USERS))
        self.access_matrix[adminIndex] = [AccessTypes.FULL] * len(OBJECTS)

    def __str__(self) -> str:
        res = "{:^20}".format('')

        for object in OBJECTS:
            res += "{:^20}".format(object)
        
        res += '\n'
        userIndex = 0

        for user_rights in self.access_matrix:
            rightsStr = "{:^20}".format(USERS[userIndex])
            for right in user_rights:
                rightsStr += "{:^20}".format(right.name)
            
            rightsStr += '\n'
            res += rightsStr
            userIndex +=1 

        return res


a = AccessRights()
print(a)