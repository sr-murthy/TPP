#TO-DOS

Planned/in-progress/pending actions will be listed and described here, with a rough estimate of times.

   1. **Developing a high-level architecture for the application**.  ~~*To be finished by Jan. 30, 2015*.~~  DONE, 10/02/2015

   2. **Setting up the Django app development environment on the development machine**.  This involves creating the Django project and app, checking project settings, creating the database (SQLite (v. 3.8.7.4)), running the initial migrations for the utility apps.  ~~*To be finished by Jan. 30, 2015*.~~  DONE, 10/02/2015

   3. **Writing Python and GAP scripts for data extraction**.  The data has two sources: (1) the [static HTML tables](http://www2.informatik.uni-halle.de/da/hedtke/tpp/) which contain data about maximal-by-size subgroup TPP triples for *almost* all groups in the GAP Small Groups Library of order up to 1000, with some important [exceptions](http://www2.informatik.uni-halle.de/da/hedtke/tpp/README.txt) and (2) the small groups of order up to 1000 contained in the [GAP small groups library (SGL)](http://www.icm.tu-bs.de/ag_algebra/software/small/).

   The Python script will be actually be a parser class that ~~will~~ has methods to extract data from the HTML tables, which are stored as static local web pages (in the project's assets directory), and write JSON files (to the static subdirectory inside the app folder) that represent small groups as JSON objects (mapping to Python dicts).  The JSON objects conform to a JSON schema which is hard-coded as a dictionary inside the parser.  The parser also has methods to read from the JSON files and load the data into ordered dictionary objects that can be reused on demand.  Flexibility in writing the JSON files is provided by methods which can write the JSON files for groups whose orders are in a specified list of orders or whose GAP IDs are in a specified list of GAP IDs.  The parser relies on utility classes that contain numeric information about the number of GAP small groups in the SGL and the IDs of those small groups which are excluded from the subgroup TPP search scope.

   The GAP script is a set of GAP functions that will, to some extent, be analogous to the methods of the Python parser class - it will be able to write GAP small groups as JSON objects containing various properties such as the GAP ID, order, generator list, character degrees list, whether the group is abelian, cyclic etc.  These properties conform to the same JSON schema as the data read and written by the Python parser.  Additional flexibility in writing the files is provided by the functions being able to write GAP small groups whose orders are in a specified list of orders or whose GAP IDs are in a specified list of GAP IDs.  *To be finished by ~~Mar. 1, 2015~~.*  DONE, 01/03/2015

   4. **Extracting all the small groups data from the static HTML files and writing complete JSON for all GAP small groups in the subgroup TPP search project scope**.  This has been completed for all GAP small groups in the subgroup TPP search project scope except for groups of order 256.  ~~*To be finished by Mar. 15, 2015*.~~  DONE, 10/03/2015

   5. **Designing and implementing app database schema**.  This will describe and implement the schema for the core tables of the database, of which there will be at least ~~three~~ one initially, namely  `TPP_App_smallgroup` which stores essential group-theoretic information about GAP small groups including the subgroup TPP capacity (Beta_0), the parameter type of a maximum-by-size (MBS) subgroup TPP triple, and its D3 (sum of cubes of character degrees).  The project database system is SQLite3 and changes to the schema and data in the database will be effected via the `makemigration` and `migrate` tools provided by Django.  ~~*To be finished by Mar. 21, 2015*.~~ DONE, 25/02/2015

   6. **Writing custom Django scripts for populating the database**.  This will be done as a data migration using the Django `Migration` class.  It involves writing a custom method for populating the `small_groups` db table with the data contained in the JSON files, listing the method as an operation in a data migration class that calls the `RunPython` tool, and then running the migration using `python manage.py migrate`.  ~~*To be finished by Apr. 1, 2015*.~~ DONE, 26/03/2015

   7. **Setting up the admin users and site**.  *To be finished by Oct. 15, 2015*.

   8. **Designing and implementing views**.  *To be finished by Nov. 1, 2015*.
