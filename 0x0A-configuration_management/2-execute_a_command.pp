# manifest to kill a process named `killmenow`
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}
