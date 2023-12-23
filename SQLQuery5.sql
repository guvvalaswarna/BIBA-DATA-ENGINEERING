USE Pet_adoption


CREATE TABLE animals(
    ID int,
	Name VARCHAR(225),
	Breed VARCHAR(225),
	Color VARCHAR(225),
	Gender VARCHAR(225),
	Status int
	);

	INSERT INTO DBO.animals VALUES(1,'PUPPY','BEAGLE','BROWN','M',0),
	                          (2,'SNOWY','HUSKY','WHITE','F',0),
							  (3,'SPOT','DALMATION','BLACK&WHITE','M',0)


	SELECT *FROM animals


	SELECT COLOR FROM animals

	DELETE FROM animals WHERE ID=2

	UPDATE animals SET Name='CRICKET' WHERE ID=3

	
	USE Pet_adoption
	

	CREATE TABLE adopted(
	  Animalid int,
	  NAME VARCHAR(225),
	  CONTACT VARCHAR(225),
	  DATES date
	  );

	  INSERT INTO DBO.adopted VALUES(1,'PRIYA','PRIYA09@GMAIL.COM', CURRENT_TIMESTAMP),
	                                (3,'SAM','SAM22@GMAIL.COM', CURRENT_TIMESTAMP)
	                           

	SELECT *FROM adopted

	  UPDATE animals set Status=1 WHERE ID=1

	  SELECT * FROM animals

	  ALTER TABLE adopted ADD city VARCHAR(30);

	  ALTER TABLE adopted ADD phoneno VARCHAR(50);

	  SELECT *FROM adopted

	  DROP TABLE adopted

	  TRUNCATE  TABLE animals

	
	  
	 