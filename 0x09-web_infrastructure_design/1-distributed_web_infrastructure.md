![Task 0](https://github.com/bouhvli/alx-system_engineering-devops/blob/58f74096456807138a702916871723800402e630/0x09-web_infrastructure_design/task1.jpg)
# Task 0:
design a three server web infrastructure that hosts the website www.foobar.com.
---
## specifications about the infrastructure:
- What distribution algorithm your load balancer is configured with and how it works:
    the algorithm used is Round robin because, since we have two servers the load should be destributed evenly between the two servers,
    and it is the simplest because it checks the servers and select the next in line.

- Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both:
    our load balancer uses the active-active setup because we are using bouth servers to handle the (requests), we are not waiting for one server to break
    to use the other (active-passive).

- How a database Primary-Replica (Master-Slave) cluster works:
    database primary-replica enables the replication of the master database server data into a one or more database servers, if the main or the master
    has changes the data in all the replicated DB servers (slaves) recieves the updates and return an output in seccess,
    the replication can be synchronos or asynchronos.

- What is the difference between the Primary node and the Replica node in regard to the application:
    since we are using the a load balancer and bout servers are functional in the real time, data must be present in bouth servers,
    no matter what server the load balancer chooses the date will be there.
## issues about the infrastructure:
- the SPOF: the load balancer.
- Security issues: may grant unauthorized access, hacker can access the data easaly, the servers can be infacted by malwares.
- No monitoring: will make it diffecult to identify the issues incase of system failure.
