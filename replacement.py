key = 'chair'
data = 'datatosecure'

def encrypt(data, key):
  keylen = len(key)
  result = ''

  for i in range(len(data)):
    dataChar = data[i]
    keyChar = key[i % keylen]

    dataCharCode = ord(dataChar) - ord('a')
    keyCharCode = ord(keyChar) - ord('a')

    encodedChar = chr((dataCharCode + keyCharCode) % 26 + ord('a'))
    result += encodedChar
  
  return result;

def decrypt(data, key):
  keylen = len(key)
  result = ''

  for i in range(len(data)):
    dataChar = data[i]
    keyChar = key[i % keylen]

    dataCharCode = ord(dataChar) - ord('a')
    keyCharCode = ord(keyChar) - ord('a')
    
    encodedCharCode = dataCharCode - keyCharCode
    if encodedCharCode < 0:
      encodedCharCode += 26
    
    encodedChar = chr(encodedCharCode + ord('a'))

    result += encodedChar
  
  return result;

print('data to encrypt: ', data)
encryptedData = encrypt(data, key)
print('encrypted data: ', encryptedData)
decryptedData = decrypt(encryptedData, key)
print('decrypted data: ', decryptedData)