This is a Django app deployed on the server with some other Django apps.

## Deploying a Release
You need to connect to the server from inside the lab network. You can find the
internal IP address in the `servers.md` file in the `dev-docs` repository. If
you don't already have an account on the server, ask the lab director for
access.

The source code is deployed with a Git clone at
`/alldata/bblab_site/tools/variable_function`. To deploy an update, change to that
directory, and then run `sudo git pull`. 

Note that the contents of `static/` should go in `/alldata/bblab_site/static/`. 
This includes the contents of `static/vfa_css/`.

Then restart the Apache server with
`sudo systemctl restart httpd`