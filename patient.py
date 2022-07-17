from user import User


class Patient(User):
    def __init__(self,firstName,lastName,age,sex,address,MedicalHistory):
        self.patientId = super.userId
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.sex = sex 
        self.address = address
        self.MedicalHistory = MedicalHistory

    def createPatientDetails():
        pass

    def dischargePatient():
        pass

    def generateDischargeReport():
        pass

    def generatePatientCaseSheet():
        pass

    def payBill():
        pass

    def takedoctorsAppointment():
        pass

    def takeTestingAppointment():
        pass








