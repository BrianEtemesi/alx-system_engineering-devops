# sets the configuration file to connent to a server without typing a passsword
file { '/home/ubuntu/.ssh/config':
  ensure  => present,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => "Host remote_server\n  Hostname 100.25.137.152\n  User ubuntu\n  IdentityFile ~/.ssh/school\n",
}
