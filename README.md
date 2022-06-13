## Pythonインストール

### pyenv install

```
$ brew install pyenv
```

### python install

```
$ pyenv install 3.10.4
```
※ pyenvでインストールする前提としてXcodeをインストールしておく必要がある。  
→ pythonをビルドするため。

### pyvenv 設定

```
$ mkdir /path/to/workdir
$ cd /path/to/workdir
$ pyenv local 3.10.4
$ python -m venv venv
$ source venv/bin/activate
```

### pipenv インストール

```
$ python -m pip install --upgrade pip
$ pip install pipenv
```

### flake8 インストール

```
$ pipenv install -d flake8
```

### pytest インストール

```
$ pipenv install -d pytest
```

## Python for VS Code

### VS Code の拡張機能をインストールする

Python関連
* Python (Microsoftが出しているやつ)
* Python Preview

視覚系
* indent-rainbow  
インデントを可視化
* ZenKaku  
全角スペースを可視化する
* Trailing Spaces  
行末スペースの可視化

整形系
* Python Indent
* flake8設定  
  設定の python.linting.flake8Enabled にチェックを入れる。

その他
* Markdown All in One
* Markdown PDF
