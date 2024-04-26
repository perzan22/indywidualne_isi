CREATE TABLE Uczelnia
(
  id_uczelni INT NOT NULL,
  nazwa_uczelni VARCHAR(40) NOT NULL,
  PRIMARY KEY (id_uczelni)
);

INSERT INTO Uczelnia (id_uczelni, nazwa_uczelni) VALUES (1, 'AMW');

CREATE TABLE Wydzial
(
  id_wydzialu INT NOT NULL,
  nazwa_wydzialu VARCHAR(40) NOT NULL,
  id_uczelni INT NOT NULL,
  PRIMARY KEY (id_wydzialu),
  FOREIGN KEY (id_uczelni) REFERENCES Uczelnia(id_uczelni)
);

INSERT INTO Wydzial (id_wydzialu, nazwa_wydzialu, id_uczelni) VALUES 
(1, 'WME', 1),
(2, 'WHiS', 1);

CREATE TABLE Grupa_Studencka
(
  id_grupy INT NOT NULL,
  nazwa_grupy VARCHAR(8) NOT NULL,
  id_wydzialu INT NOT NULL,
  PRIMARY KEY (id_grupy),
  FOREIGN KEY (id_wydzialu) REFERENCES Wydział(id_wydzialu)
);

INSERT INTO Grupa_Studencka (id_grupy, nazwa_grupy, id_wydzialu) VALUES 
(1, '215IC', 1),
(2, '202DE', 2);

CREATE TABLE Student
(
  nr_indeksu INT NOT NULL,
  imie VARCHAR(20) NOT NULL,
  nazwisko VARCHAR(30) NOT NULL,
  id_grupy INT NOT NULL,
  PRIMARY KEY (nr_indeksu),
  FOREIGN KEY (id_grupy) REFERENCES Grupa_Studencka(id_grupy)
);

INSERT INTO Student (nr_indeksu, imie, nazwisko, id_grupy) VALUES
(1, 'Olaf', 'Perzanowski', 1),
(2, 'Marek', 'Kalcki', 1),
(3, 'Bartek', 'Kot', 1),
(4, 'Miroslaw', 'Okulski', 2),
(5, 'Sylwia', 'Malinowska', 2),
(6, 'Zuzanna', 'Iksinska', 2);

CREATE TABLE Wykladowca
(
  id_wykladowcy INT NOT NULL,
  imie VARCHAR(20) NOT NULL,
  nazwisko VARCHAR(30) NOT NULL,
  PRIMARY KEY (id_wykladowcy)
);

INSERT INTO Wykladowca (id_wykladowcy, imie, nazwisko) VALUES 
(1, 'Tomasz', 'Igrekowski'),
(2, 'Mariusz', 'Michalowski'),
(3, 'Wiktor', 'Poznanski'),
(4, 'Katarzyna', 'Golubicka'),
(5, 'Marian', 'Drakar');

CREATE TABLE Przedmiot
(
  id_przedmiotu INT NOT NULL,
  nazwa_przedmiotu VARCHAR(30) NOT NULL,
  id_wykladowcy INT NOT NULL,
  PRIMARY KEY (id_przedmiotu),
  FOREIGN KEY (id_wykladowcy) REFERENCES Wykładowca(id_wykladowcy)
);

INSERT INTO Przedmiot (id_przedmiotu, nazwa_przedmiotu, id_wykladowcy) VALUES 
(1, 'Programowanie', 2),
(2, 'Jezyk angielski', 5),
(3, 'WF', 4),
(4, 'Fizyka', 1),
(5, 'Systemy komputerowe', 3);

CREATE TABLE Ocena
(
  id_oceny INT NOT NULL,
  ocena INT NOT NULL,
  nr_indeksu INT NOT NULL,
  id_przedmiotu INT NOT NULL,
  PRIMARY KEY (id_oceny),
  FOREIGN KEY (nr_indeksu) REFERENCES Student(nr_indeksu),
  FOREIGN KEY (id_przedmiotu) REFERENCES Przedmiot(id_przedmiotu)
);

INSERT INTO Ocena (id_oceny, ocena, nr_indeksu, id_przedmiotu) VALUES
(1, 3, 1, 1),
(2, 4, 1, 2),
(3, 5, 1, 3),
(4, 3, 1, 4),
(5, 4, 1, 5),
(6, 2, 2, 1),
(7, 3, 2, 2),
(8, 5, 2, 3),
(9, 4, 2, 4),
(10, 3, 2, 5),
(11, 4, 3, 1),
(12, 4, 3, 2),
(13, 4, 3, 3),
(14, 5, 3, 4),
(15, 3, 3, 5),
(16, 5, 4, 1),
(17, 3, 4, 2),
(18, 4, 4, 3),
(19, 3, 4, 4),
(20, 4, 4, 5),
(21, 5, 5, 1),
(22, 3, 5, 2),
(23, 5, 5, 3),
(24, 4, 5, 4),
(25, 3, 5, 5),
(26, 5, 6, 1),
(27, 4, 6, 2),
(28, 2, 6, 3),
(29, 4, 6, 4),
(30, 4, 6, 5);