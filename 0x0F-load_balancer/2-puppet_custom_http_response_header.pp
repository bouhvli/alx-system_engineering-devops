#  automate the task of creating a custom HTTP header response, but with Puppet.

exec { 'update':
    provider => shell,
    command  => 'apt.get update',
}
package { 'nginx':
    ensure  => 'installed'
    require => Exec['update']
}
exec { 'header HTTP':
    provider => 'shell',
    command  => 'sudo sed -i "50i\\t\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default'
}
service { 'nginx':
    ensure => 'running',
    require => Package['nginx']
}