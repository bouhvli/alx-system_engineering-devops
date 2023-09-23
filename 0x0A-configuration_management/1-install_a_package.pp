package { 'python3-pip':
  ensure => 'latest',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
