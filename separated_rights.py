# 4 юзера, 6 объектов
# чтение, запись, передача прав

from enum import Enum
import random

USERS = [('Boris', '1234'), ('Victor', '1234'), ('Konstantin', '1234'), ('Evgeny', '1234')]
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
            rightsStr = "{:^20}".format(USERS[userIndex][0])
            for right in user_rights:
                rightsStr += "{:^20}".format(right.name)
            
            rightsStr += '\n'
            res += rightsStr
            userIndex +=1 

        return res

    def try_login(self, userIndex, password):
        if userIndex >= len(USERS):
            return None

        (username, true_password) = USERS[userIndex]

        if (true_password == password):
            return username

        return None

def handle_user_action(userIndex):
    print('Введите действие, которое необходимо выполнить:')
    print('1 - чтение')
    print('2 - запись')
    print('3 - передача прав')
    user_action = int(input(userIndex))

    if (user_action > 3 or user_action < 0):
        print('Неверное действие')
        return
    

access_rights = AccessRights()

exit = False

while (not exit):
    print(str(access_rights))
    print('Введите индекс пользователя, за которого необходимо войти')
    userIndex = int(input())
    print('Введите пароль')
    password = input()
    print()
    username = access_rights.try_login(userIndex, password)
    
    if (username):
        handle_user_action(userIndex)
    else:
        print('Неверный индекс пользователя/пароль')