# Debugging with strace
exec { 'fix typo':
    command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/:/usr/bin/',
}
