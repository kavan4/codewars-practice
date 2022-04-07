def hex_switch_map (mod16val):
    # run a switch statement to check the the mod16 value. 
    if mod16val == 10:
        return 'A'
    
    elif mod16val == 11:
        return 'B'
    
    elif mod16val == 12:
        return 'C'
    
    elif mod16val == 13:
        return 'D'
    
    elif mod16val == 14:
        return 'E'
    
    elif mod16val == 15:
        return 'F' 

def rgb(r, g, b):
    # init temp arr for storing stuff
    temp_arr = []
    #loop over rgb and find remainder and quotient
    for val in (r,g,b):
        #cap to upper and lower bounds
        if val > 255 :
            val = 255
        elif val < 0:
            val = 0
        #remainder and quotient
        val1_hex = val//16
        val2_hex = val%16
        #if remainder > 9, map
        if val2_hex >= 10 :
            val2_hex_map = hex_switch_map(val2_hex) 
        # else keep
        elif val2_hex < 10 :
            val2_hex_map = str(val2_hex)
        #if quotient > 9, map
        if val1_hex >= 10 :
            val1_hex_map = hex_switch_map(val1_hex) 
        # else keep
        elif val1_hex < 10 :
            val1_hex_map = str(val1_hex)
        
        #combine to val_hex
        val_hex = val1_hex_map + val2_hex_map
        
        #push to temp array
        temp_arr.append(val_hex)
    return "".join(temp_arr)