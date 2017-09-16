import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('datasets/enrollments.csv')
daily_engagement = read_csv('datasets/daily_engagement.csv')
project_submissions = read_csv('datasets/project_submissions.csv')

### For each of these three tables, find the number of rows in the table and
### the number of unique students in the table. To find the number of unique
### students, you might want to create a set of the account keys in each table.

enrollment_num_rows = len(enrollments)
eachItem = set()
for item in enrollments:
    eachItem.add(item['account_key'])
enrollment_num_unique_students = len(eachItem)

unique_daily_engagement = set()
for item_daily in daily_engagement:
    unique_daily_engagement.add(item_daily['acct'])
engagement_num_rows = len(daily_engagement)

engagement_num_unique_students = len(unique_daily_engagement)
unique_project_submissions = set()
for item_project in project_submissions:
    unique_project_submissions.add(item_project['account_key'])
submission_num_rows = len(project_submissions)
submission_num_unique_students = len(unique_project_submissions)
