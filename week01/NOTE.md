学习笔记

## logging

> python 的日志记录工具

#### 日志级别

- info
- warning
- error
- debug
- critical

#### 配置

- `logging.basicConfig`(***kwargs*)

  常用键字参数：

  ​	filename：使用指定的文件名而不是 StreamHandler 创建 FileHandler

  ​	datefmt：使用指定的日期/时间格式，与 `time.strftime()` 所接受的格式相同。

  ​	level： 设置根记录器级别去指定。

- LogRecord 属性

  ​	asctime

  ​	levelname

  ​	lineno

  ​	message