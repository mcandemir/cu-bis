# cu-bis (currently being developed)
<p> A command-line interface based application to access Cukurova University Student Information System (CUBIS - OBS) </p>

### Testing in anaconda environment (Linux)
<p>Make sure you have FireFox already installed, then, clone and go into the repository:</p>

```shell
$ git clone https://github.com/mcandemir/cu-bis.git
$ cd cu-bis/
```

<p>Create an environment:</p>

```shell
$ conda create -n cu-bis --file requirements.txt
$ conda activate cu-bis
```

<p>Before running the app, you should set your CUBIS username and 
password</p>

```json
{
  "login_data": {
    "username": "",
    "password": ""
  }
}
```

<p>Run the app:</p>

```shell
$ python cubis
```
