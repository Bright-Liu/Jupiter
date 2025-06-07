# Python Study

## 常用操作命令
### 环境管理

|命令|说明|
|:----|:----|
|conda create --name myenv python=3.9	|创建名为 myenv 的 Python 3.9 环境|
|conda activate myenv	|激活环境（命令行前缀显示 (myenv)）|
|conda deactivate	|退出当前环境|
|conda env list	|查看所有环境|
|conda remove --name myenv --all	|删除环境|

### 包管理

|命令|说明|
|:----|:----|
|conda install numpy pandas	|安装多个包（自动解析依赖）|
|conda install tensorflow-gpu=2.6.0	|安装指定版本包|
|conda list	|查看当前环境的已安装包|
|conda update numpy	|更新单个包|
|conda update --all	|更新所有包|
|conda remove numpy	|卸载包|

### 环境导出与重建

```bash
# 导出环境配置（生成 environment.yml）
conda env export > environment.yml

# 根据 YAML 文件重建环境
conda env create -f environment.yml
```

## 高效使用技巧
### 加速下载
配置清华镜像源：
```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes
```

### 混合使用 Conda + Pip
优先用 `Conda` 安装（能更好处理 `C` 库依赖），次选用 `Pip`：
```bash
conda install numpy
pip install torch torchvision  # 当Conda源无此包时
```

### 环境克隆（复制已有环境）
```bash
conda create --name new_env --clone old_env
```

## 常见问题解决

### Conda 命令不可用
检查环境变量：`Path` 中是否包含 `C:\Miniconda3\Scripts` 和 `C:\Miniconda3\Library\bin`

### 安装包冲突
尝试用 `conda install --channel conda-forge package_name（社区源通常更全）`

### 清理缓存
```bash
|conda clean -y --all  # 删除所有缓存包
```