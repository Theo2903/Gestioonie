FROM python:3.8

# Initialize
RUN apt-get update \
    && apt-get install -y gunicorn nginx

RUN curl -sLo /usr/local/bin/ep https://github.com/kreuzwerker/envplate/releases/download/v0.0.8/ep-linux && chmod +x /usr/local/bin/ep

# Setup
COPY entrypoint.sh /var/www/django/entrypoint.sh
RUN chmod +x /var/www/django/entrypoint.sh

RUN rm -f /etc/nginx/sites-enabled/default
COPY sites-enabled/nginx.conf /etc/nginx/sites-enabled/nginx.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Prepare
COPY requirements.txt /var/www/django/
WORKDIR /var/www/django
RUN pip install -r requirements.txt
COPY mysite /var/www/django/mysite/
RUN mkdir -p mysite/static/admin


WORKDIR /var/www/django/mysite

ENTRYPOINT ["/var/www/django/entrypoint.sh"]

CMD ["/usr/local/bin/ep", "-v", "/etc/nginx/sites-enabled/nginx.conf", "--", "/usr/sbin/nginx", "-c", "/etc/nginx/nginx.conf"]
