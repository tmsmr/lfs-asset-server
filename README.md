# lfs-asset-server

## Dependencies
- https://pypi.org/project/GitPython/
- https://pypi.org/project/bottle/

## Test it
- Dummy asset store: https://github.com/opthomas-prime/lfs-asset-store
- Run: `./serve.py ../lfs-asset-store /tmp` (ensure `/tmp` is a tmpfs - gotta go fast)
- Measure: `hey http://localhost:880/assets/v4/aaa.asset -n 100 -c 10` (uses https://github.com/rakyll/hey)
