![Task 0](https://github.com/bouhvli/alx-system_engineering-devops/blob/b3935c9da4dafe5bc7163412d892aeea70c0a32e/0x09-web_infrastructure_design/tsak0.jpg)
# Task 0:
design a one server web infrastructure that hosts the website that is reachable via www.foobar.com. Start your explanation by having a user wanting to access your website.
---
## specifications about the infrastructure:
- What is a server: a program or a physical computer, runing an OS (windoes server, ubuntu ...) mostly located in a datacenter,
                      prvides other users with the requested files, data or computations ...
- What is the role of the domain name: mainly to make easier for human being to remember IP address of each website.
- What type of DNS record www is in www.foobar.com: the dns record used is A record.
- What is the role of the web server: the role of a web-server is to respond to HTTP requests (deliver static web pages)
- What is the role of the application server: host and execute application programs, and deliver dynamic webpages.
- What is the role of the database: is to store, organize and manage data about the hosted applications.
- What is the server using to communicate with the computer of the user requesting the website: the server uses the TCP/IP, when the user requests a website, their computer
                      sends a TCP request to the server , and the server will respond with the requested data.
## issues about the infrastructure:
- SPOF: it is an entity that may cose a break down of the entire system such as load balancers, the SPOF can be caused by a software and hardware.
- Downtime when maintenance needed: since we are using only one server, updating adding new features, force us to retart the server, causing a **downtime**
- Cannot scale if too much incoming traffic: beacause having one server the amount of trafics that can be handled is limited, which may cause the server to crash
