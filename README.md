# Logs Analysis Project

### About the project
>You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

>In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

### How to Run the Program

#### Requirements
  * [Python2](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)

#### Setup Project:
  1. Install Vagrant and VirtualBox, Please check [instructions to install the virtual machine](https://classroom.udacity.com/courses/ud197/lessons/3423258756/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)
  2. Download or Clone this repository in the /vagrant directory **You must finish step 1 first**.

#### Prepare the Software and Data
 1. The virtual machine from step 1

       If you need to bring the virtual machine back online with `$ vagrant up`. Then log into it with `$ vagrant ssh`
 2. Download the data from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
    1. Unzip this file after downloading it. The file inside is called newsdata.sql.
    2. To run the reporting tool, you'll need to load the site's data into your local database. To load the data, use the command
        ```
        psql -d news -f newsdata.sql
        ```
    3. The database includes three tables:
        - The `authors` table includes information about the authors of articles.
        - The `articles` table includes the articles themselves.
        - The `log` table includes one entry for each time a user has accessed the site.

#### Run the Tool :boom:
1. From the vagrant directory inside the virtual machine, run `log-analyser.py` using:
    ```
    $ python log-analyser.py
    ```
2. Check the output file for the results `logOutput.txt`

##### For more understanding please check the [PostgreSQL documentation](https://www.postgresql.org/docs/current/static/index.html)
- [The select statement](https://www.postgresql.org/docs/9.5/static/sql-select.html)
- [SQL string functions](https://www.postgresql.org/docs/9.5/static/functions-string.html)
- [Aggregate functions](https://www.postgresql.org/docs/9.5/static/functions-aggregate.html)
- [CREATE CAST](https://www.postgresql.org/docs/9.5/static/sql-createcast.html)
- [Data Type Formatting Functions](https://www.postgresql.org/docs/9.5/static/functions-formatting.html)
