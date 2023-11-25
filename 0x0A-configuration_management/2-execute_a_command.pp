#Creates a manifest that kills a process called killmenow
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
  path    => ['/bin', '/usr/bin/bin'],
}
