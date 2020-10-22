# python ideas
The repo with useful python patterns that can help in coding , debugging and refactoring

## Folders:
1. logger: 
    - contains the exemplary configuration of logger class
    - in `logger_tool.py` logger is defined and functions `wrap`, `entering` and `exiting`
    - in `buisness_logic.py` there is an instantiating of Logger class and exemplary usage of that
    - thanks to the decorator in log file we can see when the particular function was entered and when exited  
    - below the logfile resulting from running business_logic.py

``` bash
77033 | logger_tool | 2020-10-22 12:54:14,645 | DEBUG    | Entered read_data
77033 | __main__ | 2020-10-22 12:54:15,021 | INFO     | 
        
Columns of df_titanic dataset:

Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
      dtype='object')

Description of df_titanic dataset:

       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
    
77033 | logger_tool | 2020-10-22 12:54:15,021 | DEBUG    | Exited  read_data

```