# loaddata to restore the data
echo dumping blogapp data
python3 manage.py dumpdata blogapp > blogapp.json
mv blogapp.json blogapp/backup/blogapp.json
