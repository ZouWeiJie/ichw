## 1. 用你的语言描述图灵为什么要证明停机问题, 其证明方法和数学原理是什么.
### 图灵证明停机问题是为了说明计算机并不是万能的，一切程序都必须合乎逻辑
### 证明方法：运用了对角线方法（反证法）
### 假设存在程序A，A可以判断任何一个程序在给定输入下是否会停机。
### 假设有某一程序B，在B中输入某一程序C，若C被A判定为会停机，则B不会停机，倘若C被判定为不会停机，则B会停机。
### 这时，我们假设输入B的程序是B，则会出现下面的情况：
### 若B被判定为会停机，则被输入程序B的B不会停机，矛盾；
### 若B被判定为不会停机，则被输入程序B的B会停机，矛盾。
### 得证！
### 数学原理：哥德尔不完备性定理
### 任意一个包含一阶谓词逻辑与初等数论的形式系统，都存在一个命题，它在这个系统中既不能被证明为真，也不能被证明为否。
## 2. 你在向中学生做科普，请向他们解释二进制补码的原理.
### 二进制补码：补码解决了反码存在的问题，即可使计算机顺利地通过加法运算来进行减法。
### 其原理如下所述：我们在进行某一计算时（背景：该组计算中每一个数不得大于或等于16，倘若某一数大于16，则用其减去16，不断进行该操作，直到得到一个小于16的数），十进制计算中，15+9=24，而在这里15+9=8，一般理解为15+9-16=8，而我们也可利用二进制补码的原理，即先将16-9=7，再用15-7=8，总的可以写成如下：15-（16-9）=8
### 我们举一例进行运算：在8位代码中，将十进制数-15转化为二进制补码，首先，将（-15）取绝对值，得15，之后，将15转化为二进制00001111，将每一位取反，得到取反后的代码11110000，11110000+00001111=11111111，00001111+（11110000+00000001）=00000000，因此（-15）的二进制补码可表示为11110001
## IEEE 754
### 0：*0000 0000 000 0000
### ±1.0： *0111 1111 000 0000
### 最大非规范数： *0000 0000 111 1111
### 最小非规范数： *0000 0001 000 0000
### ±∞： 1111 1111 0000 0000
### NaN： *1111 1111 non zero