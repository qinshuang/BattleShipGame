#!usr/bin/env python
# -*- coding:utf-8 -*-

import io
import os
import sys
from setuptools import find_packages, setup, Command

# 包的元信息
NAME = 'BattleShipGame'
DESCRIPTION = '项目的简短描述，不超过200字符'
URL = 'https://github.com/qinshuang/BattleShipGame'
EMAIL = 'qinshuang_11@163.com'
AUTHOR = 'qinshuang'
REQUIRES_PYTHON = '>=2.7,<3.0'
VERSION = '0.1.0'
KEYWORDS = 'sample setuptools development'

# 项目依赖，也就是必须安装的包
REQUIRED = [
    'Flask==1.0.2',
    'flask-restplus==0.12.1',
    'flask_sqlalchemy',
    'flask_jwt_extended',
    'flask_script',
    'flask_migrate',
    'pyyaml',
    'flask_marshmallow',
    'marshmallow-sqlalchemy',
    'mysqlclient',
]

# 项目的可选依赖，可以不用安装
EXTRAS = {
    # 'fancy feature': ['django'],
}

# 剩下部分不用怎么管 :)
# ------------------------------------------------
# 除了授权和授权文件标识符!
# 如果你改了License, 记得也相应修改Trove Classifier!

here = os.path.abspath(os.path.dirname(__file__))

# 导入README文件作为项目长描述.
# 注意 这需要README文件存在!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except BaseException:
    long_description = DESCRIPTION

# 当前面没指定版本号的时候，将包的 __version__.py 模块加载进来
about = {}
if not VERSION:
    with open(os.path.join(here, '__version__.py')) as f:
        exec (f.read(), about)
else:
    about['__version__'] = VERSION

# 神奇的操作，一个函数完事
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    keywords=KEYWORDS,
    # 项目中要包括和要排除的文件，setuptools可以自动搜索__init__.py文件来找到包

    packages=['BattleShipGame',
              'BattleShipGame.apiv1',
              'BattleShipGame.apiv1.users',
              'BattleShipGame.commons',
              ],
    # package_dir={NAME:''},
    # 如果项目中包含任何不在包中的单文件模块，需要添加py_modules让setuptools能找到它们:
    # py_modules=['yitian_first_package'],
    # data_files=['BattleShipGame/logging.yml','BattleShipGame/private.key'],
    entry_points={
        'console_scripts': ['bsgd=BattleShipGame.manage:command_line'],
    },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    # 老旧的distutils需要手动添加项目中需要的非代码文件，setuptools可以用下面参数自动添加(仅限包目录下)
    include_package_data=True,
    # 如果是包的子目录下，则需要手动添加
    # package_data={
    #     'yitian_first_package': ['static/*.html']
    # },
    license='MIT'
)
