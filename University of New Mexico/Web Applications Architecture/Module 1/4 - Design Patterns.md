# Design Patterns

Developing, maintaining and extending a complex web application is extremely
difficult. But, building it using a foundation of solid design principles
can simplify each of these tasks.
Design patterns provide useful design abstractions of object-oriented systems.

## What is a Design Pattern?

Is a description of interacting objects and classes that interact to solve a
general design problem within a particular context.

- Is an abstract template that can be applied over and over again.
- Apply abstract design to solve specific problems
- We can use numerous design patterns that will help to organize
  how pieces are placed within the client-server architecture.

### The n-tier architecture:
- Is a useful design pattern that maps to the client-server model
- Based on the concept of breaking system into different pieces or tiers that
  can be physically separated.

##### Advantages:
- The abstraction provides a means of managing the complexity of the design.
- Tiers can be upgraded or replaced independently as technology. The new Tier
  just needs to use the same interfaces as the old one.
- Its a balance between innovation and standardization
- Much easier to build, maintain, scale and upgrade.

### The 3-Tier Architecture:
1.  Presentation Tier - The user interface
2.  Application Tier (logic) - Retrieves, modifies and delete data.
3.  Data Tier - The source of data associated with the application

A modern web application is often depoloyed over the Internet as a 3-tier
architecture:
1. Presentation Tier - Browser
2. Application Tier (logic) - The web server
3. Data Tier- The database

The **Application** Tier is subdivided into two tiers:
- Business Logic
- Data Access

The **Presentation** Tier can also be subdivided into to tiers:
- Client - User interface components
- Presentation Logic - Server-side scripts for generations web pages.
