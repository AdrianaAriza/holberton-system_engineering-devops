# kill a process
exec { 'http-header':
  command  => 'sudo apt-get -y upgrade &&
  	       sudo apt-get -y update &&
  	       sudo apt-get -y install nginx &&
	       n3="sendfile on;\n\tadd_header X-Served-By $HOSTNAME;"
	       sudo sed -i "s/sendfile on;/$n3/" /etc/nginx/nginx.conf &&
	       sudo service nginx start',
  provider => shell,
}

