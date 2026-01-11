rm -rf ./dist/* ./build/*

# 从 .pypirc 读取 token
TOKEN=$(grep -A2 '\[pypi\]' ~/.pypirc | grep password | sed 's/.*= *//')

uv build
uv publish --token "$TOKEN"

