#Larvae painful obstacle LED activation script

import math

@returns(int)

def process(value): #input parameter is an XY coordinate tuple
    x_larva = value.x #current X position of the larva 
    x_A = 157   # Start of obstacle gradient (Left)
    x_B = 212   # Start of primary obstacle (middle strip left)
    x_C = 232   # End of primary obstacle (middle strip right)
    x_D = 287   # End of obstacle gradient (Right)
    LED_OFF_VALUE = 255

    #LED value notes:
    #   LED is turned on by default, script decreases intensity based on larva position
    #   0 = LED on (maximum intensity)
    #   255 = LED off (minimum intensity)

    #Larva is to the left of the pain region. No stimulus -> LED off
    if (x_larva < x_A):
        returnValue = LED_OFF_VALUE
        return int(returnValue)

    #Larva is inside the left gradient region (but not the middle strip) -> calculate intensity based on X position
    elif (x_A <= x_larva and x_larva < x_B):
        returnValue = (1 - computeGradient(x_A, x_B, x_larva)) * LED_OFF_VALUE
        return int(returnValue)

    #Larva is inside the middle strip, max intensity for entire width
    elif (x_B <= x_larva and x_larva < x_C):
        returnValue = 0
        return int(returnValue)

    #Larva is inside the right gradient region (but not the middle strip) -> calculate intensity based on X position
    elif (x_C <= x_larva and x_larva < x_D):
        returnValue = computeGradient(x_C, x_D, x_larva) * LED_OFF_VALUE
        return int(returnValue)

    #Larva is to the right of the pain region. No stimulus -> LED off
    else:
        returnValue = LED_OFF_VALUE
        return int(returnValue)

#Function to compute distance between the larva and the edges of the middle strip as a percent
def computeGradient(x_1, x_2, x_larva):
    return ((x_larva-x_1) / (x_2-x_1))
