# sets the configuration file to connent to a server without typing a passsword
class ssh_config {
  file { 'alx-system_engineering-devops/0x0B-ssh/.ssh/config':
    ensure  => file,
    content => "# Puppet-managed file. Do not edit.\n
    HostName 100.25.137.152
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no\n",
  }
}
