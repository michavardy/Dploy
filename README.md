# Goal
provide a command line tool that can handle all deployment of local scripts onto remote servers, containers and pods
this tool should take care of all of the annoying devops
so that  when I"m working in the command line I can just keep typing

# syntax

``` bash

$ cd <projct-dir>
$ Dploy init                                                    # copies .Dploy/DployConfig.toml
$ Dploy sync                                                    # sync's directory or sub-directory according to mapping
$ Dploy run                                                     # runs a script remotely, pipes in stdout, stderror
$ Dploy run -p /path/to/script                                  # runs a script remotely, using path 
$ Dploy run -a  {-arg1:val1, -arg2:val2}                        # runs a script remotely, with explicite arguments
$ Dploy run -c (optional) /path/to/.DployConfig.toml            # runs a configured script remotely from .Dploy/DployConfig.toml
$ Dploy run -l /path/to/log/src /path/to/log/dst                # runs a script remotely, pipes in log
$ Dploy run -i                                                  # runs a script remotely, pipes in interactive ipython console
$ Dploy run -d                                                  # runs a debugger remotely, pipes in debug output, must be configured from .Dploy/DployConfig.toml
$ Dploy run -r                                                  # runs a script remotely, ssh into script, leaves user in remote environment
```

### Dploy init
- copies .Dploy/DployConfig.toml into project directory

#### Dploy sync
- syncs directory or sub-directory according to mapping listed in DployConfig.toml
- if the directory is not in the mapping, a warning will be displayed on screen
- if a sub-directory is synced thats ancestors are mapped, the program will:
    - search from sub-directory until project directory
    - determine if an ancestor is mapped
    - adopt ancestor mapping

### Dploy run
- runs a script remotely, pipes in stdout, stderror

#### Options
-p, --path: include specific path to file
-a, --args: include an arguments key value pair, or dictionary
-c, --configured: runs a configured script remotely from .Dploy/DployConfig.toml
-l, --log: pipes in logs from src to dst
-i, --ipython: pipes in interactive ipython console
-d, --debugger: runs a remote debugger, pipes in debug output, must be configured from .Dploy/DployConfig.toml
-r, --remote: runs a script remotely, ssh into script, leaves user in remote environment

### DployConfig.toml
- a deploy config must be present in the project-dir in order to use Dploy command

#### fields
- meta
    - name
    - email
    - git-remote
- project
    - name
    - deployment.name
    - deployment.client.name
    - deployment.client.credentials.username
    - deployment.client.credentials.passphrase
    - deployment.client.ip
    - deployment.mapping
    - interpreter.path
    - logger.conf
    - logger.out


