#Executing increase of request limit of nginx
exec { 'change ulimit':
    command  =>  'sed -i "s/15/2000/" /etc/default/nginx;
                sudo service nginx restart',
    provider => 'shell',
}
