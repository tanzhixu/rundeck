#!/usr/bin/evn python
# -*- coding: utf-8 -*-
from jinja2 import Template
l = [
{"tag":"member-center",			"ip":"10.1.17.45"},
{"tag":"member-center",			"ip":"10.1.17.46"},
{"tag":"casher-backend",		"ip":"10.1.17.47"},
{"tag":"casher-backend",		"ip":"10.1.17.48"},
{"tag":"notification-backend",	"ip":"10.1.17.70"},
{"tag":"config-backend",		"ip":""},
{"tag":"timer-backend",			"ip":"10.1.17.78"},
{"tag":"member-center-wap",		"ip":"10.1.17.58"},
{"tag":"octopus-api",			"ip":"10.1.17.10"},
{"tag":"octopus-member-server",		"ip":"10.1.17.12"},
{"tag":"octopus-member-server",		"ip":"10.1.17.13"},
{"tag":"octopus-ums",		"ip":"10.1.17.14"},
{"tag":"static-resources",		"ip":"10.1.17.82"},
{"tag":"report",		"ip":"10.1.18.14"},
{"tag":"passport",		"ip":"10.1.18.94"},
{"tag":"employee-app",		"ip":"10.1.18.96"},
{"tag":"employee-backend",		"ip":"10.1.18.78"},
{"tag":"css",		"ip":"10.1.18.15"},
{"tag":"auth",		"ip":"10.1.18.16"},
{"tag":"platform-changelog",		"ip":"10.1.18.17"},
{"tag":"management-app",		"ip":"10.1.18.43"},
{"tag":"config-app",		"ip":"10.1.18.72"},
{"tag":"timer-app",		"ip":"10.1.18.76"},
{"tag":"timer-agent",		"ip":"10.1.18.80"},
{"tag":"cms",		"ip":"10.1.18.99"},
{"tag":"sales",		"ip":""},
{"tag":"boss-portal",		"ip":"10.1.18.93"},
]

template = '''{ \
{% for i in l %}
  "{{ i['ip'] }}": {
    "tags": "{{ i['tag'] }}",
    "osFamily": "unix",
    "username": "ippjradmin",
    "osVersion": "2.6.32-504.12.2.el6.x86_64",
    "osArch": "amd64",
    "description": "{{ i['tag'] }}",
    "hostname": "{{ i['ip'] }}:6123",
    "nodename": "{{ i['ip'] }}",
    "osName": "Linux"
  }, \
{% endfor %}}
'''

def main():
	t = Template(template)
	outputText = t.render(l=l)
	outputText = outputText.replace(', }','\n}')
	temp_file = '/tmp/resources.json'
	with open(temp_file,'w') as f:
		f.write(outputText)

if __name__ == '__main__':
	main()
