app_name = 'readit'

content = "version: '3'"

content += """
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
      - {app_name}_media:/usr/src/media
      - {app_name}_static:/usr/src/static
      - ./config/nginx.conf:/etc/nginx/nginx.conf
  webapp:
    image: foxonn/django3:{app_name}
    env_file: .env
    volumes:
      - {app_name}_sock:/sock
      - {app_name}_static:/webapp/static
      - {app_name}_media:/webapp/media
      - ./webapp/:/webapp/
      - ./config/:/config/
    links:
      - memcached
      - postgres
    command: uwsgi --ini /config/uwsgi.ini
    working_dir: /webapp/{app_name}
  postgres:
    image: postgres
    env_file: .env
    volumes:
      - {app_name}_postgres:/var/lib/postgresql/data
      - ./config/postgresql.conf:/etc/postgresql/postgresql.conf
    command: -c \'config_file=/etc/postgresql/postgresql.conf\'
  memcached:
    image: memcached
    command: -m 512
  rabbitmq:
    image: rabbitmq
    env_file: .env
    ports:
      - '5672:5672'
    volumes:
      - {app_name}_rabbitmq:/var/lib/rabbitmq

volumes:
  {app_name}_sock:
  {app_name}_static:
  {app_name}_media:
  {app_name}_postgres:
  {app_name}_rabbitmq:
""".format(app_name=app_name)

f = open('docker-compose.yaml', 'w')
f.write(content)
f.close
