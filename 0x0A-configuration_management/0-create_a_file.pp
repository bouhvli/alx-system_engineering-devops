# this create a file in /tmp, using Puppet.

file { '/tmp/shcool':
  content => 'I love Puppet',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744',
}
