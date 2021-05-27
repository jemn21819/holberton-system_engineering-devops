# web server setup featuring Nginx is doing under pressure and it turns out
# it’s not doing well: we are getting a huge amount of failed requests
exec { 'fix--for-nginx':
  command => "/bin/sed -i 's/worker_processes 4/worker_processes 8/g' /etc/nginx/nginx.conf && /etc/init.d/nginx restart"
}
