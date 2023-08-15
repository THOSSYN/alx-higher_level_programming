-- Show all tables in mysql server
-- sets the db name to command line arg
SET @db_name = 'mysql';

SELECT table_name
FROM information_schema.tables
WHERE table_schema = @db_name;
