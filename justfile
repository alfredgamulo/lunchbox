_:
    @just -l -u --list-heading $'Lunchbox 🍱\n'

# Install poetry
install:
    poetry install

# Whoami?
intro:
    @poetry run python -m intro

alpha *args:
    @poetry run alpha {{args}}

bravo *args:
    @poetry run bravo {{args}}

charlie *args:
    @poetry run charlie {{args}}

delta *args:
    @poetry run delta {{args}}

compile:
    poetry run python -m nuitka lunchbox/delta/main.py -o lunchbox-portable --static-libpython=no --standalone --onefile --assume-yes-for-downloads --include-package-data=* --remove-output
    chmod +x lunchbox-portable
    export PATH=$PWD/:$PATH
