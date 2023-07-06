[NISACTF 2022]checkin

打开后发现是简单的get

![](Aspose.Words.da13b22e-7316-417c-b536-caa0679b1581.001.png)

Payload后不会输出flag，但是在复制是发现问题

![](Aspose.Words.da13b22e-7316-417c-b536-caa0679b1581.002.png)

选中了nis后面的flag也一起被选中了发现脏东西

用winhex打开原🐎

![](Aspose.Words.da13b22e-7316-417c-b536-caa0679b1581.003.png)

发现第一个haha是正常的第二个cui乱码发现脏东西

将第二个参数的16进制复制出来转url拼接

![](Aspose.Words.da13b22e-7316-417c-b536-caa0679b1581.004.png)

传入得flag

分析：E2 80 AE E2 81 A6

对于这个特殊字符，它是Unicode编码U+202E转UTF-8对应的十六进制编码

它的名字叫做**从右往左强制符**

它的作用就是：根据内存顺序**从右至左**显示字符

![](Aspose.Words.da13b22e-7316-417c-b536-caa0679b1581.005.png)

