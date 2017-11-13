-- Modify the CREATE TABLE statements as needed to add constraints.
-- Do not otherwise change the column names or types.

CREATE TABLE People
(id INTEGER NOT NULL PRIMARY KEY UNIQUE,
 name VARCHAR(256) NOT NULL,
 pet VARCHAR(256),
 wand_core VARCHAR(256) 
);

CREATE TABLE Teacher
(id INTEGER NOT NULL PRIMARY KEY REFERENCES People(id)
);

CREATE TABLE House
(name VARCHAR(32) NOT NULL PRIMARY KEY UNIQUE,
 teacher_id INTEGER NOT NULL REFERENCES Teacher(id)
);

CREATE TABLE Student
(id INTEGER NOT NULL PRIMARY KEY REFERENCES People(id),
 year INTEGER NOT NULL,
 house_name VARCHAR(32) NOT NULL REFERENCES House(name)
);

CREATE TABLE Deed
(id SERIAL PRIMARY KEY,
 student_id INTEGER NOT NULL REFERENCES Student(id),
 datetime TIMESTAMP NOT NULL,
 points INTEGER NOT NULL,
 description VARCHAR(512) NOT NULL
    CHECK ((description LIKE 'Arriving late%' AND points <= -10) OR
      (description NOT LIKE 'Arriving late%'))
);

CREATE TABLE Subject
(name VARCHAR(256) NOT NULL PRIMARY KEY UNIQUE
);

CREATE TABLE Offering
(subject_name VARCHAR(256) NOT NULL 
  REFERENCES Subject(name),
 year INTEGER NOT NULL ,
 teacher_id INTEGER NOT NULL
 REFERENCES Teacher(id),
UNIQUE(teacher_id, subject_name,year),
PRIMARY KEY (subject_name, year)
);

CREATE TABLE Grade

(student_id INTEGER NOT NULL REFERENCES Student(id),

 subject_name VARCHAR(256) NOT NULL,
 year INTEGER NOT NULL,
FOREIGN KEY (subject_name, year) REFERENCES Offering(subject_name, year),

 grade CHAR(1)
 CHECK (grade = 'O' OR grade = 'E' OR grade = 'A' OR grade = 'P' OR grade = 'D' OR grade = 'T' OR grade IS NULL),

 PRIMARY KEY (student_id, subject_name, year)

);

CREATE TABLE FavoriteSubject
(student_id INTEGER NOT NULL 
    REFERENCES Student(id),
 subject_name VARCHAR(256) NOT NULL 
    REFERENCES Subject(name),
  PRIMARY KEY (student_id, subject_name)
);

-- (e) Using a trigger, enforce that if a student ever receives a D or
-- T for a subject, the student cannot take the same subject
-- again. (Otherwise students may repeat a subject.)

CREATE FUNCTION TF_DTGrades() RETURNS TRIGGER AS $$
BEGIN
  -- YOUR IMPLEMENTATION GOES HERE
  -- IF ((OLD.grade ='D' or OLD.grade = 'T') AND (OLD.student_id = NEW.student_id) AND (OLD.subject_name = NEW.subject_name)) THEN
  --   RAISE EXCEPTION 'The student cannot take the subject again';


IF (EXISTS ( SELECT grade FROM Grade WHERE Grade.grade = 'D' OR Grade.grade = 'T' AND
    Grade.student_id = NEW.student_id AND Grade.subject_name = NEW.subject_name )) THEN   
    RAISE EXCEPTION 'The student cannot take the subject again';

  END IF;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER TG_DTGrades
  BEFORE INSERT OR UPDATE ON Grade

  FOR EACH ROW
  EXECUTE PROCEDURE TF_DTGrades();

-- (f) Using triggers, enforce that a person cannot be both student
-- and teacher at the same time.
-- YOUR IMPLEMENTATION GOES HERE
CREATE FUNCTION TF_student_notsameperson() RETURNS TRIGGER AS $$
BEGIN 

  IF ((NEW.id = Teacher.id)) THEN 
    RAISE EXCEPTION 'A person cannot be both student and teacher at the same time';
  END IF;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;
  
CREATE TRIGGER TG_student_notsameperson
  BEFORE UPDATE ON Student 
  FOR EACH ROW
  EXECUTE PROCEDURE TF_student_notsameperson();

CREATE FUNCTION TF_teacher_notsameperson() RETURNS TRIGGER AS $$
BEGIN 
  IF ((NEW.id = Student.id)) THEN 
    RAISE EXCEPTION 'A person cannot be both student and teacher at the same time';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;
  
CREATE TRIGGER TG_teacher_notsameperson
  BEFORE UPDATE ON Teacher 
  FOR EACH ROW
  EXECUTE PROCEDURE TF_teacher_notsameperson();

-- Some initial data to play with.  These INSERT statements should succeed.
-- Do NOT modify this section.
INSERT INTO People VALUES
  (0, 'Albus Dumbledore', 'Fawkes the phoenix', 'Thestral tail-hair'),
  (1, 'Minerva McGonagall', NULL, 'dragon heartstring'),
  (2, 'Pomona Sprout', NULL, NULL),
  (3, 'Filius Flitwick', NULL, NULL),
  (4, 'Severus Snape', NULL, NULL);
INSERT INTO Teacher VALUES
  (0), (1), (2), (3), (4);
INSERT INTO House VALUES
  ('Gryffindor', 1),
  ('Hufflepuff', 2),
  ('Ravenclaw', 3),
  ('Slytherin', 4);
INSERT INTO People VALUES
  (11, 'Harry Potter', 'Hedwig the owl', 'phoenix feather'),
  (12, 'Hermione Granger', 'Crookshanks the cat', 'dragon heartstring'),
  (13, 'Ron Weasley', 'Scabbers the rat', 'unicorn tail hair'),
  (21, 'Cedric Diggory', NULL, 'unicorn hair'),
  (22, 'Laura Madley', NULL, NULL),
  (31, 'Cho Chang', NULL, NULL),
  (32, 'Luna Lovegood', NULL, NULL),
  (41, 'Draco Malfoy', 'eagle owl', 'dragon heartstring'),
  (42, 'Marcus Flint', NULL, NULL);
INSERT INTO Student VALUES
  (11, 1991, 'Gryffindor'),
  (12, 1991, 'Gryffindor'),
  (13, 1991, 'Gryffindor'),
  (21, 1989, 'Hufflepuff'),
  (22, 1994, 'Hufflepuff'),
  (31, 1990, 'Ravenclaw'),
  (32, 1992, 'Ravenclaw'),
  (41, 1991, 'Slytherin'),
  (42, 1986, 'Slytherin');
INSERT INTO Deed(student_id, datetime, points, description) VALUES
  (11, '1991-09-06 10:00:00', -1, 'Cheekiness'),
  (12, '1991-10-31 13:00:00', -5, 'Claimed to have gone looking for the troll'),
  (11, '1991-10-31 18:00:00', 5, 'For saving Hermione from the troll'),
  (13, '1991-10-31 18:00:00', 5, 'For saving Hermione from the troll'),
  (41, '1992-02-22 07:00:00', -20, 'Wandering the corridors at night'),
  (12, '1992-09-02 11:30:00', 10, 'Getting full marks on Lockhart''s quiz'),
  (13, '1993-10-10 15:30:00', -50, 'For throwing a crocodile heart at Draco Malfoy');
INSERT INTO Subject VALUES
  ('Charms'),
  ('Defence against the Dark Arts'),
  ('Arithmancy'),
  ('Potions'),
  ('Transfiguration');
INSERT INTO Offering
(SELECT 'Charms', year, 3
 FROM generate_series(1986, 1998) as year);
INSERT INTO Offering VALUES('Defence against the Dark Arts', 1996, 4);
INSERT INTO Offering
(SELECT 'Potions', year, 4
 FROM generate_series(1986, 1995) as year);
INSERT INTO Offering VALUES('Transfiguration', 1955, 0);
INSERT INTO Offering
(SELECT 'Transfiguration', year, 1
 FROM generate_series(1986, 1998) as year);
INSERT INTO Grade VALUES
  (13, 'Potions', 1992, 'P'),
  (13, 'Potions', 1993, 'T'),
  (13, 'Transfiguration', 1994, 'P');
INSERT INTO FavoriteSubject VALUES
  (11, 'Defence against the Dark Arts'),
  (12, 'Arithmancy'),
  (13, 'Charms'),
  (21, 'Defence against the Dark Arts'),
  (31, 'Charms'),
  (41, 'Potions');

-- (g) Write an INSERT statement that fails because a student grade
-- record is entered for a non-existent offering.
-- YOUR IMPLEMENTATION GOES HERE
INSERT INTO Grade VALUES (13, 'Defence against the Dark Arts', 1992, 'P');

-- (h) Write an INSERT statement that fails for violating (b).
-- YOUR IMPLEMENTATION GOES HERE
INSERT INTO Offering VALUES('Charms', 1996, 4);

-- (i) Write an UPDATE statement that fails for violating (c).
-- YOUR IMPLEMENTATION GOES HERE

UPDATE Grade SET grade = 'V' WHERE student_id = 13 AND subject_name = 'Transfiguration' AND year = 1994;


-- (j) Write an INSERT statement that fail for violating (d).
-- YOUR IMPLEMENTATION GOES HERE
INSERT INTO Deed(student_id, datetime, points, description) VALUES (11, '1991-09-06 10:00:02', 2, 'Arriving late');

-- (k) Write an INSERT statement that fails for violating (e). Then
-- write another UPDATE statement that fails also for violating (e).
-- YOUR IMPLEMENTATION GOES HERE

INSERT INTO Grade VALUES (13, 'Potions', 1993, 'T');

UPDATE Grade SET subject_name = 'Potions' WHERE student_id = 13 AND subject_name = 'Transfiguration' AND year = 1994;


-- (l) Write an INSERT statement that fails for violating (f).  Then
-- write another UPDATE statement fails also for violating (f).
-- YOUR IMPLEMENTATION GOES HERE
INSERT INTO Teacher VALUES (11);

UPDATE Teacher SET id = 31 WHERE id = 3;

-- (m) Define a view that lists, for each House, the total number of
-- points accumulated by the House during the school year 1991-1992
-- (which started on September 1, 1991 and ended on June 30,
-- 1992). Note that your view should list all Houses, even if a House
-- didn’t have any points earned or deducted during this period (in
-- which case the total should be 0) or there were more points
-- deducted than earned (in which case the total should be negative).
CREATE VIEW HousePoints(house, points) AS
-- REPLACE THE FOLLOWING WITH YOUR IMPLEMENTATION


SELECT name, COALESCE (Deed.points, 0) 
FROM House LEFT OUTER JOIN Student ON House.name = Student.house_name LEFT OUTER JOIN Deed ON Deed.student_id = Student.id;
AND Deed.datetime >= '1991-09-01 00:00:00' AND Deed.datetime <= '1992-06-30 23:59:59';
-- = '1991-09%' or  Deed.datetime ='1991-10%' OR Deed.datetime  = '1991-11%' 
-- OR Deed.datetime  = '1991-12%' OR Deed.datetime  = '1992-01%' 
-- OR Deed.datetime = '1992-02%' OR Deed.datetime =  '1992-03%' OR Deed.datetime =  '1992-04%' 
-- OR Deed.datetime =  '1992-05%' OR Deed.datetime =  '1992-06%';


SELECT house, SUM(points) as points FROM HousePoints GROUP BY house;
