# Active Record Design Pattern

Named by Martin Fowler in 2003 in his book *Patterns of Enterprise Application
Architecture*. Are commonly used in **Ruby** as a means of persisting data.
More specifically, this pattern is used to access data stored in relation
databases. It allows you to perform CRUD operations without worrying about
the database technology.

#### The solution for Object Oriented and SQL
Relational databases are incompatible with an OO language. So, this design
encapsulates that notion as an object-relational mapping (ORM) and constructs
the tables based on your classes and objects. This creates a "virtual object
database" that can be used from within an OO language.

### ORM: How It's Done

OO Language | Relational Database
------------ | -------------
Classes | Tables
Objects | Record
Attributes | Columns

## Active Records in Ruby
Is provided in a module called <code>ActiveRecord</code> and the features are:
- Establish a connection to a database
- Create database tables
- Specify associations between tables and Ruby classes
- Establish an ORM between Ruby classes, objects and attributes to tables,
  rows and columns in the underlying database
- Perform CRUD operations on a <code>ActiveRecord</code> object

## Active Records in Rails
- The <code>ActiveRecord::Base.establish_connection</code> method uses the
  information in `./config/database.yml` to connect a Rails application to a
  database
- The <code>ActiveRecord::Migration</code> object is used to incrementally evolve
  the database over time
- The <code>ActiveRecord::Schema.define</code> method, in `./db/schema.rb` is
  created by inspecting the database and then expressing its structure
  programmatically using a portable DSL

### The Interactive Ruby Shell
- For interactive Ruby shell, type <code>$ irb</code>
- For Rails console, type <code>$ rails console</code> from the root of a Rails
  application directory
