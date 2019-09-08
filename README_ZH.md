```
  _____  _____  _     _ ______ _______    ______ _
 / ____|/ ___ \| |   | |  __  \__   __|  |  __  (_)
| |    | |   | | |   | | |__| |  | |     | |__| |_ ____    ___ _ __
| |    | |  _| | |   | |  ____/  | |     |  ____/ |  __ \ / _ \ '__\
| |___ | |__\  | |___| | |       | |     | |    | | |__| |  __/ |
 \____/ \____/\_\_____/|_|       |_|     |_|    |_|  ___/ \___|_|
                                                  |_|
```

![](https://img.shields.io/badge/build-passing-brightgreen) ![](https://img.shields.io/badge/license-MIT-blue) ![](https://img.shields.io/badge/Python-3%2B-yellowgreen)

🤯 CQUPT Piper 是一个 [重邮教务在线](jwzx.cqupt.edu.cn) 查询的命令行工具. (构建中)

## 安装

先确保您的设备上安装有 Python3+ 和 pip 工具

安装:

```bash
pip install CQUPTPiper
```

## 使用

Windows 的同学可打开 cmd 执行下面命令

MacOS 和 Linux 的同学随便您怎么搞

```bash
piper
```

第一次使用会先进行在校学生身份验证

验证成功后便可开始使用, 你可以执行 help 查看可使用的指令

### 获取信息

##### 获取你的照片

```bash
> get photo
```

##### 获取其他同学的照片

```bash
> get photo 2017213056
```

##### 获取当前学分统计数据

```bash
> get credit
```

##### 获取某一学年的学分

```bash
> get credit 2018
```

##### 获取某一学年的绩点和专业排名

```bash
> get gpa 2018
```

##### 获取某一学年学费

```bash
> get fee 2018
```

##### 获取当前学期考试安排

```bash
> get tasks
```





## Todo

- [x] **登录教务在线**
    - [x] 手动&自动识别验证码

- [ ] **获取信息**

## License

© XJJ, 2019~datetime.now()

Released under the [MIT License](https://github.com/Mivinci/cqupt-piper/blob/master/LICENSE)