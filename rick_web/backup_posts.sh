echo dumping blogapp data
python manage.py dumpdata blogapp > blogapp.json
mv blogapp.json blogapp/backup/blogapp.json
