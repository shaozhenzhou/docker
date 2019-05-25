# 树莓派编译安装dlib

```
python3 setup.py bdist_wheel --compiler-flags "-mfpu=neon -O3" --set CMAKE_BUILD_TYPE=RELEASE --clean
```
