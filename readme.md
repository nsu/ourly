# Development

## Install
```sh
pip install -r requirements/dev.txt
```

# Production (Heroku)

## Create App
```sh
# Get the heroku toolbelt https://toolbelt.herokuapp.com/
wget -qO- https://toolbelt.heroku.com/install.sh | sh
heroku apps:create ourly --addons heroku-postgresql:dev
git push heroku master
heroku config:set DJANGO_SETTINGS_MODULE=ourly.settings.prod
heroku run python manage.py syncdb --noinput
```
