1.
yum install MySQL-python
2.Dcokerfile docker-compose ../
3.stop up status containers
    docker ps -a | grep 'Up' | awk '{print $1}'| xargs docker container stop
4.rm Exited status containers
    docker ps -a | grep 'Exited' | awk '{print $1}'| xargs docker container rm
5.rm none images
    docker image ls | grep none | awk '{print $3}' | xargs docker image rm
GG
