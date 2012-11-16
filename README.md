cloudstart
==========

A simple way to bootstrap your cloud instances based on user-data

LICENSE: MIT
------------
Copyright (c) 2012 Jason Hancock <jsnbyh@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

WHY?:
-----

This project exists for a couple of reasons. First, I'm a CloudStack user and
the user-data associated with a VM running on a CloudStack cloud is limited to
2KB after it's been base64 encoded. That means that every byte is important if
you have a lot of config data you are passing. Using a markup language like
yaml would simply waste too much space. The other main reason this project
exists is because I like being able to user the user-data by many different
programs and languages. For example, in a bash script, a perl script, some
ruby code, etc. I wanted to keep it simple to read, simple to parse in a
variety of languages, and dense.

INSTALLATION:
-------------

If you're on a RHEL or RHEL derivative, I would recommending using the included
spec file to build it into an rpm. 

If you're manually installing, copy the cloudstart script to /etc/init.d/, copy
all of the plugins in /usr/share/cloudstart/plugins/, and copy sysconfig into
/etc/sysconfig/cloudstart

USER-DATA:
----------

cloudstart expects user-data to be a list of newline delimited key-value pairs
such as this:

```
hostname=server1.example.com
role=base
environment=development
```

PLUGINS:
--------

Cloudstart's magic happens by running a set of plugins when your VM is booting up.
The plugins get run in the order specified in /etc/sysconfig/cloudstart.

Plugins can be written in any language. When executed, the plugins are passed a
single argument - a temporary file to write/read user-data to/from. This means
that if your plugin is retieving user-data, it should append it to that file. If
your plugin is reading the user-data, read if from that file.

cloudstart ships with the following plugins:
*   **cloudstack** - A plugin to retrieve user-data from CloudStack's virtual routers
*   **hostname** - A plugin that will set the hostname of the system if a key called
hostname is found in the user-data
*   **puppet** - A plugin that will set the puppet agent's environment setting in
/etc/puppet/puppet.conf. You can override the location of puppet.conf by setting
the puppet_conf environment variable in /etc/sysconfig/cloudstart. Future plans
include expanding this plugin to set other settings.

TODO:
-----

*   Some debian love needs to happen
*   AWS support needs to be added
*   Rackspace/OpenStack support needs to be added
