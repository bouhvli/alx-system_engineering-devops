![Task 2](https://github.com/bouhvli/alx-system_engineering-devops/blob/345f20dc72d90bee375aceb4f9357a76156a38f1/0x09-web_infrastructure_design/task2.png)
# Task 2:
design a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.
---
## specifications about the infrastructure:
- What are firewalls for:
    - limits the trafic, block, and filter unauthorized users, mainly firewalls used to protect the components it is installed on from
    malwares, cyberattacks..., and by doing that it enhance the performance of the servers as an example.

- Why is the traffic served over HTTPS:
    - protect data form being accessed by unwanted entities by encrypting it only the sender and the reciever knows how to decrypt it because of the SSL certificat
    established between the two.

- What monitoring is used for:
    - it is used to detect unwanted behavoir from the hardware or software.

- How the monitoring tool is collecting data:
    - by collecting data from log files from servers, and analyse metrics from the system(CPU, Memory...) and send it to the monitoring system used.

- Explain what to do if you want to monitor your web server QPS:
    - collect the data, and configuring alerts in case of crashs to take actions.
## issues about the infrastructure:

- Why terminating SSL at the load balancer level is an issue:
    - that means sacreficing the performance, because dycripting SSL trafic out of the Load Balancer reduce the latency of the request,
    - security, and the trafic will be vulnerble to attacks.
    - complexity, mean the need to manage the certificats on the LB and the web servers.

- Why having only one MySQL server capable of accepting writes is an issue:
    - because the replicated data can not be updated if the master server is down we can not write into the replicated data.

- Why having servers with all the same components (database, web server and application server) might be a problem:
    - if a server is hacked means that all the other at risque.
    - if any server is overloaded, all the servers will wait for it to finish.
    - by scaling the app, upgrading server components hardware or software will consume time and it is expansive.

