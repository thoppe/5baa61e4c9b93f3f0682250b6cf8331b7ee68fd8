# 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8
_Cracking passwords with deep learning_

--------------------------------------------------------------------
 
### Backstory

Back in 2012, [LinkedIn](https://www.linkedin.com/) suffered a hack that leaked the entire database of user emails and passwords.
The passwords were not stored in plain-text, they were hashed with [SHA-1](https://en.wikipedia.org/wiki/SHA-1) and left [unsalted](https://en.wikipedia.org/wiki/Salt_(cryptography)).
This means that the passwords were put through a one-way cryptographic function that left the password unknown unless guessed exactly.
For example, instead of:

    amsoawen@rotterdam.nl, cat
    mankmrx@yahoo.com, password
    amrita1240@gmail.com, mrsbutterworth
    bigryder@yahoo.nl, cat

The password dump looked like
  
    amsoawen@rotterdam.nl, 9d989e8d27dc9e0ec3389fc855f142c3d40f0c50
    mankmrx@yahoo.com, 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8
    amrita1240@gmail.com, 71785ac6c2fb928c0652cdc26e1aba389565242b
    bigryder@yahoo.nl, 9d989e8d27dc9e0ec3389fc855f142c3d40f0c50

There are two common attacks to crack the passwords, either brute-force all combinations or use a dictionary of previously identified passwords.
The first method utilizes the raw processing power of your hardware (CPU or GPU), see [hashCat](https://github.com/hashcat/hashcat) for an example of state-of-the-art.
The second method, is effective but limited in scope due to the pre-determined list of passwords.

This project proposes a third method.

### Experiment

We utilize a simple RNN-LSTM (Recurrent Neural Network with Long Short-Term Memory) built with [tensorflow](https://github.com/tensorflow/tensorflow) and [tflearn](https://github.com/tflearn/tflearn).
This RNN reads from a [set of starter passwords](starter_passwords.txt) and tries to predict new passwords from the linguistic patterns observed.
These passwords are then validated against the LinkedIn dump and the RNN is re-trained.

![](images/flowchart.png)

To improve sampling speed, we sample from the RNN using hundreds of independent parallel streams.
This avoids the expensive overhead of copying to the GPU for each character sampled.
Full implementation can be found in [src/model.py](src/model.py).

### Results

+ Started with 654,500 matching passwords.
+ Ran 6 cycles of validate/train/sample (1 day/cycle).
+ Generated [**8,943,093** new passwords](generated_passwords.txt).
+ ~1300% enrichment from starter passwords.

### Password lists

+ [starter_passwords.txt](starter_passwords.txt)
+ [generated_passwords.txt](generated_passwords.txt)

### Presentations

Hack && Tell, Round 37: Cell Out (with DC NLP!) [presentation link](http://thoppe.github.io/5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8/HnT_pres.html)

### Further reading

Want to find more password dumps? Start here, [https://www.vigilante.pw/](https://www.vigilante.pw/]).

More reading about the source data can be found in this nice [Ars writeup](http://arstechnica.com/security/2016/06/how-linkedins-password-sloppiness-hurts-us-all/).