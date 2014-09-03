# The Blog App - Iteration 2 (Associations)

To make our models in Rails fully functional we need to add **associations**.
Each post needs to know the list of comments associated with it, and each
comment needs to know which post it belongs to.

The `ActiveRecord` module contains a set of class methods for tying
objects together through foreign keys.

| Relationship | Model with no foreign key | Model with foreign key |
| :------------- | :------------- | :------------- |
| one-to-one | has_one | belongs_to |
| many-to-one | has_many | belongs_to |
| many-to-many | has_and_belongs_to_many | * |

\* The foreign key for each model are stored in a join table.

### Code example:

##### Post class:

```ruby
class Post < ActiveRecord::Base
  has_many :comments
end
```

##### Comment class:

```ruby
class Comment < ActiveRecord::Base
  belongs_to :post
end
```

To delete all the comments that are dependent of a post, we can use the
`dependent: :destroy` on the **association**.

```ruby
class Comment < ActiveRecord::Base
  belongs_to :post, dependent: :destroy
end
```
