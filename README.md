Waltz
=====

Waltz is a pre-built web.py application for rapidly designing web apps
in 3/4 time. Waltz comes pre-configured, ready to run, and includes
features like out-of-the-box support for analytics tracking. Waltz
and never miss a beat.

Installation
------------

Installation occurs in 2 steps. First, clone the waltz repository as to a directory + <project-name> of your choosing. Secondly, you will use pip to install all dependent python modules which includes webpy (as the web framework), lazydb (for storing analytics in flatfile format), and nose (for testing with nosetests).

    # clones waltz to a directory named <project-name> instead of waltz

    git clone git@github.com:mekarpeles/waltz <project-name>

    cd <project-name>

    pip install -e . # installs dependencies