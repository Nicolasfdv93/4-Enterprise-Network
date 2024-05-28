Project 4 – Enterprise Networking Project - Devs Config

### ROUTERS ###

## Campus Router ##

en
conf t
hostname Campus-Router

int se0/1/0
no shut
clock rate 64000
ip address 10.10.10.5 255.255.255.252

int se0/1/1
no shut
ip address 10.10.10.1 255.255.255.252

int g0/0
no shut

//Inter-VLAN Routing

int g0/0.10
encapsulation dot1q 10
ip address 192.168.1.1 255.255.255.0
int g0/0.20
encapsulation dot1q 20
ip address 192.168.2.1 255.255.255.0
int g0/0.30
encapsulation dot1q 30
ip address 192.168.3.1 255.255.255.0
int g0/0.40
encapsulation dot1q 40
ip address 192.168.4.1 255.255.255.0
int g0/0.50
encapsulation dot1q 50
ip address 192.168.5.1 255.255.255.0
int g0/0.60
encapsulation dot1q 60
ip address 192.168.6.1 255.255.255.0
int g0/0.70
encapsulation dot1q 70
ip address 192.168.7.1 255.255.255.0
int g0/0.80
encapsulation dot1q 80
ip address 192.168.8.1 255.255.255.0

//DHCP Server

service dhcp
ip dhcp pool Admin-pool
network 192.168.1.0 255.255.255.0
default-router 192.168.1.1
dns-server 192.168.1.1

ip dhcp pool HR-pool
network 192.168.2.0 255.255.255.0
default-router 192.168.2.1
dns-server 192.168.2.1

ip dhcp pool Finance-pool
network 192.168.3.0 255.255.255.0
default-router 192.168.3.1
dns-server 192.168.3.1

ip dhcp pool Business-pool
network 192.168.4.0 255.255.255.0
default-router 192.168.4.1
dns-server 192.168.4.1

ip dhcp pool EyC-pool
network 192.168.5.0 255.255.255.0
default-router 192.168.5.1
dns-server 192.168.5.1

ip dhcp pool AyD
network 192.168.6.0 255.255.255.0
default-router 192.168.6.1
dns-server 192.168.6.1

ip dhcp pool SutdLab-pool
network 192.168.7.0 255.255.255.0
default-router 192.168.7.1
dns-server 192.168.7.1

ip dhcp pool ITDept-pool
network 192.168.8.0 255.255.255.0
default-router 192.168.8.1
dns-server 192.168.8.1
exit

//RIP

router rip
version 2
network 10.10.10.0
network 10.10.10.4
network 192.168.1.0
network 192.168.2.0
network 192.168.3.0
network 192.168.4.0
network 192.168.5.0
network 192.168.6.0
network 192.168.7.0
network 192.168.8.0
do wr

## Branch Router ##

en
conf t
hostname Branch-Router

int se0/2/0
no shut
clock rate 64000
ip address 10.10.10.2 255.255.255.252
exit

//Inter-Vlan Routing

int g0/0
no shut
int g0/0.90
encapsulation dot1q 90
ip address 192.168.9.1 255.255.255.0
exit

int g0/0.100
encapsulation dot1q 100
ip address 192.168.10.1 255.255.255.0
exit

//DHCP Server

service dhcp
ip dhcp pool Staff-pool
network 192.168.9.0 255.255.255.0
default-router 192.168.9.1
dns-server 192.168.9.1
exit

ip dhcp pool Stud-Lab-pool
network 192.168.10.0 255.255.255.0
default-router 192.168.10.1
dns-server 192.168.10.1
exit

//RIP

router rip
version 2
network 192.168.9.0
network 192.168.10.0
network 10.10.10.0
exit
do wr

## Cloud Router ##
en
conf t
hostname Cloud-Router

int g0/0
ip address 20.0.0.1 255.255.255.252
no shut
exit

int se0/1/0
no shut
ip address 10.10.10.6 255.255.255.252
exit

//RIP

router rip
version 2
network 20.0.0.0
network 10.10.10.4

do wr

### SWITCHES ###

## Main-Campus L3 ##

en
conf t
hostname L3-Main-Campus

vlan 10
name Admin
vlan 20
name HR
vlan 30
name Finance
vlan 40
name Business
vlan 50
name EyC
vlan 60
name AyD
vlan 70
name StudLab
vlan 80
name ITDept
vlan 90
name Staff
vlan 99
name native
vlan 100
name StudLabBranch

int g1/0/2
switchport mode access
switchport access vlan 10
exit

int g1/0/3
switchport mode access
switchport access vlan 20
exit

int g1/0/4
switchport mode access
switchport access vlan 30
exit

int g1/0/5
switchport mode access
switchport access vlan 40
exit

int g1/0/6
switchport mode access
switchport access vlan 50
exit

int g1/0/7
switchport mode access
switchport access vlan 60
exit

int g1/0/8
switchport mode access
switchport access vlan 70
exit

int g1/0/9
switchport mode access
switchport access vlan 80
exit

int g1/0/1
no shut
switchport mode trunk
switchport trunk native vlan 99
exit

do wr

## Branch-Campus L3 ##

en
conf t
hostname L3-Branch-Campus

vlan 10
name Admin
vlan 20
name HR
vlan 30
name Finance
vlan 40
name Business
vlan 50
name EyC
vlan 60
name AyD
vlan 70
name StudLab
vlan 80
name ITDept
vlan 90
name Staff
vlan 99
name native
vlan 100
name StudLabBranch

int g1/0/1
no shut
switchport mode trunk
switchport trunk encapsulation dot1q
switchport trunk native vlan 99
exit

int g1/0/2
no shut
switchport mode access
switchport access vlan 90
exit

int g1/0/3
no shut
switchport mode access
switchport access vlan 100
exit

do wr

## ALL L2 Switches ## 

en
conf t

vlan 10
name Admin
vlan 20
name HR
vlan 30
name Finance
vlan 40
name Business
vlan 50
name EyC
vlan 60
name AyD
vlan 70
name StudLab
vlan 80
name ITDept
vlan 90
name Staff
vlan 99
name native
vlan 100
name StudLabBranch
exit

int ran fa0/1-24
switchport mode Access
switchport access vlan 100
exit

int g0/1
switchport mode Access
switchport access vlan 100
do wr
