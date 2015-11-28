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

