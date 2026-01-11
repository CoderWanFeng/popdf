pip3.11 freeze > allpackages.txt
pip3.11 uninstall -r allpackages.txt -y
pip install twine pytest
