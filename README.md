# mage2-behave

## Introduction

**mage2-behave** is a project that leverages Python for Behavior-Driven Development (BDD) development in Magento 2 projects. The project uses various Python packages to achieve its objectives, with some of the notable ones being `selenium`, `behave`, `splinter`, `stere`,`maria-db`, `docker` and `webdriver-manager` among others.

This project endeavors to create Magento2/Adobe Commerce projects that are robust, maintainable, and solves real-world problems effectively. Key concepts of software development, such as object-oriented design and clean code, are embraced fully.

The project also exposes you to libraries and frameworks commonly used in Python ecosystem, thereby giving you practical exposure that goes beyond theoretical knowledge.

Whether you're a seasoned developer or an individual in the earlier stages of the Python learning curve, contributing to this project offers a tremendous opportunity to learn, grow and make a difference. 

To get started, make sure you've Python 3.8 or greater installed on your machine alongside the necessary Python packages listed in the requirements file.


## Benefits of Using BDD in a Magento 2 Project

Behavior-Driven Development (BDD) is a powerful approach that aligns software development with business expectations. Utilizing BDD in a Magento 2 project using Python brings numerous benefits:

1. **Communication Enhancement:** BDD enhances communication between developers, stakeholders, and non-technical or business participants. It allows everyone to have a clear understanding of the project requirements.

2. **Focus on the End User:** BDD encourages the team to focus on the end user’s perspective, ensuring that the development process centers around the delivery of features that provide real value to users.

3. **Reduced Ambiguity:** BDD scenarios provide a clear agreement on what is to be delivered, reducing ambiguities and rework.

4. **Regression Detection:** BDD aligns with Test-Driven Development (TDD) to ensure that all code is covered by tests. This early detection of bugs reduces the cost and time involved in fixing them.

5. **Integration with Agile and Continuous Delivery:** BDD is ideal for Agile development and complements continuous integration and delivery, thereby accelerating product releases and ensuring robust quality.

In essence, utilizing BDD in a Magento 2 project using Python facilitates effective communication, ensures optimal focus on delivering user value, enhances requirement clarity, aids in early bug detection, and promotes seamless integration with Agile and continuous delivery practices.

## Why using Python Instead of PHP for BDD in Magento 2?

While PHP has served as a strong language for web development over the years, Python offers certain advantages that make it a preferred choice for projects like mage2-behave. Here's why:

1. **Readability and Syntax:** Python follows a strict indentation enforcement, which leads to clear, readable code. Its syntax is designed to be easy to understand and use.

2. **Extensive Libraries:** Python is known for its vast selection of libraries, many of which simplify tasks that would be more complex in PHP, e.g. setting up the environment for BDD development.

3. **Strong Community**: Python has a vibrant community that contributes to a rich ecosystem of libraries and frameworks. This means you are likely to find help or an existing solution to your problem faster than in PHP.

4. **Irrespective of the PHP version utilized by Magento 2**: Tests written in Python will be easily more portable to other Magento 2 projects without the need to refactor code due to a different PHP version used by Magento 2.

Remember, the decision between Python and PHP depends on the requirements of the project, and each has its strengths. However, for mage2-behave, Python's strengths align more closely with the project's goals and needs.

## Behavior-Driven Development (BDD) Life Cycle

Behavior-Driven Development (BDD) follows a set of practices that encourage collaboration between developers, QA and non-technical business participants in a software project.

The BDD process can be outlined in the following steps:

1. **Requirements Identification:** Business Analysts, Product owners or subject-matter experts collaborate with the technical team to identify and comprehend the requirements.

2. **Defining Acceptance Criteria:** Each identified requirement is then elaborated in detail. The team defines the expected behavior of the system. This step is a crucial component of BDD as it ensures that everyone within the team has a clear understanding of the feature and what is considered to be its correct behavior.

3. **Automated Test Case Generation:** Using the established acceptance criteria, BDD practitioners use a domain-specific language (DSL) to create readable and understandable test cases. Languages like Gherkin are often used due to their ability to create structured yet easy-to-understand test cases.

4. **Test Case Review:** The test cases are reviewed by the whole team, including developers, test engineers, business analysts, and stakeholders. The goal of this stage is to ensure that the team understands the behavior of the system.

5. **Test Execution:** The test cases are executed and the system behavior is validated against expected results.

6. **Coding:** Developers begin coding the solution, following the agreed upon acceptance criteria.

7. **Refactoring:** The code is continuously refactored for improvements while maintaining its behavior.

8. **Feedback and Maintenance:** Test results provide immediate feedback, allowing teams to address issues. This feedback loop is inherent to the BDD process. Maintenance and further development cycles can then follow.

By defining behavior in terms of user stories and plain-language test cases, BDD ensures that all team members understand and contribute to the product’s development.

## Writing Feature Files in Gherkin

Gherkin provides a structured way to write software behavior scenarios in a human-readable language. Here's an approach to writing effective feature files in Gherkin:

### 1. Feature
Start by defining the feature. This provides an overview of the functionality that you'll be defining in the scenarios. It's a brief explanation of the feature in the system.

Example:

~~~gherkin
Feature: Login functionality for a social networking site
~~~

#### 1.1  Using ```As a... I want ... So That``` 

Example:

~~~gherkin
Feature: Login functionality for a social networking site
  As a user,
  I want to be able to log in,
  So That I can access member-only content
~~~

### 2. User Story:
Link the feature to a user story to provide context. This is usually a short statement from the user's perspective, describing some piece of functionality.

### 3. Scenarios:
Scenarios are the core of the feature. Each scenario should represent one flow of the feature. Start with the keyword "Scenario", followed by a short description.

Example:

~~~gherkin
Scenario: Successful login of the user
~~~

#### 3.1 ```Given```:
This step is used to set up the test case's scenario. This could involve setting certain conditions or preparing data.

Example:

~~~gherkin
Given the user is on the Login Page
~~~

#### 3.2 ```When```:
This step is used to describe an action - it's often where the user interaction happens.

Example:

~~~gherkin
When the user enters valid credentials
~~~

#### 3.3 ```Then```:
This step is used to describe the outcome or result of the "When" step.

Example:

~~~gherkin
Then the user should be able to successfully login
~~~

#### 3.4 ```And``` & ```But```:

Example:

~~~gherkin
 Scenario: Validating login fields
  Given I am on the login page
  When I fill in the username field
  And I leave the password field empty
  Then I should see a message that the password is required
  But I should not be logged in
~~~

### Scenario Outline:

Scenario Outlines in Gherkin allow us to more concisely express these scenarios through the use of placeholders, which are filled with the values from an Examples table.

Here's an example of a scenario outline:

~~~gherkin
Scenario Outline: Testing login with multiple sets of data
  Given the user is on the Login Page
  When the user enters Username "<username>" and Password "<password>"
  Then "<outcome>" should be displayed

  Examples:
  | username | password | outcome                      |
  | John     | secret   | Login Successful             |
  | Invalid  | secret   | Login Failed. Invalid username |
~~~

In the `Scenario Outline`, `<username>`, `<password>`, and `<outcome>` are variables. For each row in the `Examples` table, these variables are substituted, and the scenario is executed.

### Background in Gherkin:

The `Background` keyword in Gherkin is used to group several `Given` steps that are common to all the scenarios in the feature file. It helps to reduce the duplication of the `Given` steps.

Here's an example:

~~~gherkin
Feature: Blog
  Background: 
    Given I am logged in as a Writer
    And I am on the create article page
  
  Scenario: Successful article creation
    When I fill in the title field
    And I fill in the body field
    And I submit the form
    Then I should see that the article was successfully created

  Scenario: Unsuccessful article creation with blank fields
    When I leave the title field blank
    And I leave the body field blank
    And I submit the form
    Then I should see error messages about the blank fields
~~~

In the example above, the `Background` comprises steps that apply to all scenarios in the feature. This helps to keep your feature file DRY (Don't Repeat Yourself).

## Testing Overview 

During the execution of behave, it is vital to ensure that the integrity of an environment data remains uncompromised. For this, we have put in place a system wherein the tests are performed on a separate, duplicate database. 

### Protecting Original Database 

`mage2-behave` is configured to protect the data integrity of the original database. Prior to the execution of tests, a copy of the environment main Magento 2 database is made, and all tests interact exclusively with this copy. This practice ensures that our main database stays unaltered, and no unexpected data manipulation occurs.

By executing tests on a copy of the database, we ensure both the reliability of our tests and the safety of our data. During testing, the modified database configuration (pointing to the test database) is active, ensuring all database interactions occur on the separate testing database, not on the main one.

This method ensures that environment database remains guarded against unintended alterations while testing, providing us with a safe and effective testing approach.

During development, it might not be ideal to generate a test DB at each `behave` run. To skip dropping the db, thus reusing the test DB already generated simply run the `behave` command with the `-D keep-test-db=true` option:

```shell
behave -D keep-test-db=true ... [OTHER OPTIONS]
```

#### Keep in mind that if you do this, you may have to revert changes in the test DB to avoid failure of some tests that expects certain data.
#### You can achieve this via `fixtures`.

#### IMPORTANT:
By default `mage2-behave` performs duplication of database and configuration in Magento 2 only in development environment.
If it is required to integrate behave in CI/CD pipelines, it is beyond the scope of this project due to the multitude of possible environments to consider, and will be needed to integrate tear-up and tear-down of the database as well as the configuration in behave `before_all` and `after_all` environment hooks.
You can however take as a good starting point what has been done for a development environment in this project.

## Setting Up a Virtual Python Environment for the mage2-behave Project

1. **Installing the `virtualenv` package**

    Before we begin, ensure that you have the `virtualenv` package installed. If not, you can install it using pip:

    ```bash
    pip install virtualenv
    ```

2. **Creating a Virtual Environment**

    Firstly clone the `mage2-behave` project in the root of your Magento 2 installation.

    ```bash
    git clone https://github.com/ctasca/mage2-behave.git 
   ```
   
    Navigate to the project directory where you want to set up the virtual environment and run:

    ```bash
    cd <magento_root>/mage2-behave
    virtualenv venv   # "venv" can be replaced with your preferred name
    ```

    This will create a new virtual environment in the `mage2-behave` project directory.

3. **Activating the Virtual Environment**

    Activate the virtual environment using one of the following commands based on your operating system:

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

    - On Windows:

        ```bash
        .\\venv\Scripts\activate
        ```

    You should now see the virtual environment name in the terminal prompt. This indicates that the virtual environment is active.

4. **Install Necessary Dependencies**

    With the virtual environment activated, install the necessary dependencies for `mage2-behave` project as defined in the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

5. **Running the Project**

    You are now ready to run the project. Always ensure that the virtual environment is activated (i.e., you can see its name in terminal) whenever you are running or making changes to the project.

6. **Deactivate the Virtual Environment**

    Once you're done, you can deactivate the virtual environment:

    ```bash
    deactivate
    ```

    This command will bring back the system’s default Python interpreter. 

---

This setup ensures that the various Magento 2/mage2-behave projects on your system are isolated from each other, each with their own set of dependencies, thus eliminating any potential conflicts.

## Integrating the 'mage2-behave' Project with Magento 2 Repository or Separately

When integrating the 'mage2-behave' project into the Magento 2 repository or when migrating it to a separate repository altogether, it is important to remove the `.git` directory in the 'mage2-behave' project. Here's why:

The `.git` directory contains all the important metadata for a project under Git version control. This includes information about commits, remote repository addresses, etc.

If you attempt to migrate the project without removing the `.git` directory, there can be several complications:

1. **Commit History Confusions:** The commit history of the 'mage2-behave' project will be retained and can conflict with the commit history of the Magento 2 repository or the new repository. This might lead to confusion in understanding the evolution and progression of the project.
2. **Configuration Clashes:** The `.git` directory also holds the configuration details for the 'mage2-behave' repository. These details might conflict with the settings of the Magento 2 or new repository causing integration issues.
3. **Nested Git Repository:** If the Magento 2 repository is itself a Git repository, including the `.git` directory creates a nested repository situation. This situation is generally complex to manage and can cause several operational issues.

So, before integrating 'mage2-behave' with the Magento 2 repository or moving it to a new Git repository, make sure to delete the `.git` directory from 'mage2-behave'. This will result in a smoother and more streamlined project integration process.

To do so, simple navigate to the `mage2-behave` directory in the root of your Magento 2 project and run the following command:

```bash
python3 remove_git.py
```
## Note on Python Command Usage Across Different Operating Systems

In various operating systems, the command-line interface command to invoke Python can differ. Some systems use `python`, while others use `python3`. The discrepancy mainly comes from the fact that different systems may still have Python 2.x versions installed and set 'python' command to point to that version.

Here's a general guideline to follow:

- **Windows / Linux**: If both Python 2.x and Python 3.x versions are installed, `python` likely refers to Python 2.x version and `python3` to Python 3.x version. If only Python 3.x is installed then `python` should invoke the Python 3.x version.
- **MacOS**: Modern macOS versions come pre-installed with Python 2.x and 'python' command refers to that version. Users need to install Python 3.x separately which can be invoked with `python3` command. 

A good way to check your Python version and to validate the command is by typing `python --version` or `python3 --version` in your terminal. It should return the Python version that the command points to.

To ensure compatibility across multiple systems, it is recommended to use `python3` in all the commands and scripts for this project. Also, consider using [virtual environments](https://docs.python.org/3/library/venv.html) to isolate your Python environment per project.

## The `generate_config.py` Script 

The `generate_config.py` script is a vital part of our package. This script helps to generate configuration files required for the project.

It will firstly create the required `.ini` files within the `core_config` directory, copying first the `.ini.template` files and on the second execution prompt you to enter the values for the different sections of the `.ini` files, for example the Magento 2 development environment `baseurl` and `secure baseurl` as well as other parameters.

This script is intuitive in understanding if a section has already parameters with values or not, and will not prompt you to edit parameters with already values associated with them.

The following sections are set already in the mage2-behave package:

1. `[Development]`

2. `[Integration]`

3. `[Test]`

4. `[Staging]`

5. `[PreProduction]`

6. `[Production]`

7. `[DummyCustomer]`

8. `[Api]`

9. `[Docker]`

Note that for development purposes, you could simply just define the [Development] section in the `.ini` files generated by the `generate_config.py` script (Read the following section of this README about this)

Here is an example:

```ini
[Development]
development_admin_username = admin
development_admin_firstname = Test
development_admin_lastname = Test
development_admin_email = test@example.com
development_backend_url = backend/
development_env_baseurl = https://example.test/
development_env_secure_baseurl = https://example.test/
```

**Important:** `.ini` files and the `.env` (used only for passwords) should never be committed in a repository, they are already excluded in the `.gitignore` file of the repo. You may have to set them in your own repository `.gitignore`

### About the `.env` file

This file is located in the root of the 'mage2-behave' project and is where sensitive data should be stored.
They are retrieved in `behave steps` when needed via the `python-decouple` package, so for security, you won't find them in the core_config `.ini` files.

### Running the `generate_config.py` Script

To run this script, follow these steps:

1. Open a terminal.

2. Navigate to the directory where the `generate_config.py` script is located:

    ```sh
    cd <magento_root>/mage2-behave
    ```

3. Execute the script using Python or Python3 (based on your OS):

    ```sh
    python generate_config.py
    ```

    or

    ```sh
    python3 generate_config.py
    ```

Please ensure that you are in the 'mage2-behave' directory where the script is located before running the command.

### Running the `sensitive_data_config.py` Script

To run this script, follow these steps:

1. Open a terminal.

2. Navigate to the directory where the `sensitive_data_config.py` script is located:

    ```sh
    cd <magento_root>/mage2-behave
    ```

3. Execute the script using Python or Python3 (based on your OS):

    ```sh
    python sensitive_data_config.py
    ```

    or

    ```sh
    python3 sensitive_data_config.py
    ```

Please ensure that you are in the 'mage2-behave' directory where the script is located before running the command.

## Docker Magento Function Usage

### `docker_bin_magento()`

This project provides a utility function: `docker_bin_magento()`, for running Magento CLI commands from a Docker container in a development environment.

This function is defined in the `utils/docker_env.py` module and takes as input a string specifying the Magento CLI command to be run inside the Docker container that's serving as the PHP environment for the Magento application.

Here's how to use it:

```bash
docker_bin_magento('cache:clean')
```

In the example above, `cache:clean` is the Magento CLI command that we want to run. This command will clean the Magento cache.

This utility performs the following sequence of actions:

1. Reads the name of the PHP-FPM service from the project configuration.
2. Searches for a running Docker container that matches the PHP-FPM service name.
3. Constructs a Docker command to execute the Magento CLI command within the identified Docker container.
4. Uses `subprocess` to execute the Docker command.

Please note that it is necessary to have a Docker environment up and running for the tests to be able to interact with the Magento application.

**This function can be beneficial for writing tests that require changing the Magento state as per the test's needs.**

The function assumes that your Docker environment includes a service that provides a PHP-FPM environment suitable for running the Magento application. The name of this service is read from the project configuration (the `docker_config.ini` file).

It's important to ensure that the Docker environment is running, and the PHP-FPM service is correctly defined in your configuration before calling this function.

Here is an example of usage in `behave steps`:

```python
from behave import *
from utils import docker_env as denv


@given("I have flushed the magento cache")
def step_impl(context):
    denv.docker_bin_magento('ca:fl')
```
