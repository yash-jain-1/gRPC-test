import addressBook_pb2
person = addressBook_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressBook_pb2.Person.PHONE_TYPE_WORK

# person.no_such_field = 1  # raises AttributeError
# person.id = "1234"        # raises TypeError

print(person.IsInitialized() )
 # True
print(person)