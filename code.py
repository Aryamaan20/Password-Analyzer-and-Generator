# Implementing Algorithm to generate passwords
import random
words = input("Enter five words(give space between each word): ").split()
# Error if any answer < 3 characters
for i in range(len(words)):
    if len(words[i]) < 3:
        raise Exception("Please enter answer more than 3 characters")

numbers = input("Enter two numbers(give space between each number): ").split()
# Error if numbers are single digit
for i in range(len(numbers)):
    if len(numbers[i]) < 2:
        raise Exception("Please enter answer more than 1 digit")


# Error if any repetitive answers
for i in range(len(words)-1):
    if words[i].lower() == words[i+1].lower():
        raise Exception("Please do not repeat answers")


for i in range(len(numbers)-1):
    if numbers[i] == numbers[i+1]:
        raise Exception("Please do not repeat answers")

num_passwords = int(input("Enter number of passwords required:"))
special_chars = ['@', '$', '!', '#', '%',
                 '&', '(', ')', '0', '3', '8', '<', '|']
punc = ['@', '*', '+', '-', ':', '”', '/', '\\', '~', '?', '[', ']',
        '{', '}', '$', '!', '#', '%', '&', '(', ')', '_', '<', '|']
alphabets = ['a', 's', 'i', 'r', 'x', 'q', 'c', 'j', 'o', 'e', 'b', 'k', 'l']
numbername = ["zero", "one", "two", "three",
              "four", "five", "six", "seven", "eight", "nine"]
number2 = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
c2s = {}
n2s = {}


for i in range(13):
    c2s[alphabets[i]] = special_chars[i]

for i in range(10):
    n2s[number2[i]] = numbername[i]


def randomly_capitalize(s):
    result = ''
    for char in s:
        flag = random.randint(0, 1)
        if flag == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result


def merge_randomly(str1, str2):
    result = ''
    flag = random.randint(0, 1)
    if flag == 0:
        result = str1 + str2
    else:
        result = str2 + str1
    return result, flag


def charToSpecial(s):
    for i in range(len(s)): 
        char = s[i]
        if char in c2s:
            s = s.replace(char, c2s[char])
            flag[i] = 1

    return s


#def numToSpecial(s):
#    print(s)
#    for i in range(len(s)):
#        num = s[i]
#        if flag[i] == 0:
#            if num in n2s:
#
#                s = s.replace(num, n2s[num])
#                print(s)
#            break
#
#    return s


def insert_number(s, n, f, str1, str2):
    flag = random.randint(0, 2)
    if flag == 0:
        return n+s
    elif flag == 2:
        return s+n
    else:
        if f == 0:
            return s[:len(str1)]+n+s[len(str1):]
        else:
            return s[:len(str2)]+n+s[len(str2):]


def add_punctuation(s):
    return s+random.choice(punc)


passwords_generated = []
while num_passwords > 0:
    temp = list(words)
    string1 = random.choice(temp)
    temp.remove(string1)
    string2 = random.choice(temp)
    number = random.choice(numbers)
    string1, string2 = randomly_capitalize(
        string1), randomly_capitalize(string2)
    final_string, f = merge_randomly(string1, string2)   
    final_string = insert_number(final_string, number, f, string1, string2)
    flag = [0] * len(final_string)
    final_string = charToSpecial(final_string)
    #final_string = numToSpecial(final_string)
    final_string = add_punctuation(final_string)

    C = len(final_string)
    if C < 8:
        for i in range(8 - C):
            final_string += random.choice(special_chars)

    passwords_generated.append(final_string)

    print("Final Password:", final_string)
    num_passwords -= 1
    

import re
patterns = ['shadow', 'a199', 'dima199', '91', '1991', 'pun', 'EY', '1234', '123', 'eirf', 'nhei', 'dj', 'jhj', 'jy', 'way', 'amst', 'te', 'erda', 'sterda', 'al', 'ala', 'jordan', 'cho',
            'ol', 'evild', 'evi', 'evil', 'dead', 'ad', 'ea', 'vil', 'ld', '000', 'blue', 'aaa', 'a2', 'str', 'moni', 'er', 'ojo11', 'mo', 'mojo', '11', 'zxc', 'zxcv', 'love', 'br', 'bryan',
            'an', 'azz', 'ova', 'lan', 'rate', 'espera', 'esper', 'ca', 'on', 'su', 'ge', 'rna', 'rn', 'fur', 'ur', 'ace', 'butt', 'bur', 'ina', 'jack', 'auto', 'ill', 'tor', 'ector',
            'ecto', 'or', 'ect', 've', 'cto', 'ctor', 'and', 'fre', '12', 'hot', 'ot', 'cial', 'pecial', 'pe', 'pi', '19', 'oleg1', 'shir', 'sh', 'man', 'da', 'dais', 'ab', 'ba', 'angel',
            'arky', 'ra', 'ar', 'ake', 'ma', '12345678', 'cooter', 'co', 'scooter', '6chevy', 'killer', 'qwerty', 'ggy', 'master', 'ers', 'head', 'david', 'ing', 'ga', 'lon', 'ck',
            'dick', 'long', 'ng', 'count', 'ou', 'oun', 'ted', 'ire', 'oo', 'fire', 'artin', 'martin', 'in1', 'ker1', 'acker', '23', 'poppy', 'pp', 'ppy123', 'be', 'zer', 'ee', 'thunder', 'dan',
            'ana', 'ho', 'ota', 'tac', 'vol', 'el', 'elvis', 's99', 'elvi', 'ri', 'alex', 'se', 'hi', 'pimp', 'ER', 'lo', 'sasha1', 'ch', 'rest', 'john', 'sta', 'out', 'st', 'ne', 'elcome', 'we',
            'welcome', 'wel', 'nat', 'mar', 'ball', 'tymrf', 'ger', 'ki', 'king', 'es', 'ro', 'happy', 'ell', 'flash', 'qwe', 'all', '12345', 'th', 'sa', 'daniel', 'ani', 'shar', 'jerr',
            'ken', 'one', 'fi', 'fir', 'firstone', '624', 'ac', 'mic', 'art', 'sha', 'superm', 'dd', 'ista', 'rist', '2000', 'at', 'scott', 'in', 'indi', 'bz', 'hfc', '987654321', '54321',
            'ton', 'fgf', 'gf', 'fg', 'kocha', 'oc', 'land', 'home', 's1', 'good', 'iper', 'pers', 'ipers', 'per', 'vi', 'viper', 'ett', 'et', 'ob', 'bb', 'obby', 'y1', 'bby1', 'rob',
            'robb', 'robby', 'nokia', 'batman', 'aezakmi', 'a123', 'izard', 'fuck', 'min', 'esca', 'get', 'gettysbu', 'nder', 'ion', 'mi', 'ud', 'rude', 'rud', 'ru', 'boy', 'mari', 'emon',
            'big', 'rf', 'ens', 'green', 'gre', 'ford', 'ord', 'kam', 'bla', 'blast', 'bl', 'ster', 'laster', 'las', '111', 'ham', 'ture', 'lar', 'ola', 'solar', 'sol', 'so', 'tn', 'ghbdtn',
            'ghb', 'bd', 'dtn', 'nbr', 'nb', 'ey', 'rand', 'mme', 'mmer', 'tim', 'ti', 'im', 'mer', 'immer', 'sun', 'llin', 'ossi', 'lu', 'zxcvb', 'jxrf', 'ama', 'mada', 'ada', 'sex', 'ver',
            'ter', 'hel', 'dragon', 'a19', '95', '199', '1995', 'vova199', 'vova', 'purple', 'cat', 'fucks', 'tan', 'black', 'RE', 'che', 'access', 'dolphin', 'hin',
            'ret', 'barr', 'je', 'mou', 'oune', 'll', 're', 'ant', 'bu', 'bal', 'ian', 'anthon', 'on1', 'nt', 'nth', 'anth', '1Cccccc', 'Ccccc', 'atthew',
            'matt', 'ja', 'am', 'sam', 'ock', 'sea', 'oliver', 'oliv', 'er2', 'itsu', 'piderman', 'ide', 'dee', 'smith', 'nch', 'no00', 'benno', 'cks', 'ero', 'us',
            'ven', 'a2010', '55555', 'secret', 'swe', 'td', 'eanin', 'soccer', 'un', 'junior', 'age', 'verag', 'tig', 'mother', 'smo', 'the', 'her', 'moth',
            'fgh', 'nin', 'harley', 'ent', 'red', 'ward', 'er1', 'sana', 'os', 'hea', 'he', 'ik', 'kik', 'kok', 'con', 'puss', 'rocket', 'rock', 'cola', 'col',
            '00', 'dle', 'mod', 'ov', 'casa', 'asanov', 'anov', 'anova', 'eni', 'is', 'is1', 'ight', 'averic', 'eric', 'ric', 'maveric', 'CO', 'OC', 'win',
            'ed', 'gan', 'allard', 'eg', 'ta', 'ine', 'bel', 'lous', 'horny', 'hor', 'yme', 'me', 'nascar', 'andalf', 'gandalf', 'dal', 'li', 'april2', '147',
            'ile', 'le', 'fu', 'ku', 'ya', 'yak', 'ip', 'ul', 'andy', 'ena', 'girl', 'lexandr', 'music', 'pas', 'bob', 'lovejo', 'mike', 'password', 'passw',
            'ey2010', 'ashi', 'itch', 'my', 'schnu', 'nuff', 'la', 'thug', 'four', 'ble', 'ghjg', 'ghjghj', 'ghj', 'stuff', 'ove', 'qaz', 'mmy', 'birthday',
            'pol', 'ook', 'eagle', '2wsx', 'par', 'wayne', 'apple', 'DICK', 'IC', 'hris', 'anger', 'tcast', 'tca', 'tcas', 'ban', 'ustin', 'nchester',
            'field', 'olf', 'silver', 'xxx', 'dra', 'rat', 'bull', 'amir', 'mon', 'rus', 'ito', 'gri', 'negri', 'negrit', 'negr', 'hilli', 'chill', 'chillin',
            'hello', 'night', 'ic']
# Function to categorize password

import mysql.connector
def password(v):
    

    # connect to the MySQL database
    connector= mysql.connector.connect(user='sanga123', 
    password='breached6789!!', host='breachedpasswords.mysql.database.azure.com',
    port=3306, database='breachedpasswords')

    passwordinput = v

    # define the query
    query = "SELECT * FROM passwords WHERE Password = %s"

    # execute the query with the user entered password as a parameter
    cursor = connector.cursor()
    cursor.execute(query, (passwordinput,))

    # check if any passwords were returned
    result = cursor.fetchone()
    if result:
        raise Exception("Password entered is a breached password")
    else:
        print("Password entered is not a breached password")
    connector.close()  
    # the password should not be a
    # newline or space
    if v == "\n" or v == " ":
        return "Password cannot be a newline or space!"
    # password cannot contain a space
    for i in range(len(v)):
        if v[i] == " ":
            return "Password cannot contain a space"
    # the password length should be in
    # between 9 and 20
    if 9 <= len(v) <= 20:
        # checks for patterns in password
        for pattern in patterns:
            if pattern in v:
                return "Weak Password: Weak patterns have been recognized in the password"
        # checks for occurrence of a character
        # three or more times in a row
        if re.search(r'(.)\1\1', v):
            return "Weak Password: Same character repeats three or more times in a row"
        # checks for occurrence of same string
        # pattern( minimum of two character length)
        # repeating
        if re.search(r'(..)(.*?)\1', v):
            return "Weak password: Same string pattern repetition"
        else:
            return "Strong Password!"
    else:
        return "Password length must be 9-20 characters!"
      


# Analyzing strength of generated passwords:
for p in passwords_generated:
    print(password(p))
    
#Analyzing strength of password given by user:
#print(password('Hello'))