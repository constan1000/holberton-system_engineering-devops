# update +install ngnix 
# Install Nginx web server (w/ Puppet)

exec {'up':
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
  command  => 'sudo apt-get -y update',
package { 'nginx':
  ensure => installed,
}

# install ngnix 
exec {'ngin':
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
  command  => 'sudo apt-get -y install nginx',
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

exec {'conf':
  provider => shell,
  command  => 'sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/google.com\/ permanent;/" /etc/nginx/sites-available/default',
file_line { '/etc/nginx/sites-available/default':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/ permanent;',
}

exec { 'upindex':
  provider => shell,
  command => 'echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html',
file { '/var/www/html/index.nginx-debian.html':
  content => 'Holberton School',
}


exec {'restart':
  provider => shell,
  command  => 'sudo service nginx start',
} 
