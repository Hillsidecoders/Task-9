# Task-9
Team Task

Kubernetes Integration with Python-CGI

Task Description 📄

📌 In continuation of task 7.1 you need to Integrate Kubernetes commands that can be run through webUI created by you. 

👉 This time create webUI page as such that using normal English conversation your all commands can run in background. 
Example - when we write 'run deployment using httpd image' then it run complete deployment command in backend. 

Feature necessary -

👉 It can launch pods with specific name given by user. 

👉 Run deployment using image and name given by user. 

👉 Expose services on given user input port number. 

👉 Scale the replica according to user need. 

👉 Delete complete environment created. 

👉 Delete specific resources given by user. 


Note - There should be webUI based menu display so that user can get to know what your webapp can do. 

📌 This app will help the user to run all the Kubernetes commands.

Video Demo:- https://bit.ly/3w9jc1n


<b>DETAILED DESCRIPTION: </b>

This projects lets you run kubernetes command from the web browser even if you do not know the exact command.

-> Place the home3.html and the Color.gif files in /var/www/html/ directory and all the python files in /var/www/cgi-bin/ directory. [In RHEL8]

    Note: You may need to recreate all the python files and then convert then to executable using [chmod +x file_name] as 
    these python are already converted to executable file in our system and some settings may vary from system to system. 
    [Otherwise may or may not giving an Internal Server Error]

-> This project uses minikube VM for kubernetes services and RedHat 8 OS as the apache webserver host OS. [ In our case running on top of Virtual Box ].
You need to have the following setting in RedHat OS to configure the Web UI successfully

1. Have an apache server installed (yum install httpd)
2. disabe firewall [ Technically this step should be allowing various permisssions to public user however as this project is not security based so we used an unsecure round about way] (systemctl disable firewalld)
3.give apache root access through suoders (sudo gedit /etc/sudoers    :
  IN /etc/sudoers :
  
  
              ## Allow root to run any commands anywhere 
              
               root	ALL=(ALL) 	ALL

               apache  ALL=(ALL)       NOPASSWD: ALL
               
               
4. setenforce 0       [set SElinux mode from targeted to passive]



-> To use Your minikube VM as a client you need to copy the 'admin.conf' from sudo cd /etc/kubernetes/ [ minikube VM ] to sudo cd /root/.kube/ [RedHat 8 OS]
after renaming the file as 'config'.

You also need to change the server address in admin.conf file before renaming the file :

-----------------------------------------------------------------------------------------------------------------------------------

 IN 'admin.conf' :        change               
 
            server: https://control-plane.minikube.internal:8443   
            
                                  to          
                                  
            server: https://xxx.xxx.xxx.xxx:8443            [ xxx.xxx.xxx.xxx is the IP address of your minikube VM ]            
                                                                                                                                 
-----------------------------------------------------------------------------------------------------------------------------------
