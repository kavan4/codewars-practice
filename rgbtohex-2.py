def hex_map(val):
    #reference hex 'list'
    hex_ref = '0123456789ABCDEF'
    
    #bind values for val
    if val > 255:
        val = 255
    if val < 0 :
        val = 0
    
    #find remainder and quotient and map to reference hex list
    rem = val%16
    rem_hex = hex_ref[rem]
    quo = val//16
    quo_hex = hex_ref[quo]

    #return quo+rem as strs
    return quo_hex + rem_hex

def rgb(r,g,b) :
    r_hex = hex_map(r)
    g_hex = hex_map(g)
    b_hex = hex_map(b)

    return r_hex + g_hex + b_hex