# [Problem 2: Biorhythms](https://www.unb.ca/saintjohn/sase/_assets/documents/problems2019.pdf)

According to the theory of biorhythms, aspects of people’s life (physical, emotional, intellectual, etc.) are influenced by rhythmic biological cycles: like a sine wave starting at birth, with cycles of various lengths depending on the aspect: 23 days for “physical”, 28 days for “emotional”, and 33 days for “intellectual”. The following graph shows a wave for the “physical” aspect (the vertical bars show the beginning and end of each cycle): 

<img width="723" alt="image" src="https://github.com/QuanTrinhCA/Biorhythms/assets/44539970/1a9f1ae9-3ba7-4078-9d1e-39e196152a90">

With this, it is suggested that a person's level of ability in each of these domains can be predicted from day to day. Our goal for this problem is to write a program that given the number of days since birth, indicates when the next high peak and low peak will be in that person’s life, for each of the 3 aspects above. 

This can be calculated by taking the remainder of the division by 23, 28, or 33 (depending on the aspect), and compare it with what such remainder should be at those peaks:

- Physical: high peak at remainder = 6, low peak at remainder = 17
- Emotional: high peak at remainder = 7, low peak at remainder = 21
- Intellectual: high peak at remainder = 8, low peak at remainder = 25
  
For the example below where the number of days since birth is 7300 (see the example input), we have the following calculations:

- Physical: 7300 = 317 x 23 + 9 (i.e., remainder of division by 23 is 9)
- So the next high peak is in 20 days 
- ( (23 – 9) days until the end of the cycle + 6 days in the new cycle)
- And the next low peak is in 8 days
- ( (17 – 9) days until that peak, which will occur in the current cycle)
      
      
Similar calculations can be done for the emotional cycle (remainder of 7300 divided by 28 is 20) 
and the intellectual cycle (remainder of 7300 divided by 33 is 7). The output of your program 
should be those numbers (high peak then low peak), one per line, for the 3 aspects above in 
that sequence (see example output – line 1 and 2 for physical, 3 and 4 for emotional, and 5 and 
6 for intellectual). Note: the number printed can be zero if we are already on a peak.

## Sample Input 1
```
7300
```

## Sample Output 1
```
20
8
15
1
1
18
```
