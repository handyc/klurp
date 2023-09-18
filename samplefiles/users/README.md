these files are part of an automated library system for use with or without the klurp engine

they are inherited from an earlier collaborative project for dictionary searches and ended up not being used in that project

The basic idea is that librarian, archivist and webhost are created as separate automated Unix users with limited permissions on
the system, and time-based tasks using cron. Separating the users allows for increased security, as each automated user only
has access to its own tasks. This type of setup also has the added benefit of forcing the individual components to be organized
easily.

More detailed examples are to be added here soon.
