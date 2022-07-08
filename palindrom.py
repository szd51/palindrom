def czyPalindrom(x):
    """
    Check if given word is palindrom
    """
    x = x.lower().replace(" ", "")
    n = len(x)
    for i in range(n-1):
        if x[i] != x[n-1-i]:
            return False
    return True; 
print("Program sprawdzajacy czy slowo jest palindromem")
czyPalindrom ("")
print("Podane slowo " + ("jest " if(czyPalindrom("kajak")) else "nie jest ") + "palindromem")
