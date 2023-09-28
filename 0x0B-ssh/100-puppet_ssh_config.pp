#configured to use the private key ~/.ssh/school
file { '/etc/ssh/ssh_config':
  ensure  => 'present',
  content => "
        PasswordAuthentication no
        IdentityFile ~/.ssh/school
  ",
  replace => true,
}
