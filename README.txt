[Objective]:
Create a program using python that will following the RSA public private key encryption Algorithm
Will be following the Decription of the Algoithm using Network Security Essentials Applications and Standards sixth edition by William Stallings

[Requirments]:
Take in one parameter as the argument being the input file

[Algorithm]
Read the name of the input file using command line argument
There will be two prime numbers on the input file
	Line 1 of the file will have primes p and q
	p and q are seperated by 1 or more spaces
p * q to get value n 
Eulter Totient (ET(x)) will need to be calculated
	ET(n) = (p - 1) * (q - 1)
	At this point n is also not a prime since it is a multiple of primes
We will need to fine the coprimes of ET(n)
	Theses are integers that are less than ET(n) and relatively prime with ET(n)
	These values are to be stored in a list
3rd smallest coprime will be PRIVATE key
Matching d value will need to find by taking d

	