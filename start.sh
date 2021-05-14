echo "django makemigrations..."
python manage.py makemigrations
echo "django migrate..."
python manage.py migrate
echo "run server..."
python manage.py runserver 0.0.0.0:3000
