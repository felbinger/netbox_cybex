# Netbox Plugin: Credentials

This plugin adds credentials to virtual machines. It is used exclusively 
for it-security trainings where applications such as Netbox are out of scope.
Do **not** use this plugin to manage your passwords in a non training environment!

## TODO
- inline -> how to overwrite template?
  extend `templates/virtualization/virtualmachine.html`:84
  ```html
  <div class="row">
    <div class="col col-md-12">
      <div class="card">
        <h5 class="card-header">{% trans "Credentials" %}</h5>
        <div class="card-body htmx-container table-responsive"
          hx-get="{% url 'plugins:netbox_credentials:credential_list' %}?virtual_machine_id={{ object.pk }}"
          hx-trigger="load"></div>
        <div class="card-footer text-end noprint">
          <a href="{% url 'plugins:netbox_credentials:credential_add' %}?device={{ object.device.pk }}&virtual_machine={{ object.pk }}&return_url={{ object.get_absolute_url }}" class="btn btn-sm btn-primary">
            <span class="mdi mdi-plus-thick" aria-hidden="true"></span> {% trans "Add Credential" %}
          </a>
        </div>
      </div>
    </div>
  </div><br/>

  ```

## Development Environment
```sh
git clone --branch v3.7.2 --single-branch https://github.com/netbox-community/netbox ~/netbox
python3 -m venv ~/netbox/venv
source ~/netbox/venv/bin/activate
pip3 install -r ~/netbox/requirements.txt

# create configuration from example
cat ~/netbox/netbox/netbox/configuration_example.py | \
  sed -e "s/^DEBUG.*/DEBUG = True/" | \
  sed -e "s/^SECRET_KEY.*/SECRET_KEY = '$(~/netbox/netbox/generate_secret_key.py)'/" | \
  sed -e "s/^ALLOWED_HOSTS.*/ALLOWED_HOSTS = \[\'127.0.0.1\'\]/" | \
  sed -e "s/'USER': ''/'USER': 'postgres'/" > ~/netbox/netbox/netbox/configuration.py

# start database and redis
docker compose up -d

~/netbox/netbox/manage.py migrate
~/netbox/netbox/manage.py createsuperuser \
  --username admin \
  --email admin@localhost.localdomain
~/netbox/netbox/manage.py runserver

# netbox should now reachable on: http://127.0.0.1:8000/

# build plugin
python3 setup.py develop

# add plugin to configuration
sed -i -e "s/^PLUGINS.*/PLUGINS = \['netbox_credentials'\]/" ~/netbox/netbox/netbox/configuration.py

# enable developer mode to enable usage of makemigrations
echo "DEVELOPER=True" >> ~/netbox/netbox/netbox/configuration.py

# Building the app
~/netbox/netbox/manage.py makemigrations
~/netbox/netbox/manage.py migrate
```
