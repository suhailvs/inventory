# FrontEnd

FrontEnd is Angularjs 1.x. All files are placed in `docs` folder for serving easily on [Github](https://suhailvs.github.io/inventory).

# BackEnd Deployment
+ Install Apache

```
$ apt-get update
$ apt-get install python3-pip apache2 libapache2-mod-wsgi-py3
```

+ Change dir: `$ cd /var/www/`
+ Clone the repo: `$ git clone https://github.com/suhailvs/inventory`
+ Change dir: `$ cd inventory`
+ Create virtual and install django:
```
$ python3 -m venv tenv
$ source ./tenv/bin/activate
$ cd dj_backend
$ pip install -r requirements.txt
```

+ Migrate and sync db and give permission to media:
```
$ ./manage.py makemigrations
$ ./manage.py migrate
$ chmod 777 media
$ cd media/
$ chmod 777 db.sqlite3
```


+ Edit apache config :

```
$ vim /etc/apache2/sites-available/inventory.conf

Listen 80
<VirtualHost *:80>

    ServerName ng.helpservice.xyz
    <Directory /var/www/inventory/dj_backend/dj_backend>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    Alias /ng /var/www/inventory/docs
    ErrorLog /var/www/inventory/error.log
    WSGIDaemonProcess inventoryapp python-home=/var/www/inventory/tenv python-path=/var/www/inventory/dj_backend
    WSGIProcessGroup inventoryapp
    WSGIScriptAlias / /var/www/inventory/dj_backend/dj_backend/wsgi.py
</VirtualHost>

```

+ enable site: `a2ensite inventory.conf` 
+ restart apache: `service apache2 reload`

+ Optional: HTTPS Secure Apache with Let's Encrypt

```
$ add-apt-repository ppa:certbot/certbot
$ apt-get update
$ apt-get install python-certbot-apache
$ certbot --apache -d helpservice.xyz