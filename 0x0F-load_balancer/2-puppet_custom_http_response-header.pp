# kill a process
exec { 'http-header':
  command  => 'apt-get -y upgrade &&
  	       apt-get -y update &&
  	       apt-get -y install nginx &&
  	       sudo sed -i "s/sendfile on;/sendfile on;\n\tadd_header X-Served-By $HOSTNAME;/" /etc/nginx/nginx.conf &&
	       sudo service nginx start',
  provider => shell,
}

