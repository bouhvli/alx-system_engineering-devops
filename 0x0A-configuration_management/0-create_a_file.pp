# this create a file in /tmp, using Puppet.

file { '/tmp/shcool':
  mode    => '0744',
  group   => 'www-data',
  owner   => 'www-data',
  content => 'I love Puppet',
}
