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
12> Add doctype name to analysis.py at line 55



Requirements for adding access control to your website

1> Make sure to have reviewers doctype
2> Make sure to have users in your database
3> Make sure to have professors doctype
4> Create has role profiles

4.1> executive pofile 
has role {executive} 
//create role if not present, disable all except notifications, timeline and dashboard

4.2> system manager profile
//create role if not present, disable all except notifications, timeline and dashboard

4.3> principle profile
//create role principle if not present, disable all except notifications, timeline and dashboard

4.4> trustee profile 
//create role trustee if not present, disable all except notifications, timeline and dashboard

4.5> pa profile
//create role pa_teamif not present, disable all except notifications, timeline and dashboard

4.6> faculty role profile 
//create role vit_emp if not present, disable all except notifications, timeline and dashboard

4.7> reviewer profile 
reviewer






































