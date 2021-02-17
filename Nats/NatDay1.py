var_a = 'This is a string.'

var_b = 'bark'
d=130

var_c = ['This','is','a','list','on', 'the',21,'day data challenge.']

#print(var_c)

x = 'string'
y = 2021

s = 'foo'
signature= 'Dot'

print(f'a dog goes {var_b}')

lease = '''Dear Dot, 
           This document validates that you are beholden to a monthly payment of rent for this house.
           Rent is to be paid by the first of every month.
           Fill in your signature to agree to these terms.  
            -------------
            Please Sign Here: 
'''

new_lease = f'''Dear Dot, 
           This document validates that you are beholden to a monthly payment of rent for this house.
           Rent is to be paid by the first of every month.
           Fill in your signature to agree to these terms.  
            -------------
            Please Sign Here: {signature}
            '''
print(new_lease)