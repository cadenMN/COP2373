
# Compares user input to proper number formatting for phone numbers,
# social security numbers, and zip codes.
def main():

    # Program uses regular expressions
    import re

    # Define patterns for comparison
    phone = r'\d\d\d[ -]\d\d\d[ -]\d\d\d\d$'
    security = r'\d\d\d[ -]\d\d[ -]\d\d\d\d$'
    zipcode = r'\d\d\d\d\d$'

    # User input to be compared to patterns
    print('')
    userPhone = input('Enter your phone number separated by spaces or hyphens (Ex: ###-###-####): ')
    userSecurity = input('Enter your social security number separated by spaces or hyphens (Ex: ###-##-####): ')
    userZipcode = input('Enter your zip code (Ex: #####): ')
    print('')

    # Comparing and printing results to user
    # Phone number comparison
    if re.match(phone, userPhone):
        print('Your phone number is valid!')
    else:
        print('You entered an invalid phone number!')
    # Social security number comparison
    if re.match(security, userSecurity):
        print('Your security code is valid!')
    else:
        print('You entered an invalid security code!')
    # Zipcode comparison
    if re.match(zipcode, userZipcode):
        print('Your zip code is valid!')
    else:
        print('You entered an invalid zip code!')

    # End of program


# Call to run program
main()