# Notes: What to install

* [casey/just](https://github.com/casey/just)
* [pyenv](https://github.com/pyenv/pyenv)
* [poetry](https://python-poetry.org/)

```
brew install just
brew install pyenv

echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.10.0
pyenv local 3.10.0

curl -sSL https://install.python-poetry.org | python3

cat << EOF > poetry.toml
[virtualenvs]
in-project = true
system-packages = true
EOF

poetry init # creates pyproject.toml
poetry install
```
