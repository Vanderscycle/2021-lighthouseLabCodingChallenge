# Don't edit this variable!
lease = '''
            Dear Dot, 
            This document validates that you are beholden to a monthly payment of rent for this house.
            Rent is to be paid by the first of every month.
            Fill in your signature to agree to these terms.  
            -------------
            Please Sign Here: 
'''

signature = "Dot"

# Needs to be done this way for formatting reasons.
# It seems like it kinda defeats the point of storing the lease in a variable just to manually copy and paste it.
new_lease = f'''
            Dear Dot, 
            This document validates that you are beholden to a monthly payment of rent for this house.
            Rent is to be paid by the first of every month.
            Fill in your signature to agree to these terms.  
            -------------
            Please Sign Here: {signature}
'''

print(new_lease)