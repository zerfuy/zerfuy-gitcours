from jinja2 import Environment, FileSystemLoader


hostname_router = 'R1'
ip_addr_default='no ip address'
shut_state_default='shutdown'


class interface:
	def __init__(self,ip_addr=ip_addr_default,shut_state=shut_state_default):
		self.ipaddress = ip_addr
		self.shutdown = shut_state


int_lo_0 = interface('ip address 192.168.122.1','!')
int_lo_0_IP = int_lo_0.ipaddress
int_lo_0_shut_state = int_lo_0.shutdown

intf0_0 = interface()
int_f0_0_IP = intf0_0.ipaddress
int_f0_0_shut_state = intf0_0.shutdown

int_f1_0 = interface()
int_f1_0_IP = int_f1_0.ipaddress
int_f1_0_shut_state = int_f1_0.shutdown

int_f1_1 = interface()
int_f1_1_IP = int_f1_1.ipaddress
int_f1_1_shut_state = int_f1_1.shutdown

int_f2_0 = interface()
int_f2_0_IP = int_f2_0.ipaddress
int_f2_0_shut_state = int_f2_0.shutdown

int_f2_1 = interface()
int_f2_1_IP = int_f2_1.ipaddress
int_f2_1_shut_state = int_f2_1.shutdown




file_loader = FileSystemLoader('.')

env = Environment(loader=file_loader)
template = env.get_template('conf-test.j2')
output = template.render(int_lo_0_IP_ji2=int_lo_0_IP,int_lo_0_shut_state_j2=int_lo_0_shut_state,
int_f0_0_IP_j2=int_f0_0_IP,int_f0_0_shut_state_j2=int_f0_0_shut_state,
int_f1_0_IP_j2=int_f1_0_IP,int_f1_0_shut_state_j2=int_f1_0_shut_state,
int_f1_1_IP_j2=int_f1_1_IP,int_f1_1_shut_state_j2=int_f1_1_shut_state,
int_f2_0_IP_j2=int_f2_0_IP,int_f2_0_shut_state_j2=int_f2_0_shut_state,
int_f2_1_IP_j2=int_f2_1_IP,int_f2_1_shut_state_j2=int_f2_1_shut_state
)


fichier = open("output-router_conf.txt", "a")
fichier.write(output)
fichier.close()
