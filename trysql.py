from django.db import connection

import numpy as np



import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SPMV2.settings")

import django
django.setup()

from django.core.management import call_command

from spmapp.models import *

row = []

with connection.cursor() as cursor:
    cursor.execute('''
           
         Select *
         From spmapp_student_t
         
          
            
         

        
        
    '''.format(1898336,"Spring",2020))

    row.append(cursor.fetchall())

for i in row:
    print(i)


