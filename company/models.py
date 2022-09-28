from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    filepath = models.CharField(max_length=255, blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    search_term = models.CharField(max_length=255, blank=True, null=True)
    article_body = models.TextField(blank=True, null=True)
    reading_count = models.IntegerField(max_length=255, default='0')

    class Meta:
        db_table = 'scraped_data_tbl'

