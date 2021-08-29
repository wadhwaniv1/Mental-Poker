# Mental-Poker

<h3>What is Mental Poker?</h3>
<br>
1. PLAYING POKER WITHOUT CARDS (i.e OVER TELEPHONE OR INTERNET).
<br>
2. NO TRUSTED THIRD PARTY OR SOURCE OF RANDOMNESS. WE ASSUME 2 PLAYERS, 52 CARDS.
<br>
3. FIVE CARDS ARE DEALT THEN ONE ROUND OF BETTING THEN ALL CARDS SHOWN.
<br>
<hr>
<h3> The SRA protocol </h3>
<br>
1. Invented by Shamir, Rivest and Adleman in1979.
<br>
2. Relies on a commutative encryption schemeie E A (E B (M)) = E B (E A (M))
<br>
3. Two players Alice and Bob together choose alarge prime number n, then Alice choosesher key A s.t. gcd(A,n-1) = 1 and Bobchooses B similarly.
<br>
4. Encode the 52 cards as integers. Encryption E A (M)= M A (mod n) Decryption D A (M) = M inv(A) (mod n)Bob permutes the cards to x 1,x 2,…,x 52 encryptsthem then sends to Alice E B (x i ).
<br>
5. Alice chooses 5 cards for herself, encrypts them andsends to Bob E A (E B (x i )). Also chooses 5 cardsfor Bob and sends them to him (without encrypting) E B(x i ).
<br>
6. Bob can now decrypt his cards to see his hand D B (E B(x i ) = x i. He also decrypts Alice’s cards then sendsthem back to her. Here is where we need commutativity soD B (E A (E B (x i ))) = E A (x i ) Alice receives hercards and decrypt them seeing her hand D A (E A (x i ))= x i.
<br>
<br>

For more information: <link>https://people.csail.mit.edu/rivest/pubs/SRA81.pdf</link>
