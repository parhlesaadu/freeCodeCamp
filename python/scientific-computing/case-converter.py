def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    #   append processed characters one by one
    for char in pascal_or_camel_cased_string:
        if char.isupper():
          converted_character = '_' + char.lower()
          snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    #  final processing of the list (python strings are immutable, so each method returns a new string object)
    snake_cased_string = ''.join(snake_cased_char_list)   # returns the concatenation of all strings in the iterable using the calling string as a separator
    clean_snake_cased_string = snake_cased_string.strip('_')    # returns new string with parameter str removed from start and end of calling str

    return clean_snake_cased_string

def convert_to_snake_case_list_comprehension(pascal_or_camel_cased_string):
    snake_cased_char_list = ['_' + char.lower() if char.isupper() else char for char in pascal_or_camel_cased_string]    # if no else clause, if statement goes after 'for x in y'
    return ''.join(snake_cased_char_list).strip('_')

#    self-written algorithm
def convertToPascalOrCamelCase(snake_cased_str, Pascal=True):
    if Pascal:    # first letter to be capitalised
        snake_cased_str = '_' + snake_cased_str
    lis = []
    for char in snake_cased_str:
        if not lis:    # list is empty
            lis.append(char)
        elif lis[-1] == '_':    # last char is underscore
            lis.pop()
            lis.append(char.upper())
        else:
            lis.append(char)
    return ''.join(lis)
