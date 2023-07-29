# Overview
Deployment of a data pipeline in the cloud using a cluster of distributed virtual machines (VMs). Our primary objective was to generate multiple data sources on a locally created VM then transfer the data to cloud-based VMs through Apache ZooKeeper and Kafka. The data would subsequently be stored and visualized in CouchDB. The three primary project stages were:

-	Manually configured VM1 to run the data-generating python developed producer, while VM2 was outfitted with the Apache ZooKeeper server, Kafka, and a python consumer application. VM3 was equipped with a secondary Kafka broker and a CouchDB instance.

-	Transitioned towards automation to enhance efficiency and reduce risk of human error. Using Vagrant to automate the creation of the local VM1 and developing Ansible playbooks to fully automate the pipeline, encompassing tasks ranging from creating the cloud VMs (VM2 and VM3) to application deployment.

-	Incorporated containerization for an improved level of isolation and scalability. Transitioned from running processes on VMs to utilizing Docker containers, effectively managed and orchestrated by Kubernetes. This setup involved creating Dockerfiles and Kubernetes YAML files, establishing a Kubernetes cluster, and ensuring the pipeline's effective operation within this Kubernetes-managed cluster—all achieved through Ansible automation.
# Outcomes:
-	Manual pipeline implementation provided a deep understanding of component interconnections, laying the foundation for future automation design and execution.

-	Vagrant simplified the process of creating and managing VMs, while Ansible empowered the automated deployment of the application code and managed cloud infrastructure. This provided a repeatable and consistent environment setup.

-	Docker provided an extra layer of abstraction and automation of operating-system-level virtualization, improving the isolation of the different components of our pipeline, while Kubernetes ensured better management and scalability of the containerized applications.	
# Tools: 
VirtualBox, Ubuntu, Vagrant, Ansible, Docker, Kubernetes, Chameleon Cloud, Apache Kafka, Apache CouchDB, Python - Requests, Kafka, JSON, CouchDB

# Demo Video Links 
[Part 1   ](https://drive.google.com/file/d/15hYCKiFmBqPa8YFsPxigeiVNOKLRe567/view?usp=sharing) - Manual Deployment of a Data Transfer Pipeline using Virtual Machines    

[Part 2   ](https://drive.google.com/file/d/1WkpxzxABwT8IV7E7tfjOGIY7D_6bJLpH/view?usp=sharing) - Automating data transfer pipeline: DevOps Infrastructure-as-Code   

[Part 3   ](https://drive.google.com/file/d/1mYoRNJ4-HuIjti9B1liqh1KPgaqevBll/view?usp=sharing) - Automated Data Pipeline Deployment With Kubernetes-Driven DevOps
