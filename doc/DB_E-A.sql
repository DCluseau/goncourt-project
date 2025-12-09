CREATE TABLE person(
   id INT,
   firstname VARCHAR(50),
   lastname VARCHAR(50) NOT NULL,
   PRIMARY KEY(id)
);

CREATE TABLE author(
   id INT NOT NULL AUTO_INCREMENT,
   biography VARCHAR(250),
   id_person INT NOT NULL,
   PRIMARY KEY(id),
   FOREIGN KEY(id_person) REFERENCES person(id)
);

CREATE TABLE publisher(
   id INT NOT NULL AUTO_INCREMENT,
   name VARCHAR(50) NOT NULL,
   PRIMARY KEY(id),
   UNIQUE(name)
);

CREATE TABLE book(
   isbn INT,
   title VARCHAR(100) NOT NULL,
   summary VARCHAR(250),
   publication_date DATE,
   number_of_pages INT,
   publisher_price DECIMAL(4,2) NOT NULL,
   prize BOOLEAN,
   id_author INT NOT NULL,
   id_publisher INT NOT NULL,
   PRIMARY KEY(isbn),
   FOREIGN KEY(id_author) REFERENCES author(id),
   FOREIGN KEY(id_publisher) REFERENCES publisher(id)
);

CREATE TABLE selection(
   id INT NOT NULL AUTO_INCREMENT,
   round INT NOT NULL,
   year_selection YEAR NOT NULL,
   PRIMARY KEY(id)
);

CREATE TABLE is_selected(
   isbn INT,
   id_selection INT,
   PRIMARY KEY(isbn, id_selection),
   FOREIGN KEY(isbn) REFERENCES book(isbn),
   FOREIGN KEY(id_selection) REFERENCES selection(id)
);

CREATE TABLE is_jury_member(
   id_person INT,
   id_selection INT,
   presiding BOOLEAN NOT NULL,
   PRIMARY KEY(id_person, id_selection),
   FOREIGN KEY(id_person) REFERENCES person(id),
   FOREIGN KEY(id_selection) REFERENCES selection(id)
);

CREATE TABLE is_character(
   id_person INT,
   isbn INT,
   PRIMARY KEY(id_person, isbn),
   FOREIGN KEY(id_person) REFERENCES person(id),
   FOREIGN KEY(isbn) REFERENCES book(isbn)
);
