# Emoji Mood Tracker

A Django-based web application for tracking daily moods using emojis.

## Setup

1. Clone the repository:
```git clone https://github.com/yourusername/emoji-mood-tracker.git```
and then
```cd emoji-mood-tracker```

2. Install dependencies:
```pip install -r requirements.txt```

3. Set up the database:
```python manage.py migrate```

4. Create a superuser:
```python manage.py createsuperuser```

5. Install Tailwind CSS:
```python manage.py tailwind install```

6. Run the development server:
```python manage.py runserver```

7. In a separate terminal, start the Tailwind CSS build process:
```python manage.py tailwind start```

## Running Tests
```python manage.py test```

## Linting
```flake8 .```

## Deployment
Before deploying, build the Tailwind CSS file:
```python manage.py tailwind build```

