

from django.db import models





class Customer(models.Model):
    ''' geography choice '''
    GEOGRAPHY_CHOICE = (
        (u'EUROPE', u'Europe'),
        (u'N-AMERICA', u'North America'), 
        (u'S-AMERICA', u'South America'),
        (u'ASIA', u'Asia'),
        (u'AFRICA', u'Africa'),
        (u'AUSTRALIA', u'Australia'),
        (u'ANTARTICA', u'Antartica'),
        )

    ''' industry choices '''
    INDUSTRY_CHOICE = (
        (u'INDUST', u'Industries'),
        (u'HEALTH', u'Healthcare'),
        (u'GOV', u'Government'),
        (u'EDU', u'Education'),
        (u'BANK', u'Financial' ),
        (u'TELCO', u'Telecom'),
        (u'OIL', 'Oil & Gas'),
        )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, null=True, verbose_name="E-mail")
    website = models.CharField(max_length=30, null=True)
    geography = models.CharField(max_length=30, null=True, choices=GEOGRAPHY_CHOICE)
    industry = models.CharField(max_length=30, null=True, choices=INDUSTRY_CHOICE)
    ispublic = models.BooleanField(default=False, verbose_name="Make Plublic")
    def __unicode__(self):
        return self.name
    def get_industry(self):
        return dict(self.INDUSTRY_CHOICE).get(self.industry)
    def get_geography(self):
        return dict(self.GEOGRAPHY_CHOICE).get(self.geography)



class Reference(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer) 
    title = models.CharField(max_length=120)
    # story = models.FileField(upload_to="/customer-stories")
    story = models.CharField(max_length=3000)
    ispublic = models.BooleanField(default=False, verbose_name="Make Public")

