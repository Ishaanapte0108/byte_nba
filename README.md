ERP for appraisal process

1> Remove all sections apart from the questions
2> Edit title field to blank if error of invalid title field
3> Paste template into actual json file (for fields and field order)
4> bench migrate
5> Rewrite directions
6> Edit python file (take reference from certification for courses allotted and BSA co curricular)

6.1> imports
6.2> autoname
6.3> Shorten before save
6.4> Copy paste validations line
6.5> validate excel values and computed values

7> Change JS file according to template, put right name in line 2
8> Go to role permission manager

8.1> Delete existing records
8.2> Update excel by changing ID and Reference fields
8.3> GO to data import 
8.4> Start new data import

9> GO to doctype and under permission rules make sure u have system manager, vit_emp and reviewer
10> Revert title field to professor
11> Check everything is fine
12> Add doctype name to report.py at line 55
