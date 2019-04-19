# docker_with_ansible
docker with ansible

Instructions to execute playbooks as follows:-\
1. install_docker.yml@ 
   ansible-playbook install_docker.yml
2. launch_cont.yml@
   ansible-playbook launch_cont.yml -e "name=cont_name image=image_to_use"
3. start_cont.yml@
   ansible-playbook start_cont.yml -e "name=cont_name image=image_to_use"
4. stop_cont.yml@
   ansible-playbook stop_cont.yml -e "name=cont_name"
5. rm_cont.yml@
   ansible-playbook rm_cont.yml -e "name=cont_name"
6. volume_cont.yml@
   ansible-playbook volume_cont.yml -e "path=location_for_directory name=cont_name image=image_to_use"
7. multiple_cont.yml@
   ansible-playbook multiple_cont.yml -e "dir=directory_name name=cont_name image=image_name"
   
   Note:- volume dorectory is building under /mnt/

