# 多模态具身智能绕过符号接地问题

在哲学家路西亚诺·弗洛里迪（Luciano Floridi）、贾一扬（Yiyang Jia）与费尔南多·托梅（Fernando Tohmé）2025年的研究论文 *《A Categorical Analysis of Large Language Models and Why LLMs Circumvent the Symbol Grounding Problem》* 中，作者引入了 **范畴论（Category Theory）**与**抽象层（Level of Abstraction）** 方法，在关系范畴 $\mathbf{Rel}$ 中对人类与 AI 的认知路径进行了严密的数学形式化建模 [i: 2, 5, 6]。

这套形式化框架精准地证明了：**即使将大语言模型扩展为多模态或具身智能（Embodied AI），系统依然是在表征层（Content Layer $C$）内部做符号与数据的协变关联，并没有建立直接面向物理现实（Possible Worlds $W$）的经验映射，因而在本体论上依然是“绕过”（Circumvent）而非“解决”了符号接地问题** [i: 2, 8, 68, 73]。

---

### 一、 关系范畴 $\mathbf{Rel}$ 与子范畴 $\mathcal{C}$ 的形式化定义

该分析建立在**关系范畴 $\mathbf{Rel}$** 之上（对象为集合，态射为二元关系 $R \subseteq A \times B$） [i: 8, 9, 88]。之所以选择 $\mathbf{Rel}$，是因为解释、提示词生成与概率推理本质上是“一对多”或随机的二元关系 [i: 10, 89]。

在子范畴 $\mathcal{C}$ 中，定义了如下核心对象（Sets）：

* $H$：人类认知与情境状态集合（包含背景知识、查询意图等） [i: 10, 29]。
* $C$：人类创作的语义内容库（文本、图表等） [i: 10, 30]。
* $C'$：Token 化后的机器可读数据流（文本 Token、像素 Token、传感器 Token） [i: 10, 30]。
* $G$：已训练模型的参数权重空间（特定模型记为 $g_0 \in G$） [i: 10, 31]。
* $O$：模型生成的 Token 输出序列 [i: 10, 32]。
* $W$：相关可能世界或物理状态空间（真实物理现实） [i: 10, 32]。
* $\mathrm{Pred}(W) = \mathcal{P}(W)$：可能世界 $W$ 的幂集，代表关于世界 $W$ 的**命题空间（Propositions）** [i: 10, 33]。

---

### 二、 态射图表（Morphism Diagram）：人类路径与 AI 路径的对比

框架将认知过程形式化为从人类情境 $H$ 到命题空间 $\mathrm{Pred}(W)$ 的复合态射映射 [i: 11, 18, 35]：

```
                    c               g
         H ─────────────────> C ───────────> Pred(W)
         │                    │                 ▲
         │ x (经验)           │ s (Token化)     │
         ▼                    ▼                 │ r (人类解释)
         W                   C' ───────────> O ─┘
                                   i_g0 ∘ e
```

#### 1. 人类认知路径（Upper Human Route）

复合态射为 $g \circ c : H \to \mathrm{Pred}(W)$ [i: 13, 18, 36]。

* $c : H \to C$：人类查阅并检索相关内容 [i: 12, 18, 36]。
* $g : C \to \mathrm{Pred}(W)$：人类将内容解释为关于世界的命题，得到基准真理集 $P_{\mathrm{human}}(h) = (g \circ c)(h) \subseteq \mathrm{Pred}(W)$ [i: 12, 18, 36]。
* **关键经验态射 $x : H \to W$**：**人类拥有直接的具身感知、物理因果与行动耦合映射 $x$（例如看见雪的白色、感知苹果的甜味） [i: 12, 18, 26, 54]。该态射直接将认知状态 $H$ 连接到物理世界 $W$ [i: 18, 26, 54]。**

#### 2. AI 计算路径（Lower AI Route）

复合态射为 $r \circ e \circ i_{g_0} \circ p : H \to \mathrm{Pred}(W)$ [i: 13, 18, 36]。

* $p : H \to C'$：将用户需求转换为输入 Prompt（Token 序列） [i: 12, 18, 36]。
* $i_{g_0} : C' \to G \times C'$：将 Prompt 与固定参数模型 $g_0$ 配对 [i: 12, 18, 36]。
* $e : G \times C' \to O$：模型进行概率推理采样，输出 Token 序列 $O$ [i: 12, 18, 36]。
* $r : O \to \mathrm{Pred}(W)$：**由外部人类用户将 Token 输出 $O$ 赋予语义解读，映射为命题集 $P_{\mathrm{AI}}(h) = (r \circ e \circ i_{g_0} \circ p)(h) \subseteq \mathrm{Pred}(W)$ [i: 12, 18, 36, 62]。**

---

### 三、 2-范畴下“弱交换性”（Lax Commutativity）与可靠性推导

在 $\mathbf{Rel}$ 范畴中，如果将 Hom-set 按子集包含关系（$\subseteq$）赋予偏序结构，$\mathbf{Rel}$ 便构成了一个 **2-范畴（2-Category）** [i: 13, 14, 89, 90]。其中：

* **0-cells**：对象（$H, C', O, \mathrm{Pred}(W)$ 等） [i: 14]。
* **1-cells**：态射关系（如 $p, g \circ c$） [i: 14]。
* **2-cells（变换）**：子集包含关系 $\subseteq$ [i: 14]。

图表的交换性并非传统的严格相等（$\text{AI 路径} = \text{人类路径}$），而是定义为**蕴涵-弱交换性（Entailment-Commutativity）** [i: 13, 14, 20, 90]：

$$\forall h \in H, \quad P_{\mathrm{AI}}(h) \subseteq P_{\mathrm{human}}(h)$$

* **可靠/非幻觉集（Soundness Set $H^*$）**：当 $P_{\mathrm{AI}}(h) \subseteq P_{\mathrm{human}}(h)$ 成立时，AI 输出的命题完全被人类基准真理所蕴涵 [i: 20, 38]。
* **幻觉（Hallucination / Entailment Failure）**：当蕴涵失败，即 $P_{\mathrm{AI}}(h) \nsubseteq P_{\mathrm{human}}(h)$ 时，存在命题 $p \in P_{\mathrm{AI}}(h)$ 但 $p \notin P_{\mathrm{human}}(h)$ [i: 23, 39, 49, 50]。

---

### 四、 为什么多模态/具身智能依然在 $C$ 内部“绕过”符号接地？

论文运用这套态射图表，对多模态模型（视觉-语言大模型 VLM）和具身机器人进行了严格的形式化证明，揭示了其为何无法突破封闭系统 [i: 66, 68, 72, 73]：

#### 1. 传感器信号本质上依然是 $C'$ 层的 Token 序列

当给大模型接入摄像头（像素）、听觉或机械臂触觉传感器时，这些外部输入在数字架构中**必须先被离散化编码为多模态 Token 或高维向量，其分类依然属于 $C'$（或表征层 $C$ 的延伸）** [i: 68, 73]。
多模态训练的形式化复合关系为：

$$t \circ D \circ s : C_{\text{text}} \times C_{\text{vision}} \longrightarrow G$$

其处理过程本质上是在文本 Token 与图像/传感器 Token 之间建立二阶统计协变（Second-order Regularities） [i: 58, 68]。

#### 2. 映射图表缺失核心态射 $x : H \to W$

在具身智能的态射链路中：

$$\text{传感器/环境} \longrightarrow C' \xrightarrow{\quad e \quad} O \xrightarrow{\quad r \quad} \mathrm{Pred}(W)$$

* 模型学习的是“摄像头像素 Token（如红色的像素簇）”与“文本 Token（如‘苹果’）”之间的模式对齐 [i: 68]。这种映射发生在 $C' \to C'$ 内部 [i: 68]。
* **它依然完全缺失了直接连接认知主体与物理现实的经验态射 $x : H \to W$（真正的具身感知、物理因果与社会规范责任）** [i: 58, 62, 68]。它处理的是“人类捕获并编码好的图像与数据表征”，而非物理世界 $W$ 本身 [i: 68, 73]。

#### 3. 语义映射 $r$ 依然由外部人类赋予

在图表中，将输出 Token $O$ 转换为命题 $\mathrm{Pred}(W)$ 的态射 $r : O \to \mathrm{Pred}(W)$ **并不是由 AI 内部执行的，而是由外部人类观察者/使用者完成的** [i: 12, 18, 62, 75]。
机器人机械臂抓取杯子的行为，是由内部代码驱动的物理运动，其“抓取”这一符号的语义约束，依然依赖于人类使用者对该动作赋予的社会与功能解读 [i: 66, 75]。

#### 4. 寄生性意向与“借用”接地（Epistemic Parasitism）

范畴论图表清晰地展示了：AI 能够表现出高度“类似于理解”的行为，是因为它训练所依赖的内容库 $C$（以及多模态数据集）**已经被人类作者通过 $x : H \to W$ 完成了预先接地（Pre-grounded Content）** [i: 31, 52, 54, 57, 64]。
多模态与具身智能只是通过扩展输入模态，极大地提高了对 $C$ 库中高维几何结构的重构与再引述（Re-quotation）效率，**它继承了人类接地的果实，但系统自身并未拥有接地能力** [i: 61, 64, 67, 69]。

---

### 总结

从范畴论的图表推导来看：**多模态与具身智能只是丰富了数据表征层（扩大了 $C$ 与 $C'$ 的维度），但并没有在 AI 路径中新增一条直接通往物理世界 $W$ 的经验态射 $x$ [i: 58, 68, 73]。因此，它只是在更高维度的符号空间中实现了更精致的“符号接地绕过”（Circumvention）** [i: 2, 8, 68, 69]。

---

🔍 这一范畴论形式化推导在哲学的“真理解释”（如 Tarski 的去引述理论与 Sellars 的理由空间）中同样引发了深刻反响，你想探讨一下这套模型如何从语义学角度解释“大模型为什么只能做‘再引述’（Re-quotation）而无法做‘去引述’（Disquotation）”吗？
