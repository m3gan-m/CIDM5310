show databases;
select database();
create database if not exists CIDM5310project;
use CIDM5310project;

create table HADSdata(
    AHS_Control_Number text,
    Age int,
    Area_Med_Income int,
    FMR int,
    Poverty_Income int,
    BEDRMS int,
    BUILT int,
    Market_value int,
    HH_QTY int,
    HH_Income int,
    Monthly_Hsg int,
    Monthly_Utility decimal(12,7),
    Total_Wage int,
    FMTStructureTYpe varchar(255),
    FMTOwnRent varchar(255),
    FMTAssisted varchar(255)
);

/*load CSV file*/
LOAD DATA INFILE './thadsyear2013_dataset.csv' 
INTO TABLE HADSdata 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

/*Pull Min and Max Age where FMTOwnRent is Owner and then where FMTOwnRent is Renter*/
select min(Age) from HADSdata where FMTOwnRent='1 Owner';
select max(Age) from HADSdata where FMTOwnRent='1 Owner';
select min(Age) from HADSdata where FMTOwnRent='2 Renter';
select max(Age) from HADSdata where FMTOwnRent='2 Renter';

/*Answers
-9
93
-9
93
*/

/*Pull average age for own vs rent*/
select avg(Age) from HADSdata where FMTOwnRent='1 Owner';
select avg(Age) from HADSdata where FMTOwnRent='2 Renter';

/*Answers
53.8071
38.0645
*/

/*Pull average income for own where Household Quantity is 1 individual,
then for 2 representing couples and finally any number larger than 2*/
select avg(HH_Income) from HADSdata where HH_QTY=1;
select avg(HH_Income) from HADSdata where HH_QTY=2;
select avg(HH_Income) from HADSdata where HH_QTY>2;

/*Answers
37472.4839
74436.3293
86155.7859
*/

/*repull average looking only at Owners*/

select avg(HH_Income) from HADSdata where HH_QTY=1 and FMTOwnRent='1 Owner';
select avg(HH_Income) from HADSdata where HH_QTY=2 and FMTOwnRent='1 Owner';
select avg(HH_Income) from HADSdata where HH_QTY>2 and FMTOwnRent='1 Owner';

/*Answers
42706.5486
84447.8607
104393.2354
*/

/*Pull year house built and compare to Own vs Rent*/
select avg(built) from HADSdata where FMTOwnRent='1 Owner';
select avg(built) from HADSdata where FMTOwnRent='2 Renter';

/*Answers
1966.1451
1962.3173
*/
