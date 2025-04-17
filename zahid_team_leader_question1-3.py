# Question no 3
# Separate each student's name from their surname and store them in a separate tuple and add them to a list.

students = {
'Ahmet Yilmaz':	[85,90,	78],
'Mehmet emir':	[92,88,	76],
'Ayse Kaya':	[78,89,	95],
'Zeynep Celik':	[65,70,	80],
'Ali Kara':	    [50,60,	55],
'Fatma Yildiz':	[88,85,	90],
'Murat Aydin':	[72,68,74],
'Elif Aksoy':	[95,90,88],
'Hakan Oztiirk':[45,50,55],
'Canan Tas':	[80,75,82]
}

name_surname_list = []

for full_name in students.keys():
    first_name, last_name = full_name.split()
    name_surname_list.append((first_name, last_name))

print(name_surname_list)