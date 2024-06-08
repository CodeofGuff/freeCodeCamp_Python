



# Case Converter

# Learning list comprehension
# Converting camelCase or PascalCase into a snake_case string
# List comprehensions in Python are a concise way to construct 
# a list without using loops or the .append() method. 
# Apart from being briefer, list comprehensions often run faster.
#Strings in pascal case start with a capital char. 
# When you start a list comprehension with an if statement,
# Python requires you to also add an else clause to the expression.
 
def convert_to_snake_case(pascal_or_camel_cased_string):
 #   snake_cased_char_list = []
  #  for char in pascal_or_camel_cased_string:
   #     if char.isupper():
    #        converted_character = '_' + char.lower()
     #       snake_cased_char_list.append(converted_character)
      #  else:
       #     snake_cased_char_list.append(char)
        #    snake_cased_string = ''.join(snake_cased_char_list)
         #   clean_snake_cased_string = snake_cased_string.strip('_') #'strips' the argument from the string
          #  return clean_snake_cased_string
          #BELOW IS ALL THE ABOVE WITH LIST COMPREHENSION IN PRACTICE
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]
    return ''.join(snake_cased_char_list).strip('_')
            
def main():
    print(convert_to_snake_case('aLongANDComplexString'))

if __name__ == '__main__':
    main()





