def cipher(text, shift, encrypt=True):
    
    """
    The Caesar cipher is one of the simplest and most widely known encryption techniques.
    This cipher takes string data and decode it by shifting each letter by the number of positions specified in the alphabet. 
    
    Args:
        text: Input string data to be ciphered.
        shift: Number of digits in the alphabet to shift in the right direction.
        encrypt: True/False indicator defining whether or not the string is to be encrypted by this function.
        
    Returns:
      Ciphered text with input string data 'text' shifted the number of units defined by 'shift' input. 
      
    Example of Usage:
        >>> print([cipher('Chef',3)])
        'Fkhi'
    """
    
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text