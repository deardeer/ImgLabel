# ImgLabel

1. 下载imglib.tar.gz文件，解压放在<path-to-your>/ImgLabel的目录下
* <path-to-your>是你的ImgLabel所在的目录

2. 在<path-to-your>/ImgLabel的目录下，运行
python -m http.server XXXX
* XXXX是端口，比如20345

3. 在<path-to-your>/ImgLabel的目录下，运行
python tornado.server/server.py

4. 在浏览器打开http://localhost:XXXX
* XXXX是步骤2中设置的端口号

注意，成功运行起来后，联系我（尤其不要点nextimg这个按钮哦，如果点了这幅图像在数据库里就被标记了)
