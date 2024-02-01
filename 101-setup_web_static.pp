# set up web servers for deployment.
exec {'update':
  command  => 'apt-get -y update',
  provider => 'shell'
}

package {'nginx':
  ensure  => present,
  require => Exec['update']
}

exec {'create_folder':
  command  => 'mkdir -p /data/web_static/releases/test/ && mkdir -p /data/web_static/shared/',
  provider => 'shell',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

file { '/data/web_static/current':
  ensure  => link,
  target  => '/data/web_static/releases/test',
  require => Exec['create_folder']
}

exec {'configure':
  command => 'grep -q "location /hbnb_static/" /etc/nginx/sites-available     /default || sed -i "49a\ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_     static/current/;\n\t}" /etc/nginx/sites-available/default',
  require => Package[nginx]
}

exec {'change_owner':
  command  => 'chown -R ubuntu:ubuntu /data/',
  provider => 'shell',
  require  => Exec['create_folder']
}

service { 'nginx':
  ensure => running,
  enable => true,
}
