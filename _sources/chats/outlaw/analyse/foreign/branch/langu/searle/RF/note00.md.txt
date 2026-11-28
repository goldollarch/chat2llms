# 范畴论如何形式化证明符号接地问题

在哲学家路西亚诺·弗洛里迪（Luciano Floridi）、贾一扬（Yiyang Jia）与费尔南多·托梅（Fernando Tohmé）的研究论文 *《A Categorical Analysis of Large Language Models and Why LLMs Circumvent the Symbol Grounding Problem》* 中，作者利用 **范畴论（Category Theory）**与**抽象层（Level of Abstraction）** 方法，在关系范畴 $\mathbf{Rel}$ 中对符号接地问题（Symbol Grounding Problem）进行了严密的数理形式化证明。

其形式化证明的核心逻辑可以拆解为以下几个关键步骤：

---

### 一、 形式化框架与范畴构建

研究将分析置于**关系范畴 $\mathbf{Rel}$** 及其子范畴 $\mathcal{C}$ 中（对象为集合，态射为二元关系 $R \subseteq A \times B$），Hom-set 按子集包含关系（$\subseteq$）构成偏序结构（2-范畴）。

在子范畴 $\mathcal{C}$ 中，定义了如下核心认知对象与可能世界空间：

* **$H$**：人类认知与情境状态集合（包含背景知识、查询意图与情境）。
* **$C$**：人类创作的有意义文本/内容库。
* **$C'$**：Token 化后的机器可读数据流。
* **$G$**：训练好的模型权重参数空间（特定模型为 $g_0 \in G$）。
* **$O$**：模型生成的输出 Token 序列。
* **$W$**：物理客观现实与可能世界状态空间。
* **$\mathrm{Pred}(W) = \mathcal{P}(W)$**：关于可能世界 $W$ 的**命题空间（Propositions）**。

---

### 二、 人类认知路径 vs. AI 计算路径的态射图表对比

框架构建了一个对比图表，将从人类情境 $H$ 到命题空间 $\mathrm{Pred}(W)$ 的过程形式化为两条不同的复合态射：

#### 1. 人类认知路径（Upper Human Route）

复合态射为 $g \circ c : H \to \mathrm{Pred}(W)$：

* $c : H \to C$：人类查阅相关内容。
* $g : C \to \mathrm{Pred}(W)$：人类将内容解释为关于世界的命题，得到基准真理集 $P_{\mathrm{human}}(h) = (g \circ c)(h) \subseteq \mathrm{Pred}(W)$。
* **关键经验态射 $x : H \to W$**：**人类拥有直接的具身感知、物理因果与行动耦合映射 $x$（如看见雪的白色、感知苹果的重量），将认知状态 $H$ 直接锚定到客观物理现实 $W$ 上。**

#### 2. AI 计算路径（Lower AI Route）

复合态射为 $r \circ e \circ i_{g_0} \circ p : H \to \mathrm{Pred}(W)$：

* $p : H \to C'$：将用户情境转换为输入 Prompt（Token 序列）。
* $i_{g_0} : C' \to G \times C'$：将 Prompt 与固定参数模型 $g_0$ 配对。
* $e : G \times C' \to O$：模型进行概率采样并输出 Token 序列 $O$。
* $r : O \to \mathrm{Pred}(W)$：由外部人类用户将 Token 输出 $O$ 赋予语义解读，映射为命题集 $P_{\mathrm{AI}}(h) = (r \circ e \circ i_{g_0} \circ p)(h) \subseteq \mathrm{Pred}(W)$。

---

### 三、 形式化证明：为什么大模型是“绕过”而非“解决”符号接地？

通过对比两条复合态射路径，论文给出了大模型未能解决符号接地问题的三大数学与哲学证明：

1. **结构性缺失核心态射 $x : H \to W$**：
   在 AI 的计算路径中，推演完全发生在 $C \to C' \to G \times C' \to O$ 的数据与符号表征空间内，**完全不包含直接连接物理世界 $W$ 的经验态射 $x : H \to W$**。大模型缺乏与客观现实的直接感知、因果交互或规范性责任。
2. **认知寄生性与“借用”接地（Epistemic Parasitism）**：
   大模型之所以表现出“类似于理解”的能力，是因为其训练集 $D(C')$ 源自人类创作的内容库 $C$。而内容库 $C$ 中的文本早已由人类作者通过经验态射 $x$ 完成了预先接地（Pre-grounded Content）。**大模型学习到的只是人类描述世界的“二阶统计规律”（patterns in how humans describe patterns），而非世界本身的一阶物理规律。** 它继承了人类接地的果实，但系统自身并不具备接地能力。
3. **再引述（Re-quotation）与外部语义赋予**：
   根据塔斯基（Tarski）的去引述真理理论（Disquotation），人类能够跨出语言去比对现实 $W$。而大模型始终处于“被引述的环境”中，它做的是“再引述”（Re-quotation）——在符号层面重构统计模式。**将输出 Token 序列 $O$ 映射为命题 $\mathrm{Pred}(W)$ 的语义态射 $r : O \to \mathrm{Pred}(W)$，本质上是由外部人类使用者执行的，大模型本身只输出了无语义的字符串 $O$。**

---

### 四、 结论：蕴涵失败与“幻觉”的自然必然

在 2-范畴架构下，系统可靠性被定义为**蕴涵-弱交换性（Entailment-Commutativity）**：$P_{\mathrm{AI}}(h) \subseteq P_{\mathrm{human}}(h)$。

* **幻觉（Hallucination）被形式化定义为蕴涵失败（Entailment Failure）**：即存在命题 $p \in P_{\mathrm{AI}}(h)$ 但 $p \notin P_{\mathrm{human}}(h)$，导致 $P_{\mathrm{AI}}(h) \nsubseteq P_{\mathrm{human}}(h)$。
* **结论**：由于大模型缺失直接面向物理世界的态射 $x : H \to W$，仅靠在预接地的文本库 $C$ 上进行概率模式匹配，当统计推演偏离离散的真理边界时，产生蕴涵失败（幻觉）是该架构“绕过接地”策略下的**内禀结构性特征，而非可以通过简单技术修补消除的工程 Bug**。

---

💡 这种范畴论证明表明大语言模型本质上是高效的信息中介而非知识主体。你是否想了解论文中如何用这套图表进一步证明“即使引入多模态或 RAG 检索增强，依然无法从本体论上解决符号接地”？
