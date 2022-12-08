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

    def can_user_perform_action(self, user_index, action_index, object_index):
        required_access_type = self.map_action_index_to_access_type(action_index)

        if (self.access_matrix[user_index][object_index] in [required_access_type, AccessTypes.FULL]):
            return True
        else:
            return False

    @staticmethod
    def map_action_index_to_access_type(action_index):
        if (action_index == 1): return AccessTypes.READ
        if (action_index == 2): return AccessTypes.WRITE
        if (action_index == 3): return AccessTypes.TRANSFER

    def transfer_rights(self, to, access_type_index, object_index):
        right = self.map_action_index_to_access_type(access_type_index)
        self.access_matrix[to][object_index] = right

def handle_user_action():
    print('Введите действие, которое необходимо выполнить:')
    print('1 - чтение')
    print('2 - запись')
    print('3 - передача прав')
    user_action_index = int(input())

    if (not user_action_index in range(1,4)):
        raise Exception('Неверное действие')
    
    print()
    print('Введите индекс объекта, над которым выполняется действие')
    
    object_index = int(input())

    if (not object_index in range(0, len(OBJECTS) + 1)):
        raise Exception('Файла с таким нидексом не существует')
    
    return (user_action_index, object_index)

access_rights = AccessRights()

exit = False

while (not exit):
    print(str(access_rights))
    print('Введите индекс пользователя, за которого необходимо войти')
    user_index = int(input())
    print('Введите пароль')
    password = input()
    print()
    username = access_rights.try_login(user_index, password)
    
    if (username):
        print('Вы вошли как ' + username)
        (user_action_index, object_index) = handle_user_action()
        successful = access_rights.can_user_perform_action(user_index, user_action_index, object_index)

        if (successful):
            print('Доступ разрешен')

            if (AccessRights.map_action_index_to_access_type(user_action_index) == AccessTypes.TRANSFER):
                print('Какие права выдать пользователю?')
                rights_index = int(input())
                print('Введите индекс пользователя, которому необходимо выдать права')
                to_user_index = int(input())

                if (rights_index in range(1,4) and to_user_index in range(0, len(USERS) + 1)):
                    access_rights.transfer_rights(to_user_index, rights_index, object_index)
                    print('Операция успешно завершена')
                else: 
                    raise Exception('Неверный индекс прав или пользователя')

        else:
            print('Доступ запрещен')

    else:
        print('Неверный индекс пользователя/пароль')
        
    print('\n\n')
