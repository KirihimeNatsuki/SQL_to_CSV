# Python Script .SQL to .CSV

## Usage

### For non-developper users

Run the executable file : `script_SQL_to_CSV.exe ` and enter the name or the path of the sql file when the program is asking you to enter it.
And done ! You have your .SQL file converted to .CSV file

Example : You launch the .exe file and the script is asking you to enter the sql file name : 2 possibilities
    - mysqlfile.sql
    - C:\Users\user\documents\Script\filename.sql


### For developper users

Just run `python script_SQL_to_CSV.py` and enter the name or the path of the sql file when the script is asking you to enter it.

Example : - `python script_SQL_to_CSV.py` and enter filename like the examples above.

## How It Works
The following SQL:

```sql
CREATE TABLE `table` (
`id` int(10) NOT NULL AUTO_INCREMENT,
`item` varchar(300) NOT NULL,
`price` float(20),
PRIMARY KEY (`id`)
)

INSERT INTO  `table` VALUES 
(0,'item_1', 7.90),
(1,'item_2', 2.50);
```
is turned into the following CSV:

| id   | item   | price |
| ---- |:------:| -----:|
| 0    | item_1 | 7.90  |
| 1    | item_2 | 2.50  |

or just
```sql
INSERT INTO  `sales` (`item`,`price`,`quantity`) VALUES (`apple`, 0.50, 10), (`banana`, 0.40, 16);
```

CAREFUL : There is 2 spaces between the 'INSERT INTO' and the tablename which are specific to my sql work file. To modify it and be able to have only 1 space you need to go to line 26 and reduce the space between them. You should rebuild it by using the following commande : `python setup.py build`

This script is made in Python 3 and works numpy and cx_Freeze(for executable), make sure to install numpy and cx_Freeze with the following commands : `pip install numpy` | `python -m pip install --upgrade cx_Freeze`
You might need more libraries install to make it work (NOT most of the time !), if anything check your errors and install the plugins needed.

###### Made by Enzo Lemarchand.