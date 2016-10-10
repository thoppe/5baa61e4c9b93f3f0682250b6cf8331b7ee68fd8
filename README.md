### 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8
(SHA-1 hash of "password")
---------------------------------------------------------------------------
  

Back in 2012, LinkedIn suffered a hack that leaked (presumably) the entire database of user emails and passwords. The passwords were not stored in plain-text, they were hashed with (SHA-1)[https://en.wikipedia.org/wiki/SHA-1] and left (unsalted)[https://en.wikipedia.org/wiki/Salt_(cryptography)]. This means that the passwords were put through a one-way cryptographic function that left the password unknown unless guessed exactly. For example, instead of:

    amsoawen@rotterdam.nl, cat
    mankmrx@yahoo.com, password
    amrita1240@gmail.com, mrsbutterworth
    bigryder@yahoo.nl, cat

The password dump looked like
  
    amsoawen@rotterdam.nl, 9d989e8d27dc9e0ec3389fc855f142c3d40f0c50
    mankmrx@yahoo.com, 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8
    amrita1240@gmail.com, 71785ac6c2fb928c0652cdc26e1aba389565242b
    bigryder@yahoo.nl, 9d989e8d27dc9e0ec3389fc855f142c3d40f0c50

There are two common attacks to crack the passwords, either brute-force all combinations or use a dictionary of previously identified passwords. The first method utilizes all the processing power of the machine, CPU/GPU like (hashCat)[https://github.com/hashcat/hashcat].

Interested in more password dumps? A comprehensive list can be found at (https://www.vigilante.pw/)[https://www.vigilante.pw/].

More reading about the source data can be found here:

http://arstechnica.com/security/2016/06/how-linkedins-password-sloppiness-hurts-us-all/