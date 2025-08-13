USER
    the USER instruction is used to define the default user or gid when running the image. The RUN, CMD and ENTRYPOINT follow the USER instruction in the Dockerfile.
    usage:
        USER <user>[:<group]
        ex:
            FROM microsoft/windowservercore
            # Create Windows user in the container

            RUN net user/add patrick
            #set it for subsequent commands

            USER patrick
WORKDIR
    the WORKDIR instruction is used to define the default working directory of your docker image.
    the RUN, CMD, ENTRYPOINT, and ADD instructions follow the WORKDIR instruction.
    you can add multiple WORKDIR instruction on your Dockerfile, and if there it doesn't exist, it will be created automatically
    usage:
        WORKDIR /path/to/WORKDIR
        ex:
            ENV DIRPATH=/path
            WORKDIR $DIRPATH/$DIRNAME
            RUN pwd
EXPOSE
    this instruction is used to expose the container port on the specific network ports at runtime
    the default protocol exposed is TCP, but you can specify whether the TCP or UDP.
    usage:
        EXPOSE <port>
        EXPOSE [<port>/<protocol>]
        ex:
            EXPOSE 80/TCP