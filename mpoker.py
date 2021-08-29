import random 
# Generating Cards Deck 
cardWeight = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"] 
cardShape = ["diamonds","hearts","spades","clubs"] 
cardDeck=[] 
for i in cardShape: 
    for j in cardWeight: 
        card = i + " " + j cardDeck.append(card)

# Representing each card by numbers from 11 to 62 
numberDeck = [] 
for i in range(11,63): 
    numberDeck.append(i)

# Shuffling Cards function Fisher-Yates Shuffling Algorithm 
def shuffle(cardDeck): 
    for i in range(51, 0, -1): 
        j = random.randint(0, i + 1) 
        cardDeck[i], cardDeck[j] = cardDeck[j], cardDeck[i] 
        return cardDeck

#padding function 
def padding(cardDeck): 
    for i in cardDeck: 
        j = random.randint(0, 4) 
        for k in range(0,j+1): 
            l = random.randint(1,10) 
            i = (i*10)+l 
            return cardDeck

def prime_check(a): 
    if(a==2): 
        return True
    elif((a<2) or ((a%2)==0)): 
        return False 
    elif(a>2): 
        for i in range(2,a): 
            if not(a%i): 
                return False 
        return True

#GCD 
def egcd(a,b): 
    if b==0: 
        return a 
    else: 
        return egcd(b,a%b)
        
#Extended Euclidean Algorithm 
def eea(a,b): 
    if(a%b==0): 
        return(b,0,1) 
    else: 
        gcd,s,t = eea(b,a%b) 
        s = s-((a//b) * t) 
        return(gcd,t,s) 

#Multiplicative Inverse 
def mult_inv(e,r): 
    gcd,s,_=eea(e,r) 
    if(gcd!=1): 
        return None 
    else: 
        return s%r

#encryption function 
def encrypt(m,e,n): 
    return ((m**e)%n)

#decryption function 
def decrypt(c,d,n): 
    return (c**d)%n

#function for verifying the cards
def verify(arr,pn): 
    d = int(input("Enter opponent's d value: ")) 
    oCards=[] for i in range(0,5): 
    m = decrypt(arr[i],d,pn) 
    oCards.append(cardDeck[int(str(m)[:2])-11]) 
    print("\n opponent's cards Are\n") 
    for i in oCards: 
        print(i)

player = int(input("Enter 1 for player1 and 2 for player2 : "))

if player==1: 
    p = int(input("Enter p: ")) 
    check_p = prime_check(p) 
    while (check_p == False): 
        p = int(input("Enter a prime number for p: ")) 
        check_p = prime_check(p) 
        q = int(input("Enter q: ")) 
        check_q = prime_check(q) 
        while (check_q == False): 
            q = int(input("Enter a prime number for q: ")) 
            check_q = prime_check(q)
        n = p * q 
        print("\nSend the below message to player2") 
        print("p = ",p) 
        print("q = ",q) 
        print("n = ",n) 
        print("\n") 
        # Eulers Toitent 
        r = (p - 1) * (q - 1) 
        # Taking e as input 
        e = int(input("Enter e: ")) 
        while(egcd(e,r)!=1): 
            print("Enter e such that its gcd with Eulers toitent is 1")
            e = int(input("Enter e : "))
        # Calculating d 
        d = mult_inv(e, r) 
        #shuffling cards 
        shuffledDeck = shuffle(numberDeck) 
        #Adding padding to the shuffled deck 
        finalDeck = padding(shuffledDeck) 
        #creating encrypted deck 
        encryptedDeck = [] 
        for i in finalDeck: 
            encryptedDeck.append(encrypt(i,e,n))