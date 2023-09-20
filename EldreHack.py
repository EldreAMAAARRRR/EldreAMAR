mport hashlib

md5_hash_to_crack = '1089ba10a11a71d52c24468d14b931f3'

worldlist = open('norwegian.txt').readlines() #read file into memory


for word in worldlist: #loop through each word
    word = word.strip()     #stripping away whitespace etc

    result = hashlib.md5(word.encode()).hexdigest() #compute actual hash

    if result == md5_hash_to_crack: #check if result matches
        print('found password: ' + word) #match success

print('Searched through ' + str(len(worldlist)) + ' words') #tell user we finished
