

from django.db import models
import datetime


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    firstname = models.CharField(max_length=30, null=True)
    lastname = models.CharField(max_length=30, null=True)
    def __unicode__(self):
        return self.username

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
    name = models.CharField(max_length=256)
    # email = models.EmailField(max_length=30, null=True, verbose_name="E-mail")
    website = models.CharField(max_length=256, null=True)
    geography = models.CharField(max_length=256, null=True, choices=GEOGRAPHY_CHOICE)
    industry = models.CharField(max_length=256, null=True, choices=INDUSTRY_CHOICE)
    ispublic = models.BooleanField(default=False, verbose_name="Make Plublic")
    def __unicode__(self):
        return self.name
    def get_industry(self):
        return dict(self.INDUSTRY_CHOICE).get(self.industry)
    def get_geography(self):
        return dict(self.GEOGRAPHY_CHOICE).get(self.geography)
    def website_href(self):
        return "http://"+self.website if (self.website and not self.website.startswith("http://")) else self.website


def timedelta_to_seconds(td):
    return (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6

class Reference(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer) 
    title = models.CharField(max_length=256)
    summary = models.CharField(max_length=256)
    story = models.CharField(max_length=3000)
    link = models.CharField(max_length=3000, editable=False)
    ispublic = models.BooleanField(default=False, verbose_name="Make Public")
    votes = models.IntegerField(default=0, editable=False, blank=True)
    hotness = models.IntegerField(default=0, editable=False, blank=True)
    pubDate = models.DateTimeField(auto_now_add=True)
    submitter = models.ForeignKey(Account, editable=False)
    def get_my_vote(self, username):
        my_vote = ReferenceVote.objects.filter(reference=self, account = Account.objects.filter(username=username))
        self.my_vote = True if my_vote else False
    
    def update_hotness_score(self):
        # a la HackerNews
        if not self.votes:
            self.hotness = 0
            return
        gravity = 1.8
        seconds_per_day = 24 * 60 * 60
        timedelta = datetime.datetime.now() - self.pubDate
        age_in_days = round(timedelta_to_seconds(timedelta) / seconds_per_day)
        age_in_minutes =  round(timedelta_to_seconds(timedelta) / 60)
        self.hotness = int(round(  (self.votes - 1) / pow(age_in_days+1, gravity) ))

class ReferenceVote(models.Model):
    reference = models.ForeignKey(Reference)
    account = models.ForeignKey(Account)
    submitDate = models.DateTimeField(auto_now_add=True)
