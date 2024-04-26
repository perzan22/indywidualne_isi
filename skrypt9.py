import sqlite3
import os


def createDatabase():
    conn = sqlite3.connect('academy_database.db')

    cursor = conn.cursor()

    with open('baza.sql', 'r') as file:
        database = file.read()
    


    cursor.executescript(database)

    conn.commit()

    cursor.close()
    conn.close()

def showAllStudents():
    conn = sqlite3.connect('academy_database.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * from Student')

    students = cursor.fetchall()

    print('Wszyscy studenci uczelni: \n')

    for student in students:
        print("Nr indeksu:", student[0])
        print("Imię:", student[1])
        print("Nazwisko:", student[2])
        print("--------------------")
    
    cursor.close()
    conn.close()

def showAllStudentsFromGroup(grupa: int):

    conn = sqlite3.connect('academy_database.db')

    cursor = conn.cursor()

    cursor.execute('SELECT Student.imie, Student.nazwisko, Grupa_Studencka.nazwa_grupy from Student JOIN Grupa_Studencka ON Student.id_grupy = Grupa_Studencka.id_grupy WHERE Student.id_grupy = ?', (grupa,))

    students = cursor.fetchall()

    print(f'Grupa {students[0][2]}: ')
    for student in students:
        print("Imię:", student[0])
        print("Nazwisko:", student[1])
        print("--------------------")
    
    cursor.close()
    conn.close()

def showStudentsWithGradeAbove4():

    conn = sqlite3.connect('academy_database.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Przedmiot')

    subjects = cursor.fetchall()

    for subject in subjects:
        print(f"{subject[0]}. {subject[1]}")
    
    chosenSubject = int(input('Wpisz numer odpowiadający danemu przedmiotowi: '))

    cursor.execute('SELECT Student.imie, Student.nazwisko FROM Ocena JOIN Student ON Ocena.nr_indeksu = Student.nr_indeksu WHERE ocena >= 4 AND id_przedmiotu = ?', (chosenSubject,))

    students = cursor.fetchall()

    for student in students:
        print("Imię:", student[0])
        print("Nazwisko:", student[1])
        print("--------------------")

    

    cursor.close()
    conn.close()

def showTeachers():

    conn = sqlite3.connect('academy_database.db')

    cursor = conn.cursor()

    cursor.execute('SELECT Wykladowca.id_wykladowcy, Wykladowca.imie, Wykladowca.nazwisko, Przedmiot.nazwa_przedmiotu FROM Wykladowca JOIN Przedmiot ON Wykladowca.id_wykladowcy = Przedmiot.id_wykladowcy ORDER BY Wykladowca.id_wykladowcy')

    teachers = cursor.fetchall()

    print('\n')

    for teacher in teachers:
        print(f'{teacher[0]}. {teacher[1]} {teacher[2]} --- {teacher[3]}')

    print('\n')

    cursor.close()
    conn.close()

def showDepartment():

    conn = sqlite3.connect('academy_database.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Wydzial')

    departments = cursor.fetchall()

    for department in departments:
        print(f"{department[0]}. {department[1]}")    
    
    chosenDepartment = int(input('Wpisz numer odpowiadający danemu wydziałowi: '))

    cursor.execute('SELECT * FROM Grupa_Studencka WHERE id_wydzialu = ?', (chosenDepartment,))

    groups = cursor.fetchall()

    print('\n')
    for group in groups:
        print(f"-- {group[1]}")
    print('\n')

    cursor.close()
    conn.close()

def showStudentsGrades():

    conn = sqlite3.connect('academy_database.db')

    cursor = conn.cursor()

    cursor.execute('SELECT Student.imie, Student.nazwisko, AVG(Ocena.ocena) AS srednia_ocena FROM Student JOIN Ocena ON Student.nr_indeksu = Ocena.nr_indeksu GROUP BY Ocena.nr_indeksu')

    students = cursor.fetchall()

    print('\n')
    for student in students:
        print(f"-- {student[0]} {student[1]} -- srednia ocen: {student[2]}")
    print('\n')

    cursor.close()
    conn.close()


if __name__ == '__main__':

    if not (os.path.exists('./academy_database.db')):
        createDatabase()

    czypetla = True
    
    while (czypetla):
        print('1. Wyswietl wszystkich studentow')
        print('2. Wyświetl wszystkich studentów danej grupy')
        print('3. Wyświetl wszystkich studentów mających conajmniej 4 z danego przedmiotu')
        print('4. Wszystkich wykładowców i przedmiot który prowadzą')
        print('5. Wyświetl wydział ze wszystkimi jego grupami studenckimi')
        print('6. Wyświetl studentów z ich średnią ocen')
        print('7. Zakończ program')

        coWyswietlic = int(input('Wpisz numer odpowiadajacy temu co chcesz wyswietlic: '))

        match coWyswietlic:
            case 1:
                showAllStudents()
            case 2: 
                print('Którą grupę chcesz wyświetlić?')
                print('1. 215IC?')
                print('2. 202DE?')
                grupa = int(input('Wpisz odpowiednią cyfrę: '))
                showAllStudentsFromGroup(grupa)
            case 3:
                showStudentsWithGradeAbove4()

            case 4:
                showTeachers()

            case 5:
                showDepartment()

            case 6:
                showStudentsGrades()

            case 7:
                czypetla = False

    



