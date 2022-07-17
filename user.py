import uuid

class User:
    def __init__(self,firstName,lastName,age,username,typeofUser):
        self.userId = uuid.uuid1()
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.username = username
        self.typeofUser = typeofUser

    def changeContactDetails():
        pass

    def displayUserDetails():
        pass

    def changeUsername():
        pass