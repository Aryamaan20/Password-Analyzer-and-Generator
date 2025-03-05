# Password Analyzer & Generator

## Overview
This project provides a **secure password generator** and a **password strength analyzer**. The generator creates strong, unique passwords based on user input, while the analyzer checks passwords against common weaknesses and breached databases.

## Features
### Password Generation
- Generates passwords using user-provided words and numbers
- Random capitalization and merging of words
- Special character substitutions
- Number insertion in random positions
- Ensures passwords meet strength criteria

### Password Analysis
- Checks passwords against a **breached password database** (MySQL)
- Identifies common weak patterns
- Detects repeated characters and string patterns
- Ensures password length is between **9-20 characters**

## Installation
### Clone the repository
```sh
git clone https://github.com/yourusername/password-analyzer-generator.git
cd password-analyzer-generator
```

### Install dependencies
```sh
pip install mysql-connector-python
```

## Usage
### Running the script
```sh
python password_generator.py
```

### Follow the prompts
- Enter **five words** (at least 3 characters each)
- Enter **two numbers** (at least 2 digits each)
- Specify the number of passwords to generate

### Password Analysis
- The script will analyze generated passwords and check for weaknesses
- It verifies passwords against a breached database

## Code Breakdown
### Password Generator
```python
import random

# Function to randomly capitalize letters
def randomly_capitalize(s):
    result = ''
    for char in s:
        flag = random.randint(0, 1)
        result += char.upper() if flag == 0 else char.lower()
    return result
```

### Password Strength Analyzer
```python
import re

def password(v):
    if v == "\n" or v == " ":
        return "Password cannot be a newline or space!"
    
    if any(char == " " for char in v):
        return "Password cannot contain a space"
    
    if 9 <= len(v) <= 20:
        if re.search(r'(.)\1\1', v):
            return "Weak Password: Same character repeats three or more times in a row"
        if re.search(r'(..)(.*?)\1', v):
            return "Weak password: Same string pattern repetition"
        return "Strong Password!"
    else:
        return "Password length must be 9-20 characters!"
```



## Example Output
```
Enter five words: secure strong random complex safe
Enter two numbers: 12 34
Enter number of passwords required: 2
Final Password: StRoNg@RaNdOm12!
Final Password: CoMpLeX#SeCuRe34$
Strong Password!
Strong Password!
```

## Security Considerations
- Uses a **secure MySQL database** to check breached passwords
- Prevents weak password patterns
- Ensures passwords meet minimum complexity requirements

## Future Improvements
- Implement an **API** for real-time password checking
- Add support for **additional password policies**
- Improve password entropy scoring



