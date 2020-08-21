# class Company(object):
#     def __init__(self, employee_list):
#         self.employee_list = employee_list
        
#     def __getitem__(self, item):
#         return self.employee_list[item]


# company = Company(["Tom","Willl","Dan"])

# company1 = company[:2]

# for em in company1:
#     print (em)

import bisect
inter_list = []
bisect.insort(inter_list,3)
bisect.insort(inter_list,5)
bisect.insort(inter_list,6)
bisect.insort(inter_list,1)
bisect.insort(inter_list,9)
bisect.insort(inter_list,0)

print (bisect.bisect(inter_list,3))
print(inter_list)