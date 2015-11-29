# Notes CS253 - Lesson 4: User Accounts and Security

#### Problem with current method of Cookie Hashing (using MD5)

* Currently we are creating the cookie as follows: `value,[HASH of the <value>]`
* However, here guessing that what we are using is md5 hash of that value isn't a very difficult thing

* So to solve this problem, what we need to do is, we need to add some **_secret knowledge_** here.
* So instead of hashing, the number 1 in our hash, what we need to do is we need to hash `(<a secret string> + number 1)` into a hash.
* So as long as this secret stays secret, a would be attacker, even if they know our algorithm, won't be able to forge a hash, because it is very difficult to find two inputs that equal to the same hash (this is one of the properties of a good hashing algorithm).

---

#### HMAC (Hashbased Message Authentication Code)
1. A specific library in Python specially for doing message authentication.
2. This is basically a special algorithm that is built into Python for when you want to combine a key with your value to create a hash.
3. It looks something like this:
`hmac(<a secret>, <key>, <hashing function>) --> [HASH]`

---

#### Password Hashing
*_Lets talk about using passwords for hashing_*

1. Say we have a table for users in our database, with a couple of columns, one for the user's name and another for the user's password.
2. Now, we might have a function that accepts username and password and verifies if the details are correct
3. The problem with this approach however, is that if this database gets compromised, you are in trouble. You give away all your users passwords.
4. Hence insteads of storing plain text passwords in our database, we will store a passsword hash.

---

#### Rainbow Table

1. Although passwords are hashed, we aren't completely safe yet. The problem is, there are a handful of good hashing algorithms that people would use for this sort of thing. Say for eg: we are using SHA256.
2. Now if somebody would go through and create a mapping of every word to the hash of that word, that would be a problem. Because, the whole strength of this hashing problem is that its really hard to get from the HASH to the plain text that led to that hash
3. So if you have already computed hash for all the words, and all you have to do is, create an inverse table. Once somebody has this table of all of these words computed, they are done!
4. That would be like an attacker gaining access to a database of SHA256 of passwords.
5. This table exists, and its called a *RAINBOW TABLE*. You can google for it.
6. A simple way to get around this would be add in some secret just as we did in case of cookie hashing, however we should not enter the same secret over and over.
7. Hence we use something called a *SALT*.

---

#### Salt

1. Now in our user table, we are storing the username and we are storing the hash of the password. But instead of storing just the hash, we are going to add a secret to it.
2. But this time it is not really a secret, instead we are going to say:
This hash (h) = hash of the password + salt.
`h = H(passwrd + salt)`
3. This salt looks very similar to the use of secret as we did in case of cookie hashing, however this salt is just some random characters and it is stored in the hash field.

---

#### Bcrypt (This is not built into Python)

1. Generally you can work with SHA256, they work ok.
2. The problem with most hashing functions is that they are designed to work fast. So generally, this is a good thing.
3. However, in cases like passwords, when its much more likely that somebody is gonna try to brute force you, it would be really cool if we had a hashing function that is both, really good but also kind of slow.
4. One such function is called bcrypt.
5. Bcrypt takes an extra parameter which basically says, how long do you want it to take.
6. Hence we can explicitly ask this function to stay slow no matter how speedy the computers get overtime.

---

#### HTTPS

1. We know how to store a password securely on the server.
2. However, we still have a issue that if you type in a password, the password is actually sent in plain text over the internet.
3. So if you really really care about the passwords being encrypted the whole way, so that some bad guy in the middle can't just sniff the password, you use HTTPS
4. HTTPS is just like HTTP except that its encrypted over SSL.

---