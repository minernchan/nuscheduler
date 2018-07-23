import requests, json

FACULTY_CHOICES = (
    ('Arts and Social Sciences', 'Arts and Social Sciences'),
    ('Business', 'Business'),
    ('Computing', 'Computing'),
    ('Continuing and Lifelong Education', 'Continuing and Lifelong Education'),
    ('Dentistry', 'Dentistry'),
    ('Design and Environment', 'Design and Environment'),
    ('Duke-NUS', 'Duke-NUS'),
    ('Engineering', 'Engineering'),
    ('Integrative Sciences and Engineering', 'Integrative Sciences and Engineering'),
    ('Law', 'Law'),
    ('Medicine', 'Medicine'),
    ('Music', 'Music'),
    ('Public Health', 'Public Health'),
    ('Public Policy', 'Public Policy'),
    ('Science', 'Science'),
    ('University Scholars Programme', 'University Scholars Programme'),
    ('Yale-NUS', 'Yale-NUS'),
)


blank_choice_faculty = (('', 'Please select your faculty...'),)

YEAR_CHOICES = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('Alumni', 'Alumni'),
    ('Incoming Student','Incoming Student'),
    ('Other','Other'),
)

YEAR_CHOICES_SCHEDULE = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('Other','Other'),
)

YEAR_FILTER_CHOICES = (
    ('','All'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('Other','Other'),
)

blank_choice_year = (('','Please select your year of study...'),)

SEMESTER_CHOICES = (
    ('1','1'),
    ('2','2'),
    ('Special Term 1','Special Term 1'),
    ('Special Term 2','Special Term 2'),
)

SEMESTER_FILTER_CHOICES = (
    ('','All'),
    ('1','1'),
    ('2','2'),
    ('Special Term 1','Special Term 1'),
    ('Special Term 2','Special Term 2'),
)

blank_choice_semester = (('','Please select a semester...'),)


def edit(item):
    return tuple(tuple((str(choice), str(choice)) for choice in item))

MODULE_CHOICES = edit(requests.get('http://api.nusmods.com/2018-2019/1/moduleCodes.json').json())