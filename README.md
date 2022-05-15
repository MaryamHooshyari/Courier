# Courier

### Daily salary
In this project we have three apps first one is "courier" which 
is for the information about our couriers, then there is "income" 
app that contains three models for Trips, Deductions, and Additions.
The last one is "salary", it has a model to save each day's total 
salary which updates after every add record from income app, so we
always have the list of daily salaries.


### Weekly salary
I implement a view which calculate weekly salaries for all couriers
and shows them with the date of the week's saturday(start day of week in Solar calendar)

### project tree
* [courier](courier)
  * [admin.py](courier/admin.py)
  * [models.py](courier/models.py)
  * [serializers.py](courier/serializers.py)
  * [urls.py](courier/urls.py)
  * [viewsets.py](courier/viewsets.py)
* [income](income)
  * [admin.py](income/admin.py)
  * [models.py](income/models.py)
  * [serializers.py](income/serializers.py)
  * [urls.py](income/urls.py)
  * [viewsets.py](income/viewsets.py)
  * [tests.py](income/tests.py)
* [salary](salary)
  * [admin.py](salary/admin.py)
  * [models.py](salary/models.py)
  * [serializers.py](salary/serializers.py)
  * [urls.py](salary/urls.py)
  * [viewsets.py](salary/viewsets.py)
  * [filtersets.py](salary/filtersets.py)
* [courier_salary](courier_salary)
  * [settings.py](courier_salary/settings.py)
  * [urls.py](courier_salary/urls.py)
* [requirements.txt](requirements.txt)
