# Goal
provide a command line tool that can handle all deployment of local scripts onto remote servers, containers and pods
this tool should take care of all of the annoying devops
so that  when I"m working in the command line I can just keep typing

# syntax

``` bash

$ cd <projct-dir>
$ Dploy 
$ Dploy run <script-name> -arg1 val1 -arg2 val2
$ Dploy run <scrip-name> -s /path/to/script -arg1 val1 
```

### Dploy
- Dploy command may be used to deploy all files according to the deployment mapping

#### Options
--ssh, connect via ssh to remote

### Dploy run
- Dploy run may be used to run a script remotly and pipe in relevant logs and errors

#### Options
-s, --script: path to script to pass into remote and run before running remote script
-d, --debugger: path to debugger to pass into remote and pipe all output and errors back


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


