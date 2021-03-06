## Pythonインストール

### pyenv install

pyenv インストール
```
$ brew install pyenv
```

環境変数の設定
```
$ vi ~/.zshrc or ~/.bashrc
--- 以下を記載
# Pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
---
$ source ~/.zshrc or ~/.bashrc
```

### python install

```
$ pyenv install 3.10.4
```
※ pyenvでインストールする前提としてXcodeをインストールしておく必要がある。  
→ pythonをビルドするため。


### pyvenv 設定

```
$ mkdir /path/to/workdir or git clone https://xxx(自分で作成したGitリポジトリ)
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

### pytest, pytest-cov, pytest-mock インストール

```
$ pipenv install -d pytest
$ pipenv install -d pytest-mock
$ pipenv install -d pytest-cov
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

# Python関連ドキュメント

* 公式ドキュメント：https://docs.python.org/ja/3/index.html
