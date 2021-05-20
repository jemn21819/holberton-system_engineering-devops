# fix it and then automate it using Puppet
exec {'fix php ext.':
  command => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}
