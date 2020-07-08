# 基于DRF的RBAC组件

> 旨在为Django REST framework打造一个开箱即用的RBAC(基于角色的权限管理)系统

核心rbac模块来源于[rest_xops](https://github.com/xufqing/rest_xops)，本项目对其中的权限管理进行了剥离，在此基础上对drf的responce进行二次封装，实现兼容自定义的responce返回。



肺炎肆虐，在家整理的一个开源权限组件

## Getting Started 使用指南

### Prerequisites 项目使用条件

请确保安装以下python第三方库

```.env
[packages]
Django = "*"
djangorestframework = "*"
pillow = "*"
djangorestframework-jwt = "*"
django-filters = "*"
django-filter = "*"
pyyaml = "*"
django-simpleui = "*"

[requires]
python_version = "3.7"
```

### Installation 安装

后续将会给出docker镜像

### Usage example 使用示例

给出更多使用演示和截图，并贴出相应代码。

## Deployment 部署方法

目前均在测试环境中使用，部署到生产环境注意事项，请参照生产环境具体部署要求。

## Contributing 贡献指南

清阅读 [CONTRIBUTING.md](#) 了解如何向这个项目贡献代码

## Release History 版本历史

* 0.2.1
  * CHANGE: Update docs
* 0.2.0
  * CHANGE: Remove `README.md`
* 0.1.0
  * Work in progress

## Authors 关于作者

* **huangyongchi** - *Initial work* - [huangyongchi](https://huangyongchi.com)

查看更多关于这个项目的贡献者，请阅读 [contributors](#) 

## License 授权协议

这个项目 MIT 协议， 请点击 [LICENSE.md](LICENSE.md) 了解更多细节。
