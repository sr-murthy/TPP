#TO-DOS

Planned/in-progress/pending actions will be listed and described here, with a rough estimate of times.

   1. **Developing a high-level architecture for the application**.  ~~*To be finished by Jan. 30, 2015*.~~  DONE, 10/02/2015

   2. **Setting up the Django app development environment on the development machine**.  This involves creating the Django project and app, checking project settings, creating the database (SQLite (v. 3.8.7.4)), running the initial migrations for the utility apps.  ~~*To be finished by Jan. 30, 2015*.~~  DONE, 10/02/2015

   3. **~~Writing Python~~ and GAP scripts for data extraction**.  The data has two sources: (1) the [HTML tables](http://www2.informatik.uni-halle.de/da/hedtke/tpp/) which contain data about maximal-by-size subgroup TPP triples for *almost* all groups in the GAP Small Groups Library of order up to 1000, with some important [exceptions](http://www2.informatik.uni-halle.de/da/hedtke/tpp/README.txt) and (2) the small groups of order up to 1000 contained in the [GAP small groups library (SGL)](http://www.icm.tu-bs.de/ag_algebra/software/small/).  The Python scripts ~~will~~ extract data from the HTML tables, which are stored as static local web pages, and write JSON files that represent small groups as JSON objects (mapping to Python dicts).  The JSON object data needs to be updated with additional information from GAP.  *To be finished by Mar. 1, 2015.*

   4. **Designing the app database schema**:- this will specify the schema for the core tables, of which there will be at least three initially - `groups`, `subgroup_tpp_triples` and `mbs_tpp_stats` - and the table relationships, views, indexes and stored procedures.  *To be finished by Mar. 21, 2015*.

