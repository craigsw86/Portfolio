import mysql.connector
from datetime import date

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="clinic_db"
    )

def add_patient():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    gender = input("Enter gender (Male/Female/Other): ")
    contact_info = input("Enter contact info: ")
    conn = connect_db()
    cursor = conn.cursor()
    sql = """
        INSERT INTO patients (first_name, last_name, date_of_birth, gender, contact_info)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (first_name, last_name, dob, gender, contact_info))
    conn.commit()
    print("Patient added successfully.")
    conn.close()

def view_patients():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, first_name, last_name, date_of_birth, gender, contact_info FROM patients")
    for patient in cursor.fetchall():
        print(patient)
    conn.close()

def delete_patient():
    patient_id = input("Enter patient ID to delete: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE id = %s", (patient_id,))
    conn.commit()
    print("Patient deleted successfully.")
    conn.close()

def update_patient():
    patient_id = input("Enter patient ID to update: ")
    first_name = input("Enter new first name: ")
    last_name = input("Enter new last name: ")
    dob = input("Enter new date of birth (YYYY-MM-DD): ")
    gender = input("Enter new gender (Male/Female/Other): ")
    contact_info = input("Enter new contact info: ")
    conn = connect_db()
    cursor = conn.cursor()
    sql = """
        UPDATE patients SET first_name=%s, last_name=%s, date_of_birth=%s, gender=%s, contact_info=%s
        WHERE id=%s
    """
    cursor.execute(sql, (first_name, last_name, dob, gender, contact_info, patient_id))
    conn.commit()
    print("Patient updated successfully.")
    conn.close()

def main_menu():
    while True:
        print("\n--- Patient Records CLI ---")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            update_patient()
        elif choice == "4":
            delete_patient()
        elif choice == "5":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()
