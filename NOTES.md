```
brew install just
brew install pyenv

echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

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
