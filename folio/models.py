from django.db import models


# Create your models here.
class Bio(models.Model):
    # first_name - char field
    # middle_name - char field
    # last_name - char field
    # headline - char field
    # introduction - text field
    # profile_image - image field
    # resume - file upload
    pass


class Projects(models.Model):
    # title - char field
    # project_image - image field
    # technologies_used - text field
    # project url - url field
    # date_created - date field
    pass


class Education(models.Model):
    # school_name - char field
    # course - char field
    # start_date - date field
    # end_date - date field
    pass


class WorkExperience(models.Model):
    # organization - char field
    # position_held - char field
    # duties - text field
    # start_date - date field
    # end_date - date field
    pass


class Certification(models.Model):
    # name - char field
    pass


class Contact(models.Model):
    # email - email field
    # cell_phone1 - integer field
    # cell_phone2 - integer field
    pass
