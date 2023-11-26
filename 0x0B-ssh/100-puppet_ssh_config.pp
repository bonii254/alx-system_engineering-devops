#Puppet to make changes to our configuration file
file { '/etc/ssh/ssh_config':
  ensure => 'file',
  mode => '0600',
  content => '
Host 100.25.2.209
  IdentityFile  ~/.ssh/school
  PasswordAuthentication no
',
}
