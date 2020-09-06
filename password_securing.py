SECURE = (('s', '$'), ('a' , '@'), ('o', '0'), ('i', '!'), ('and' , '&'))

def securePassword(password):
    for a,b in SECURE:
        password = password.replace(a, b)
    return password

if __name__ == "__main__":
    password = input("Enput ur password: ")
    password = securePassword(password)
    print(f"Your password is secure now. Your new secure password is {password}")
    
