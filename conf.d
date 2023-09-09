events {
    worker_connections 1024;
}
http {
    include    /etc/nginx/mime.types;
    upstream webapp {
    server abiodoun_api:8000;
}
    server {

    listen              443 ssl;
    server_name         ${api_host};
    ssl_certificate     /etc/letsencrypt/live/${api_host}/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/${api_host}/privkey.pem;

    location / {
        proxy_pass http://webapp;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
    }

    location /static/ {
     alias /code/static/;
    }
}

}
