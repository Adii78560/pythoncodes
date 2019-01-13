from utilities.cliniqueutility import CliniqueManagement

if __name__ == '__main__':
    cliniqueManagement_obj = CliniqueManagement()

    patient_file = cliniqueManagement_obj.read_Json_file_of_Patient()
    # print(patient_file)
    appointment_file = cliniqueManagement_obj.readJsonfileofAppoinment()
    # print(appointment_file)

    cliniqueManagement_obj.getUserInput()
