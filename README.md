简单的`demo`，`flask_demo`是一个`server`,任务函数在`tasks`
异步执行由`worker`完成
简单的异步任务就不用`celery`这么重的了

`go`可能更适合些

*Deploy*:
 - 安装：`sudo apt-get install python-virtualenv`
 - 开发环境：`ubuntu 14.04 64 LTS`
 - 克隆项目：`git clone https://github.com/yuzhiquan/flask_demo.git`
 - 搭建`env`：  
 ```bash
 cd flask_demo && virtualenv env && source env/bin/activate && pip install -r requirements.txt
 ```
 - 在虚拟环境下启动，包括`server`和`worker`:
 ```bash
 python worker.py
 python flask_demo.py
 ```
 
 - `Dockerfile`:待定
 
 
