#!/bin/bash
attempt=10
migrate() {
	result=1
	python manage.py migrate
	var=$?
	if [[ $var == 0 ]]
	then
		result=0
	fi
	return "$result"
}

start_migration() {
	echo "Starting migration"
	echo "Trying making migration $attempt times."
	migrate
	result=$?
	i=1
	if  [[ 0 != $result ]]
	then
		echo "Attempt n°$i: Failed"
	else
		echo "Attempt n°$i: Success"
	fi
	while [[ 0 != $result ]]
	do
		sleep 5
		migrate
		result=$?
		((i++))
		if  [[ 0 != $result ]]
		then
			echo "Attempt n°$i: Failed"
		else
			echo "Attempt n°$i: Success"
		fi
		if [[ $i == $attempt ]]
		then
			if  [[ 0 != $result ]]
			then
				echo "Migration failed"
				return 1
			fi
		fi
	done
	echo "Migration done"
	return 0
}

collect_static() {
	if [ $DEBUG = False ]
	then
		echo "collecting static files"
		rm -rf ./staticroot/*
    	python manage.py collectstatic
	else
		echo "skip collecting static files step"
	fi
}

load_data() {
    echo "load data"
    # python manage.py loaddata db.json
    ./data/loaddata.sh
}


change_permissions() {
    chgrp -R www-data /var/www/django/media/
    chmod -R 770 /var/www/django/media/
}

create_superuser() {
    if [ -z "$DJANGO_SUPERUSER_NAME" ] || [ -z "$DJANGO_SUPERUSER_MAIL" ] || [ -z "$DJANGO_SUPERUSER_PASSWORD" ]; then
        echo "Environment variables for database not set, not creating superuser."
    else
        echo "Creating superuser"
				isAdminExist=$(echo "from django.contrib.auth.models import User; isadminexist=User.objects.filter(username='$DJANGO_SUPERUSER_NAME').exists(); print(isadminexist)" | python manage.py shell)

				if [ $isAdminExist = "False" ]
				then
					echo "from django.contrib.auth.models import User; User.objects.create_superuser('$DJANGO_SUPERUSER_NAME', '$DJANGO_SUPERUSER_MAIL', '$DJANGO_SUPERUSER_PASSWORD')" | python manage.py shell
				fi
    fi
}


setup_server() {
	python /usr/bin/gunicorn mysite.wsgi:application -w 2 -b :8000 -t 600 &
}

echo toto
echo $1
echo $?
echo $@


CMD="/bin/bash"
if [ $1 ]
then
	start_migration
	migration=$?
	if [[ 0 != $migration ]]
	then
		echo "Stopping"
		exit -1
	fi
	collect_static
	load_data
	create_superuser
	change_permissions

  if [[ $1 != 'python' ]]
	then
	    echo "setup_server prod mode"
	    setup_server
        else
	    echo "setup_server dev mode"
        fi
	echo "Running: $@"
	$@
else
	echo "Starting: $CMD"
	$CMD
fi
