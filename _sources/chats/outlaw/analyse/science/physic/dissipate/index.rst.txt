Fluctuation-Dissipation Theorem
======================================

涨落-耗散定理是非平衡态统计物理学的核心基石之一（由赫伯特·卡伦和西奥多·维尔顿于1951年严格证明）。

它极其深刻地揭示了：系统局部的微观自发“涨落”（内部热运动），与系统在受到外部微小扰动时的“耗散/响应”（抵抗与吸收能力），在数理本质上是由同一种微观动力学机制决定的。

将其引入本案，并非主张将物理公式直接作为刑事证据，而是以该定理的因果边界、尺度分离与响应约束逻辑，
检验控方“微观转发→宏观秩序严重混乱”指控在统计物理与信息动力学层面的科学合理性，
进而完成刑法因果关系的客观证伪。

-------------------

 .. toctree::
    :maxdepth: 3

    grok
    gemini
    copilot
    chatgpt
    deepseek
    qwen

-----------------------

**涨落-耗散定理（Fluctuation–Dissipation Theorem, FDT）**

-----------------------

一句话直觉： **系统热平衡时的"自发涨落"有多大，决定了它在受到微扰后线性响应的"耗散/阻尼"有多大——反过来，测耗散就能反推出涨落。**

它是涨落理论里 **最可操作**、最常被拿来"连接理论与实验"的定理：

- **涨落** → 平衡态下观测量对其均值的无规起伏
- **耗散** → 系统对外力做功不可逆地转化为热的能力（阻尼、电阻、黏度等）

1. 最常用的一般性表述（线性响应框架）

考虑一个系统处于温度 :math:`T` 的热平衡，哈密顿量受外场微扰：

.. math::

    H(t)=H_0 - A\,F(t)

其中 :math:`A` 是系统中某个微观可观测量（比如磁化分量、极化、粒子数密度…），:math:`F(t)` 是共轭的外驱动（磁场、电场、化学势梯度…）。

线性响应关系:

对微扰 :math:`F(t)`，:math:`B` 的期望变化在线性阶为

.. math::

    \langle B(t)\rangle-\langle B\rangle_0=\int_{-\infty}^{t}\chi_{BA}(t-t')\,F(t')\,dt'

其中 :math:`\chi_{BA}` 是 **响应函数 / 广义极化率** （也叫 susceptibility kernel）。

涨落–耗散定理（经典，一般形式）

.. math::

    \chi_{BA}(\omega)=\frac{i}{\hbar}\bigl(1-e^{-\beta\hbar\omega}\bigr)\,S_{AB}(\omega)

或等价地更常用的实形式（经典极限 :math:`k_BT\gg\hbar\omega`）：

.. math::

    S_{AA}(\omega)\equiv\int_{-\infty}^{\infty} C_{AA}(t)\,e^{i\omega t}\,dt
    =\frac{2k_B T}{\omega}\,\operatorname{Im}\chi_{AA}(\omega)

其中

.. math::

    C_{AA}(t)=\langle A(t)A(0)\rangle_{\text{eq}}-\langle A\rangle_{\text{eq}}^2

是平衡态下 :math:`A` 的 **涨落自相关函数**。

2. 读这句公式到底在说什么

- 左边 :math:`S_{AA}(\omega)`： **平衡态自发涨落的功率谱** （不加外场也能测到的噪声谱）
- 右边 :math:`\operatorname{Im}\chi(\omega)`： **对外场的线性响应虚部** （决定吸收/耗散/阻尼的那个部分）

**物理含义**：

系统越容易被外场"拖着耗散能量"（:math:`\operatorname{Im}\chi` 大），它自己在平衡时就"抖得越厉害"（:math:`S(\omega)` 大），且比例由 :math:`k_B T` 固定。

这就是 **爱因斯坦关系 / 奈奎斯特定理 / 涨落–耗散定理** 在不同语境下的统一面孔。

3. 三个最经典的例子（最容易记住）


(a) 布朗粒子：摩擦 ↔ 扩散（爱因斯坦关系）

对悬浮粒子的速度  :math:`v` （一维）：

.. math::

    D=\mu\,k_B T,\qquad \mu=\frac{1}{\gamma}=\frac{1}{m\Gamma}

- **耗散**：摩擦系数 :math:`\gamma` （外力  :math:`F` 产生稳态漂移 :math:`v=\gamma^{-1}F`）
- **涨落**：扩散常数 :math:`D` （位移方差  :math:`\langle\Delta x^2\rangle=2Dt`）

写得更"FDT"一点：

.. math::

    \langle v(t)v(0)\rangle_{\text{eq}}\; \xrightarrow{\text{积分}/谱}\; D=\frac{k_B T}{\gamma}

(b) 电阻的热噪声：约翰逊–奈奎斯特噪声

两端开路电压涨落：

.. math::

    \langle\delta V^2\rangle = 4R\,k_B T\,\Delta f

- :math:`R=\operatorname{Re}Z(\omega)` （耗散部分）
- 噪声功率谱正比于 :math:`R\,k_B T`

这就是电路工程师天天用的 FDT 实例。

(c) 顺磁 / 介电极化：磁化率 ↔ 磁化涨落

.. math::

    \chi''(\omega)=\frac{\omega}{2k_B T}S_M(\omega)

测交流磁化率的虚部（吸收），就等价于知道了平衡态 :math:`M` 的涨落谱，反之亦然。

4. 适用条件（很重要，也是学生最常踩坑的地方）

涨落–耗散定理 **严格成立** 需要：

1. **系统处于热平衡** （或准平衡、细致平衡成立）
2. **线性响应区** （扰动足够小，线性近似有效）
3. 微扰–可观测量构成 **共轭对**  :math:`-A\,F` （以保证 Kubo 公式的起点）

超出这些条件就要小心：

- 强驱动、主动介质、生物系统、"远非平衡稳态"：一般 **FDT 被破坏**，需要修正因子（有效温度 :math:`T_{\text{eff}}(\omega)` 之类，但不是真正温度）
- 量子情形：零温仍有零点涨落，这时公式里的 :math:`(1-e^{-\beta\hbar\omega})` 因子不能约掉

5. 与"涨落–相变"关系的衔接

在相变附近（尤其是连续相变临界点），FDT 仍然成立（系统仍热平衡），但有趣的事发生了：

- 关联长度 :math:`\xi\to\infty` ⇒ 涨落 :math:`C(r)` 衰减极慢 ⇒ :math:`S(\omega)` 出现 **低频奇异性/幂律**
- 同时 :math:`\chi(\omega)` 的奇异性也由同一套临界指数控制

所以 **FDT 保证了：临界区"噪声有多疯"和"响应有多强"永远成对出现**，临界散射（涨落）与临界响应函数本质上是同一枚硬币的两面——这也是为什么实验上既可以用中子/X射线看散射（涨落），也可以用 susceptibility 看响应，两者互相校验。


---------------------------

Video Overview

-------------------

1. `统计物理学与法律因果关系 <https://youtu.be/BpKcio6x-1w>`_ 
2. `The Micro vs Macro Trap <https://youtu.be/t7YpHVrDqAw>`_ 
3. `物理、AI与法律因果：陈京元案解析 <https://youtu.be/s7pT3jMHPWI>`_ 
4. `跨越尺度的审判：统计物理视域下的因果谬误 <https://youtu.be/2FlgI923gYc>`_ 
5. `The Blueprint of Causality: Why Micro-Fluctions are Not Macro-Chaos <https://youtu.be/VuqlSWllcIY>`_ 
6. `法律因果的物理学：微观行为与宏观混沌 <https://youtu.be/b1TodGaND-8>`_ 
