Installation Requirements

Execute the commands below to being able to run this project

* Install some required libraries:
<code>sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev libxml2-dev libxslt1-dev</code>

* Install and configure virtual enviromment
<code>
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
pyenv install 3.5.1
pyenv virtualenv 3.5.1 ponto-ivia-rest-env-3.5.1
pyenv activate ponto-ivia-rest-env-3.5.1 

pip install -r requirements.txt
</code>
