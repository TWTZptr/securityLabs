from distutils.log import error
import math

def encrypt(data, key1, key2):
  size = len(key1)
  movedColumns = []

  for i in range(size):
    movedColumns.append([])

    for _ in range(size):
      movedColumns[i].append('')

  # Двигаем столбцы
  for fromColumn in range(size):
    toColumn = int(key1[fromColumn]) - 1
    
    for row in range(size):
      movedColumns[row][toColumn] = data[row][fromColumn]

  printMatrix(movedColumns)
  movedColumnsAndRows = []

  for i in range(size):
    movedColumnsAndRows.append([])

  # Двигаем строки
  for i in range(size):
    toRow = int(key2[i]) - 1
    movedColumnsAndRows[toRow] = movedColumns[i]

  return movedColumnsAndRows

def decrypt(data, key1, key2):
  size = len(key1)
  movedColumns = []

  for i in range(size):
    movedColumns.append([])

    for _ in range(size):
      movedColumns[i].append('')

  # Двигаем столбцы
  for toColumn in range(size):
    fromColumn = int(key1[toColumn]) - 1
    
    for row in range(size):
      movedColumns[row][toColumn] = data[row][fromColumn]

  movedColumnsAndRows = []

  # Двигаем строки
  for i in range(size):
    movedColumnsAndRows.append([])

  for i in range(size):
    fromRow = int(key2[i]) - 1
    movedColumnsAndRows[i] = movedColumns[fromRow]

  return movedColumnsAndRows

# Преобразование данных из матрицы в строку
def makeDataFromMatrix(data):
  size = len(data)
  result = ''
  for i in range(size):
    for j in range(size):
      result+= data[i][j]

  return result

def splitData(data, size):
  result = []
  for i in range(size):
    result.append([])
    for j in range(size):
      result[i].append(data[i * size + j])
  return result

def printMatrix(matrix):
  size = len(matrix)
  for i in range(size):
    toPrint = ''
    for j in range(size):
      toPrint += str(matrix[i][j]) + ' '
    print(toPrint)
  print()


dataToEncrypt = 'шифрование_перестановкой_'

key1 = list('32541')
key2 = list('43512')

size = math.sqrt(len(dataToEncrypt))

if len(key1) != len(key2):
  raise error('key1 and key2 length is not equals')

keylen = len(key1)

if keylen < size:
  raise error('bad key length')

if keylen > size:
  raise error('data to encrypt is too small for provided key')

size = int(size)

matrixData = splitData(dataToEncrypt, size)
printMatrix(matrixData)
encryptedMatrixData = encrypt(matrixData, key1, key2)
encryptedData = makeDataFromMatrix(encryptedMatrixData)
decryptedData = decrypt(encryptedMatrixData, key1, key2)
printMatrix(encryptedMatrixData)
print(encryptedData)
print()
printMatrix(decryptedData)