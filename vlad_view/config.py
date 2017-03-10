from elasticsearch import Elasticsearch

host = "10.10.7.224"
client = Elasticsearch(host=host, timeout=500)
index = "1stincoffee.magemojo.com-auditd"

size = 50000
par_fields = ["comm", "syscall", "egid"]
ch_fields = ["nametype"]

par_type = "auditd-parent"
child_type = "auditd-child"
