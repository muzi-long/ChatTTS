# ChatTTS服务端
[**ChatTTS的文档**](https://github.com/2noise/ChatTTS)
本项目对ChatTTS进行了修改，使其能够作为服务端运行。  
主要对外提供了一个API接口，以及一个demo页面
## 运行
### 最简单的运行方式
```bash
docker run -p 8889:8889 712120393/chattts:latest
```
启动后，程序会自动到huggingface上下载模型，并启动服务。

### 指定模型运行
可以设置环境变量MODEL_SOURCE，指定本地的模型。  
使用MODEL_PATH设置模型文件夹的路径（默认为:/app/models）。
```yaml
version: '3.8'

services:
  chattts:
    image: 712120393/chattts:latest
    ports:
      - "8889:8889"
    environment:
      - MODEL_SOURCE=local
    volumes:
      - ./models:/app/models
    deploy:
      resources:
        reservations:
          devices:
            - capabilities: [gpu]
    runtime: nvidia
```