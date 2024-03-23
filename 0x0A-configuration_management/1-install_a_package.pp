#!/user/bin/pup
exec { 'install flask':
  command => 'sudo pip3 install flask==2.1.0',
  path    => '/usr/bin',
  }
