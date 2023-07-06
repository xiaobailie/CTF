[NISACTF 2022]easyssrf

给了一个输入curl的界面

![](Aspose.Words.d1b9ccd7-f476-418c-acdc-65ef3c52903b.001.png)

随便写得到信息

![](Aspose.Words.d1b9ccd7-f476-418c-acdc-65ef3c52903b.002.png)

结合题目的ssrt

![](Aspose.Words.d1b9ccd7-f476-418c-acdc-65ef3c52903b.003.png)

访问这个文件

![](Aspose.Words.d1b9ccd7-f476-418c-acdc-65ef3c52903b.004.png)

审计发现有file\_get\_contents有ssrt漏洞

Payload：file=flag

![](Aspose.Words.d1b9ccd7-f476-418c-acdc-65ef3c52903b.005.png)

发现不行

Payload：file=../../..//flag

![](Aspose.Words.d1b9ccd7-f476-418c-acdc-65ef3c52903b.006.png)

<https://blog.csdn.net/Leaf_initial/article/details/130072727>

方法二：

https://cloud.tencent.com/developer/beta/article/2208167
