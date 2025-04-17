# Question no 1
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
new_dic = {}
for key,values in students.items():
    gpa_each_student = round(sum(values) / len(values), 2)
    new_dic.update({key:gpa_each_student})
print(max(sorted(new_dic.items()), key=lambda x: x[1]));