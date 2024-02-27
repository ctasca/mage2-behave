# mage2-behave

### Introduction

**mage2-behave** is a project that leverages Python 3.8 and greater for development. The project uses various Python packages to achieve its objectives, with some of the notable ones being `selenium`, `behave`, `splinter`, `stere`,`maria-db` and `webdriver-manager` among others.

This project endeavors to create Magento2/Adobe Commerce projects that are robust, maintainable, and solves real-world problems effectively. Key concepts of software development, such as object-oriented design and clean code, are embraced fully.

The project also exposes you to libraries and frameworks commonly used in Python ecosystem, thereby giving you practical exposure that goes beyond theoretical knowledge.

Whether you're a seasoned developer or an individual in the earlier stages of the Python learning curve, contributing to this project offers a tremendous opportunity to learn, grow and make a difference. 

To get started, make sure you've Python 3.8 or greater installed on your machine alongside the necessary Python packages listed in the requirements file.


### Benefits of Using BDD in a Magento 2 Project

Behavior-Driven Development (BDD) is a powerful approach that aligns software development with business expectations. Utilizing BDD in a Magento 2 project using Python brings numerous benefits:

1. **Communication Enhancement:** BDD enhances communication between developers, stakeholders, and non-technical or business participants. It allows everyone to have a clear understanding of the project requirements.

2. **Focus on the End User:** BDD encourages the team to focus on the end user’s perspective, ensuring that the development process centers around the delivery of features that provide real value to users.

3. **Reduced Ambiguity:** BDD scenarios provide a clear agreement on what is to be delivered, reducing ambiguities and rework.

4. **Regression Detection:** BDD aligns with Test-Driven Development (TDD) to ensure that all code is covered by tests. This early detection of bugs reduces the cost and time involved in fixing them.

5. **Integration with Agile and Continuous Delivery:** BDD is ideal for Agile development and complements continuous integration and delivery, thereby accelerating product releases and ensuring robust quality.

In essence, utilizing BDD in a Magento 2 project using Python facilitates effective communication, ensures optimal focus on delivering user value, enhances requirement clarity, aids in early bug detection, and promotes seamless integration with Agile and continuous delivery practices.

### Why using Python Instead of PHP for BDD in Magento 2?

While PHP has served as a strong language for web development over the years, Python offers certain advantages that make it a preferred choice for projects like mage2-behave. Here's why:

1. **Readability and Syntax:** Python follows a strict indentation enforcement, which leads to clear, readable code. Its syntax is designed to be easy to understand and use.

2. **Extensive Libraries:** Python is known for its vast selection of libraries, many of which simplify tasks that would be more complex in PHP, e.g. setting up the environment for BDD development.

3. **Versatility:** Python is highly versatile and is not just limited to web development. It can be used to develop a variety of applications, from web and desktop applications to network servers and machine learning algorithms.

4. **Strong Community**: Python has a vibrant community that contributes to a rich ecosystem of libraries and frameworks. This means you are likely to find help or an existing solution to your problem faster than in PHP.

5. **Integration Feature**: Python can be easily integrated with languages like C, C++, and Java, making it a powerful tool for web application development.

6. **Independent of PHP version used by Magento 2**: Tests written in Python will be easily more portable to other Magento 2 projects without the need to refactor code due to a different PHP version used by Magento 2.

Remember, the decision between Python and PHP depends on the requirements of the project, and each has its strengths. However, for mage2-behave, Python's strengths align more closely with the project's goals and needs.

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
- **MacOS**: Modern MacOS versions come pre-installed with Python 2.x and 'python' command refers to that version. Users need to install Python 3.x separately which can be invoked with `python3` command. 

A good way to check your Python version and to validate the command is by typing `python --version` or `python3 --version` in your terminal. It should return the Python version that the command points to.

To ensure compatibility across multiple systems, it is recommended to use `python3` in all the commands and scripts for this project. Also, consider using [virtual environments](https://docs.python.org/3/library/venv.html) to isolate your Python environment per project.
