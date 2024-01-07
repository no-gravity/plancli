# plancli
File based project planning on the command line

Every project I work on has a plan/ directory in which
I do the whole project management.

I started this simply in vim by creating files like
productchart/plan/1000-tests_for_the_comparison_pages.txt
to create a task to write "Tests for the comparison pages"
of the [Product Chart](https://www.productchart.com) project.

The 1000 is the priority of the task.

It makes handling tasks nicely easy, as I have the project
directory open in vim anyhow. So when I open the plan/
dir, I see a sorted list of tasks. I can search like
in every other vim buffer. I can look into a task like into
each other file. I can edit them right away in vim too. And
I can fire off terminal commands like grep to search inside
the tasks etc. Also versioning is handled automatically
as the project is in git anyhow.

Over time, I wrote a bunch of python scripts to make
handling the tasks easier. I might publish them here
over time. For now, here is the script which creates
a new task.

License: GNU General Public License, version 2
