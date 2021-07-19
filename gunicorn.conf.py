import multiprocessing

# The socket to bind.
bind = '0.0.0.0:8080'

# The number of worker processes for handling requests.
workers = multiprocessing.cpu_count() * 2 + 1

# The type of workers to use.
worker_class = 'gevent'

# The number of worker threads for handling requests.
threads = multiprocessing.cpu_count() * 2

# Restart workers when code changes.
reload = True

# Load application code before the worker processes are forked.
preload = True

# Daemonize the Gunicorn process.
daemon = False

# The maximum number of pending connections.
backlog = 2048
