from django.db import models

gender_choices=(
    ('M',"MALE"),
    ('F',"FEMALE"),
)
bool_choices=(
    ('YES',"YES"),
    ('NO',"NO"),
)
med_choices=(
    ('TELUGU',"TELUGU"),
    ('TELUGU',"TELUGU"),
)
category_choices=(
    ("BC-A","BC-A"),
    ("BC-B","BC-B"),
    ("BC-D","BC-D"),
    ("BC-E","BC-E"),
    ("OC","OC"),
    ("SC","SC"),
    ("ST","ST"),
)

pref_choices=(
    ("MPC","MPC"),
    ("BIPC","BIPC"),
    ("CEC","CEC"),
    ("HEC","HEC"),
    ("VOC","VOCATIONAL"),
    ("CHE","CHEMICAL"),
)


class StudentData(models.Model):
    sub=models.BooleanField(default=False)
    username=models.CharField(max_length=16,default=None)
    paymentID=models.CharField(max_length=16,default=None,null=True)

    mobile = models.CharField(primary_key=True,max_length=10)
    
    studentname = models.CharField(max_length=70,default=None)
    fathername = models.CharField(max_length=70,default=None,null=True)
    mothername = models.CharField(max_length=70,default=None,null=True)
    gender = models.CharField(max_length=6,choices=gender_choices,null=True)
    dob= models.CharField(max_length=12,default=None,null=True)
    email = models.EmailField(default=None)
    hallticket = models.CharField(max_length=12,default=None)
    
    ration=models.CharField(max_length=14,default=None,null=True)
    aadhaar = models.CharField(max_length=12,default=None,null=True)
    address = models.TextField(max_length=200,default=None,null=True)
    birth_state=models.CharField(max_length=14,default=None,null=True)
    birth_district=models.CharField(max_length=14,default=None,null=True)

    ph=models.CharField(max_length=6,choices=bool_choices,default=None,null=True)

    cat = models.CharField(max_length=10,choices=category_choices,default=None,null=True)
    ews=models.CharField(max_length=6,choices=bool_choices,default=None,null=True)
    castecert=models.CharField(max_length=14,default=None,null=True)
    ewscert=models.CharField(max_length=14,default=None,null=True)
    minority=models.CharField(max_length=14,choices=bool_choices,default=None,null=True)

    income=models.CharField(max_length=14,default=None,null=True)
    incomecert=models.CharField(max_length=14,default=None,null=True)

    bankac=models.CharField(max_length=14,default=None,null=True)
    bankifsc=models.CharField(max_length=14,default=None,null=True)

    hsno=models.CharField(max_length=14,default=None,null=True)
    village=models.CharField(max_length=14,default=None,null=True)
    town=models.CharField(max_length=14,default=None,null=True)
    pincode=models.CharField(max_length=5,default=None,null=True)
    alt_mobile=models.CharField(max_length=14,default=None,null=True)


    yop=models.CharField(max_length=4,default=None,null=True)
    medium=models.CharField(max_length=6,choices=med_choices,default=None,null=True)
    school=models.CharField(max_length=4,default=None,null=True)

    cls6=models.CharField(max_length=4,default=None,null=True)
    cls7=models.CharField(max_length=4,default=None,null=True)
    cls8=models.CharField(max_length=4,default=None,null=True)
    cls9=models.CharField(max_length=4,default=None,null=True)
    cls10=models.CharField(max_length=4,default=None,null=True)

    pref6=models.CharField(max_length=10,choices=pref_choices,default=None,null=True)
    pref5=models.CharField(max_length=10,choices=pref_choices,default=None,null=True)
    pref4=models.CharField(max_length=10,choices=pref_choices,default=None,null=True)
    pref3=models.CharField(max_length=10,choices=pref_choices,default=None,null=True)
    pref2=models.CharField(max_length=10,choices=pref_choices,default=None,null=True)
    pref1=models.CharField(max_length=10,choices=pref_choices,default=None,null=True)


    photo=models.FileField(default=None,null=True)
    sign=models.FileField(default=None,null=True)

    