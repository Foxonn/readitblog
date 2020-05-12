app_name = 'readit'

content = """
version: '3'

services:
  nginx:
    image: nginx
    ports:
      - '80:80'
      - '443:443'
    links:
      - webapp
    volumes:
      - {app_name}_sock:/sock/
      - {app_name}_media:/usr/src/media/
      - {app_name}_static:/usr/src/static/
      - ./config/nginx.conf:/etc/nginx/nginx.conf
  webapp:
    image: foxonn/django3:{app_name}
    env_file: .env
    volumes:
      - {app_name}_sock:/sock/
      - {app_name}_static:/webapp/static/
      #- {app_name}_media:/webapp/media/
      - ./webapp/:/webapp/
      - ./config/:/config/
    links:
      - memcached
      - postgres
    command: uwsgi --ini /config/uwsgi.ini
    working_dir: /webapp
  postgres:
    image: postgres
    env_file: .env
    volumes:
      - {app_name}_pg_data:/var/lib/postgresql/data/
      - ./config/postgresql.conf:/etc/postgresql/postgresql.conf
    command: -c \'config_file=/etc/postgresql/postgresql.conf\'
  memcached:
    image: memcached
    command: -m 512

volumes:
  {app_name}_sock:
  {app_name}_static:
  {app_name}_media:
  {app_name}_pg_data:
""".format(app_name=app_name)

f = open('docker-compose.yaml', 'w')
f.write(content)
f.close
