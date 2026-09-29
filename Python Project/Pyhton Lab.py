even_number = 10
while even_number > 0:
  print(even_number)
  even_number -= 2
print("Even numbers finished!")
lap = 1
while lap <= 5:
    print(lap)
    lap += 1
print("Lap finished!")
total = 0
number = 1
while number <= 5:
    total += number
    print(total)
    number += 1
print("sum finished!")
power = 1
while power <= 16:
    print(power)
    power *= 2
print("power of 2 finished!")
password = ""
while password != "python123":
    password = input("enter your password: ")
    if password != "python1123":
        print("incorrect,try again.")
print("Access granted.")
number = int(input("enter a number: "))
orignal_number = number
total = 0
while number > 0:
    total += number
    number -= 1
print(f"the user entered integer is {orignal_number}")
print(f"the sum found by the while loop is {total}")
user_number = int(input("enter a positive integer: "))
original_number = user_number
factorial = 1
while user_number > 0:
    factorial *= user_number
    user_number -= 1
print(f"The factorial of the user entered integer {original_number} is {factorial}")
greet = "hello world"
for letter in greet:
    print(letter)
user_text = input("enter a word or a sentence: ")
vowel_count = 0
for letter in user_text:
    if letter in "aeiou":
        vowel_count += 1
print(f"The total number of vowels in {user_text} is {vowel_count}")
user_word = input("enter a word:")
reversed_word = ""
for letter in user_word:
    reversed_word = letter + reversed_word
print(f"The reverse of the word {user_word} is {reversed_word} ")
text =input("enter a sentence:")
count = 0
for letter in text:
    count += 1
print(f"The user entered {text}")
print(f"The number of words in the user entered text is {count}")
name = input("enter your username:")
count = 0
for letter in name:
    count += 1
print(f"The user entered username {name}")
print(f"The number of words in the user entered name is {count}")
for number in range(1,51):

    


