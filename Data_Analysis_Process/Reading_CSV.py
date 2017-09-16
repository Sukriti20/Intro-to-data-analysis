import unicodecsv

#enrollments_filename = 'enrollments.csv'

## Longer version of code (replaced with shorter, equivalent version below)

# enrollments = []
# f = open(enrollments_filename, 'rb')
# reader = unicodecsv.DictReader(f)
# for row in reader:
#     enrollments.append(row)
# f.close()

'''with open(enrollments_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)'''
    

engagement_filename = 'datasets/daily_engagement.csv'
submissions_filename = 'datasets/project_submissions.csv'

engagement_list = []
with open(engagement_filename,'rb') as f:
    reader = unicodecsv.DictReader(f)
    engagement_list = list(reader)
    
with open(submissions_filename,'rb') as f:
    reader = unicodecsv.DictReader(f)
    submission_list= list(reader)
    
    
daily_engagement = engagement_list    
project_submissions = submission_list

print(daily_engagement[0])
print(project_submissions[0])
