#  automate the task of creating a custom HTTP header response, but with Puppet.
exec { 'HTTP header':
    command  => 'apt-get -y update;
    apt-get install -y nginx;
    sudo sed -i "50i\\t\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default;
    service nginx restart',
    provider => shell
}