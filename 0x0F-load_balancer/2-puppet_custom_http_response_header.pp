#  automate the task of creating a custom HTTP header response, but with Puppet.

exec { 'HTTP header':
    provider => shell,
    command  => 'sudo apt update;
    sudo apt install -y nginx;
    sudo sed -i "50i\\t\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default;
    sudo service nginx restart'
}