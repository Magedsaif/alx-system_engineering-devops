# sets file limite for nginx to 2000 (default is 15)
exec {'sets file limite for nginx':
  command => 'sed -i "s/15/2000/g" /etc/default/nginx',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/',
  onlyif  => 'test -f /etc/default/nginx'
}
