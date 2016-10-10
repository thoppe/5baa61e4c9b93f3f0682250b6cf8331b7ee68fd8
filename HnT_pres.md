### Cracking passwords with "deep learning"
!(images/man_code.mp4) <<height:460px;transparent>>

Source Code: [https://github.com/thoppe/5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8](https://github.com/thoppe/5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8)
----------
[travis.hoppe](http://thoppe.github.io/), [@metasemantic](https://twitter.com/metasemantic)
  
====
## Please add me <br> to your LinkedIn network...
!(images/linkedin.png) <<height:400px;transparent>>
!(images/cat_hack.mp4) <<height:410px;>>

### In 2012 the entire LinkedIn database of emails/passwords were dumped
  
====

## In 2016, this database was found floating on the darkweb ... 
(all 65 millon email addresses & passwords) 
!(images/hate_hackers.mp4) <<height:460px;transparent>> people be like...

====

### Fortunately the passwords were "hashed"
!(images/hash_browns.jpg) <<height:200px;transparent>>

####    amsoawen@rotterdam.nl, cat
####    mankmrx@yahoo.com, password
####    bigryder@yahoo.nl, cat 
####    amrita1240@gmail.com, mrsbutterworth
--------------------------------------
####    amsoawen@rotterdam.nl, *9d989e8d27dc9e0ec3389fc855f142c3d40f0c50*
####    mankmrx@yahoo.com, 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8
####    bigryder@yahoo.nl, *9d989e8d27dc9e0ec3389fc855f142c3d40f0c50*
####    amrita1240@gmail.com, 71785ac6c2fb928c0652cdc26e1aba389565242b

====
### Unfortunately, they were hashed with SHA-1 <br> which can be brute-forced (see [hashCat](https://hashcat.net/hashcat/))
!(images/code_cycle.mp4) <<height:300px;transparent>> (~ 8 millon hashes per second)


====+

  
# but that's no fun ...
====

# RNN-LSTM
Recurrent Reural Network with Long Short-Term Memory
With NLP? Generate *new text* from observed *linguistic patterns*
====+  
<br><br>
### prior work: [arXiV title generator](http://thoppe.github.io/RNN_science_titles/HnT_RNN_arXiv.html#/)
Hack && Tell Round 26: The Curious Camaraderie of Code
    1. A User-Friendly Code to Diagnose Chromospheric Plasmas
    2. Shock Parameters in Astrophysics
    3. Wormholes in the accelerating universe
    4. Phase recovering by Electron Deconvolution on Gravitational Wave Signals
    5. Averaging and Cosmological Observations
    6. Developments of global mass function
    7. VIMOS total transmission profiles for broad-band filters
    8. Bayesian plane for MACS. Atmospheric Cherenkov Telescopes
    9. Gaseous Inner Disks
    10. Science and Fluorescence Detection Time Scales with Transient Least Squares II. Mask coronagraphs
    11. Dissipation of Magnetic Flux in Primordial Star Formation: From Run-away Phase to Mass Accretion Phase
    12. High-energy Cosmic Ray Shower Observations on Pulsar Disk
    13. Thermal inertia of near-Earth asteroids and implications for the magnitude of the Yarkovsky effect
    14. Activity Ionization and Instrumentation
    15. A 610 MHz Survey of the 1H XMM-Newton Chandra Survey Field
    16. Estimating visible variability in the neutron a cross-correlations

====

## Passwords?
dantes1234, mif135, Jenna015, salidams, karla0304, fia0202, kpn1954, sairames,
j200767, 8646463, csumit, zamman13, jackdosn, mattymatt, 2439nc, lymic123, 
mca15a, hkumar, merger2011, mick462, 9743399, 28272408, 61166s, adh1323, 
betapapa, shaq1979, 1222xxxx, castane12, emmaan1, mazdabil, 4611av, tekereg,
9426469, 1111yess, kalgar01, pjcent, gmom1995, zarma38, adj2911, Lou7010, 
ASOSCI, jonavera, meeguin, melinders, yopam2, hk6325, lairree, 8948748, 
pat6963, 24002933, girls1975, madia2309, jajax5, dec1560, 99923070, bedrule,
karennick, powernap, pascully, bones987, sazza47, wg3740, smarty333, 17507711,
mcnabu, tim1664, b192021, 1tailer1, ivanmasa, badgal10, jasper1225, FM1949, 
Porgie1, bookiebo, wj2188, pikolo11, 19768030, jan271971, ric2929, mstg01,
lled44, lspook, 1704653, madjan1969, cupidread, vick7500, kr3743, johnpeter1,
friede03, karem311, 05011981, 4672376, livylin, mutumene, Claude25, kar7413,

====

### Most password "patterns" are predictable.
!(images/so_dumb.mp4) <<height:400px;transparent>>

Most common hash is `5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8`
which is "`password`". No, really. 176,120 accounts, or 1 out of every 360 people.

  
====

### How it works

!(images/flowchart.svg)  <<height:600px;transparent>>


====

  
        
#  Thanks, you!
Say hello: [@metasemantic](https://twitter.com/metasemantic)
