# secret_messages.py

Inspired by CTFs, i decided for my second trimester project i created a secure login system to hide some sort of secret message or information.

The data structure used was dictionaries, which stored an md5 hashed username as a key, and the value was a list containing an md5 hashed password in the `0` position and the AES keyed encryption in the `1` position.

The dictionary was extremely effective for this purpose, and, due to the secure encryption, looks completely ridiculous, but is very easy to work with in code.  After the data is imported from Excel, the dictionary object looks like this: 

```
{'e55b100fbf0457be4a660a215cf13a40': ['d581a686b32e406128237faf69ec9d69', 'pwnxc31MtWEdhJ1CvR0SML1GIu0Ra6uslrFj3a6Mfso='], 'ecadcc86b826012f012fa427c4115614': ['66d62ed87061ab1e8374fdb07bed5af7', 'kfQc1Rb/GYfrW1ShgxuO1Q/tvfqssAh7FEieTta1cbnCobtn+YWeflMgSa2gawBZpuYtcD7p+3nBVHLwhlis+KKw50FUI338YUPeJvYEwOu2nxQpbMvk0WhKF7yL1uqZyMRLhGbxBmBSvrmdUSoXv6LjAJZPReB5SwcjTyLwp14XC/AmxEu10m5wBAhUiQ26sPx9yId+JHVW7lg6IDLs8g=='], 'cb525f817e0092b3cf415aa813cc98be': ['23fd44228071730e3457dc5de887b3ae', 'Mc/RDyEkCEd6pX2D81AOxYUL9gTXexvjLczJDSNJ1Q5P8f7aLDANLAvgw+wuqJYA8ppbQsXg0LXMFtbpOH7DUw=='], '69a99f608340f12d821de723a60f3c41': ['098f6bcd4621d373cade4e832627b4f6', 'vLVdXDkVvoQshZN0F9HsxbCzOlTIW2e2XIPxl7YQ41U='], '61409aa1fd47d4a5332de23cbf59a36f': ['0cbc6611f5540bd0809a388dc95a615b', 'FPR0vsbx7a+VgU3FsLHYT0Envto5ufU3D/CxPM0Y6Y8='], 'eb8d6ddf6e16b42471a2d251b2f45d90': ['96de354fa3df933535d4859d07a3ba72', 'DuuiumkLhlh5nnZRgw6AmXUCHOBUOXQhgrJYE+lOVUvx05KWZNeBcFNWJSxXewTEdT5wjmr5h3QnUWzRFSrHvG+PFd8p0nXv8NW1VXYJzthhs8bnZKfzH4KhoUqJXGLJnz2ffRewkaqawQeCr7X1KBsJRZ+JFiN+p2XRkHHsjp9ofCipSLTLdBiz/Oy6V78ArGnr4ZuRhRIZXQO40yjFJEuRk8TPT0kkCQ2s7lS44Gmr9AuqurxmuUj5W72Wx2bEiTnr61ouLaebkdZbulhHkg6vIrD5GFKYlK6gg+wQTMs1zvYcb/gD8jwNcMo07dRgpVtNU+sZf2Qlp6gW9+1oLQ=='], 'c988fa7c33ce43962b9803702b747a35': ['89f3a21f6d184df6a92c9a4097380c22', 'oL7RKPXU9Vl0w87i1RuNvZLS8dPn46WMsWWox7ctsb8=']}
```

Both the username and password are unecrypted with non-reversable md5 hashing, and the message is stored using reversable AES encryption, the key for which is the password, so all data is very secure.

Excel through openpyxl was used to store the data to be used and reused, although if a similar implementation was to be actually used on something like a server backend, some sort of database would be better suited for this purpose, as the data is transfered into memory and then only saved at the end, or i would be able to implement live updating of the excel file if that was necessary.

For instance, a user registered in the system is `FirstUser` with password `UserFirst`
![image](https://github.com/jccherry/Data-Structures-And-Algorithms/blob/master/Second%20Trimester%20Projects/John/Screen%20Shot%202018-02-11%20at%208.22.31%20PM.png?raw=true)



### Required Libraries

* Openpyxl
* Pycrypto
* Hashlib
* base64
