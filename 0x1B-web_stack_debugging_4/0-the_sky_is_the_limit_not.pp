# Set the Nginx ULIMIT to a higher value

exec { 'replace ULIMIT':
    path    => '/usr/bin',
    command => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 262144\"/g" /etc/default/nginx',
}
-> exec { 'restart NGINX':
    path    => '/usr/bin',
    command => 'service nginx restart',
}
