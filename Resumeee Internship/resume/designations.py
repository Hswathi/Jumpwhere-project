from .models import Designation

designations = [
    {'name': 'Software Engineer'},
    {'name': 'Senior Software Engineer'},
    {'name': 'Technical Lead'},
    {'name': 'Project Manager'},
    {'name': 'Product Manager'},
    {'name': 'Business Analyst'},
    {'name': 'Quality Assurance Engineer'},
    {'name': 'UI/UX Designer'},
    {'name': 'Data Scientist'},
    {'name': 'DevOps Engineer'}
]

Designation.objects.bulk_create([Designation(**d) for d in designations])

