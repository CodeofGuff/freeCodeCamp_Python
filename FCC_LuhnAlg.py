


# Luhn Algorithm from freecodecamp
# validate a variety of identification numbers

# From the right to left, double the value of every second digit; 
# if the product is greater than 9, sum the digits of the products. 
# Take the sum of all the digits. If the sum of all the digits 
# is a multiple of 10, then the number is valid; else it is not valid.


# the str class has a method called maketrans
# that can help us create a translation table
# This table can be used to replace characters in a string:
# str.maketrans({'t': 'c', 'l': 'b'})
# The above, when called on a string, will replace all t characters with c and all l characters with b.

# You can also use the index operator to access a range of 
# characters in a string with string[x:y:h] 
# Where x is the starting index, y is the ending index,
# and h is the step (the amount of characters to skip over).

def verify_card_number(card_number):
        sum_of_odd_digits = 0
        card_number_reversed = card_number[::-1] # Slice is [x:y:h] with both blank, we reverse the order with -1
        odd_digits = card_number_reversed[::2] # contains every other digits in the card_number_reversed str. 
        for d in odd_digits:
            sum_of_odd_digits += int(d)
        sum_of_even_digits = 0
        even_digits = card_number_reversed[1::2]
        for d in even_digits:
            number = int(d) * 2
            if number >= 10:
                number = number // 10 + number % 10 #  double every second digit, starting from the right. If the result of doubling the number is greater than or equal to 10, add the two digits together. 
            sum_of_even_digits += number
        total = sum_of_even_digits + sum_of_odd_digits
        return 0 == total % 10
            
def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID')
    
main()