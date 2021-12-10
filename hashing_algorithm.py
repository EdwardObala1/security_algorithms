# Python custom objects are hashable by default. Their hash is derived from their Id.
class User:
    
    def __init__(self, name, occupation):

        self.name = name
        self.occupation = occupation

u1 = User('John Doe', 'gardener')
u2 = User('John Doe', 'gardener')

print('hash of user 1')
print(hash(u1))

print('hash of user 2')
print(hash(u2))

if (u1 == u2):
    print('same user')
else:
    print('different users')

u1 = User('John Doe', 'gardener')
u2 = User('John Doe', 'gardener')

print('hash of user 1')
print(hash(u1))

# The hash function returns the hash value of the object. The default implementation is derived from the Id of the object.