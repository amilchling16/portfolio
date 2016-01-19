server {
	listen 80 default_server;

	root /var/www/allisonmilchling.com;
	index index.html index.htm;

	# Make site accessible from http://localhost/
	server_name allisonmilchling.com;

	location / {
		try_files $uri.html $uri/ =404;
		# Uncomment to enable naxsi on this location
		# include /etc/nginx/naxsi.rules
	}

}
