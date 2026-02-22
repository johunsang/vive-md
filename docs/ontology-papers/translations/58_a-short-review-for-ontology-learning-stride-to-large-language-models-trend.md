# [58] 온톨로지 학습의 LLM 전환 동향 단기 리뷰

- 영문 제목: A Short Review for Ontology Learning: Stride to Large Language Models Trend
- 연도: 2024
- 원문 링크: https://doi.org/10.48550/arXiv.2404.14991
- DOI: 10.48550/arxiv.2404.14991
- 원문 저장 상태: pdf_saved
- 원문 파일: /Volumes/SAMSUNG/apps/projects/vive-md/docs/ontology-papers/originals/58_a-short-review-for-ontology-learning-stride-to-large-language-models-trend.pdf
- 번역 상태: partial_translated

## 원문(추출 텍스트)

A S HORT REVIEW FOR ONTOLOGY LEARNING : S TRIDE TO
LARGE LANGUAGE MODELS TREND
Rick Du, Huilong An, Keyu Wang
BSH Home Appliances Holding (China) Co., Ltd
{Rick.Du, Huilong.An, Keyu.Wang}@bshg.com
Weidong Liu
Department of Computer Science and Technology, Tsinghua University
liuwd@tsinghua.edu.cn
ABSTRACT
Ontologies provide formal representation of knowledge shared within Semantic Web applications.
Ontology learning involves the construction of ontologies from a given corpus. In the past years,
ontology learning has traversed through shallow learning and deep learning methodologies, each
offering distinct advantages and limitations in the quest for knowledge extraction and representation.
A new trend of these approaches is relying on large language models (LLMs) to enhance ontology
learning. This paper gives a review in approaches and challenges of ontology learning. It analyzes
the methodologies and limitations of shallow-learning-based and deep-learning-based techniques for
ontology learning, and provides comprehensive knowledge for the frontier work of using LLMs to
enhance ontology learning. In addition, it proposes several noteworthy future directions for further
exploration into the integration of LLMs with ontology learning tasks.
1 Introduction
Extraction and organization of meaningful conceptual knowledge have been central to the pursuit of enhancing machine
comprehension and reasoning capabilities [1]. Ontology learning, a fundamental cornerstone within this domain, is
tasked with the extraction, representation, and refinement of structured ontologies that encapsulate the intricacies of
various domains [2].
In the past years, ontology learning has traversed through shallow learning and deep learning methodologies, each
offering distinct advantages and limitations in the quest for knowledge extraction and representation [ 3]. Shallow
learning techniques, characterized by their simplicity and ease of implementation, have long been the bedrock of
ontology learning [4]. These methods, albeit effective in certain contexts, often grapple with challenges of scalability
and the extraction of nuanced and complex relationships between entities. Conversely, the advent of deep learning
techniques has heralded a new era, promising more intricate representations and enhanced discernment of underlying
patterns within data. However, deep learning techniques come burdened with their own set of limitations, including the
voracious appetite for large volumes of annotated data and computational resources [5].
Amidst this landscape, the emergence of large language models stands as a disruptive force, reshaping the contours
of ontology learning [6, 7]. These models, leveraging the prowess of pre-trained language representations, exhibit a
remarkable aptitude for understanding semantic nuances, capturing context, and inferring relationships among entities
[6, 7, 8, 9]. Their applications in ontology learning holds the promise of addressing longstanding challenges by
harnessing the inherent linguistic and conceptual understanding embedded within these models.
The purpose of this paper is to give a review in approaches and challenges of ontology learning in LLMs era. It presents
the methods and analyzes the limitations of shallow-learning-based and deep-learning-based techniques, and provides
comprehensive knowledge for the current work of using LLMs to enhance ontology learning. In addition, it proposes
several noteworthy future directions for further exploration into the integration of large language models with ontology
arXiv:2404.14991v2  [cs.IR]  17 Jun 2024

learning tasks. The rest of this paper is organized as follows: Section 2 defines ontology, ontology learning, and
summarises the challenges of ontology learning. Section 3 presents the ontology learning approaches based on shallow
learning and deep learning, as well as their limitations. Section 4 presents how large language models contributes to
ontology learning procedure recently, and discusses the potential of using large language models to facilitate ontology
learning. Section 5 proposes several future directions for further exploration into using large language models to
enhance ontology learning. Finally, we conclude in Section 6.
2 Ontology Learning
2.1 Ontology
In general, an ontology describes formally a domain of discourse. Typically, an ontology consists of terms and the
relationships between these terms, where the terms denote important concepts of the domain [10]. An ontology must
be formal and machine-readable, allowing it to serve as a shared vocabulary across different applications. Formally,
ontology can be described as following tuple [11]:
O =< C, H, R, A > (1)
where O represents ontology, C represents a set of classes (concepts), H represents a set of hierarchical links between
the concepts (taxonomic relations), R represents a set of conceptual links (non-taxonomic relations), and A represents a
set of rules and axioms.
2.2 Ontology Learning
Ontology learning (OL) from text involves the construction of ontologies from a given corpus of text [12, 13]. According
to ontology learning layer cake shown in Figure 1 proposed by [14], which is widely held as cornerstone in OL [15],
the process of OL from text can be divided into six sub-tasks as following:
Terms
Synonyms
Concepts
Concept Hierarchies
Relations
Rules
disease, illness, hospital
{disease, illness}
DISEASE ≔< 𝐼, 𝐸, 𝐿 >
𝑖𝑠_𝑎(𝐷𝑂𝐶𝑇𝑂𝑅, 𝑃𝐸𝑅𝑆𝑂𝑁)
𝑐𝑢𝑟𝑒(𝑑𝑜𝑚: 𝐷𝑂𝐶𝑇𝑂𝑅, 𝑟𝑎𝑛𝑔𝑒: 𝑃𝐸𝑅𝑆𝑂𝑁)
∀𝑥, 𝑦(𝑚𝑎𝑟𝑟𝑖𝑒𝑑 𝑥, 𝑦 → 𝑙𝑜𝑣𝑒(𝑥, 𝑦)
Figure 1: Ontology Learning Layer Cake [14]
1. Term extraction: This initial step involves identifying relevant terms or entities from a given text or dataset.
These terms serve as the building blocks for constructing an ontology.
2. Synonym extraction: Synonyms are different terms referring to the same concept. In ontology learning,
identifying synonyms is crucial for ensuring comprehensive coverage and avoiding redundancy.
3. Concept formation: Once terms and their synonyms are extracted, the next step is to group them into
meaningful concepts or classes. This involves organizing related terms into hierarchies or categories based on
their similarities, functionalities, or semantic relations.
2

4. Taxonomic relation extraction: Taxonomic relations establish hierarchical relationships between concepts,
defining the "is-a" relationship (e.g., "car" is a "vehicle"). Ontology learning involves identifying and
structuring these hierarchical relationships to arrange concepts in a taxonomy or ontology hierarchy.
5. Non-taxonomic relation extraction: Unlike taxonomic relations, non-taxonomic relations capture various
associations between concepts beyond hierarchical relationships. These relations could be "part-of," "has-
property," or other associative connections that enrich the ontology’s expressiveness.
6. Rule or axiom extraction: Rules or axioms define constraints, dependencies, or logical relationships between
entities or concepts in the ontology. Extracting rules or axioms aims to formalize domain knowledge and
establish logical constraints within the ontology.
Generally, the ontology learning process follows the aforementioned steps. However, it is not uncommon for some
ontology learning processes only partially complete the six steps outlined above according to different needs. Ontology
learning methods can be roughly divided into the following three categories [16, 17, 18, 19]:
• Manual: Ontologies are developed through a process that heavily relies on human expertise and intervention.
Examples are Gene Ontology (GO) [ 20], WordNet [ 21], SNOMED CT (Systematized Nomenclature of
Medicine—Clinical Terms) [22], Cyc [23], and Foundational Model of Anatomy (FMA) [24].
• Semi-automatic: The development of ontologies is facilitated and streamlined by integrating automated
processes with human input. There are various available tools for such a purpose, like Text2Onto [ 25],
OntoGen [26], and OntoStudio [27].
• Fully automatic: The system takes care of the complete construction, without any manual intervention. While
the idea of fully automatic ontology construction is appealing, especially for handling large volumes of data or
complex domains, it is worth mentioning that full automatic construction for ontology by a system is still a
significant challenge and it is not likely to be possible [28, 29, 30].
2.3 Challenges in Ontology Learning
Ontology learning, despite its advancements, still encounters various challenges. Below is a list highlighting the key
aspects that characterize the primary challenges in ontology learning:
Labor intensiveness: Ontology construction often involves significant manual effort. Identifying, extracting, and
structuring knowledge from diverse sources demands extensive human intervention. This labor-intensive process
can be time-consuming and resource-intensive, hindering the scalability and efficiency of ontology development
[15, 31, 32, 14].
Axiom formulation: Formulating precise axioms or rules that accurately represent domain knowledge poses a
challenge. Balancing expressiveness with computational efficiency is crucial. Axioms must be meaningful and precise
to contribute effectively to the ontology’s utility. This demands specialized expertise and often involves iterative
refinement [33, 31, 32].
Domain-specific knowledge acquisition: Acquiring and representing domain-specific knowledge within the ontology
is challenging. Understanding and capturing intricate domain nuances, concepts, and relationships require expert
domain knowledge. Incorporating evolving or specialized domain terminologies into the ontology accurately is complex
[34, 35].
Dynamic environments: Adapting ontologies to dynamic or evolving environments is challenging. Ensuring ontology
coherence and consistency while accommodating changes in domain concepts, terminologies, or relationships demands
continuous updates and version control mechanisms [36, 37].
Ambiguity and uncertainty: Dealing with ambiguous terms, uncertain knowledge representations, or conflicting
information within data sources presents challenges. Resolving ambiguity and handling uncertain or conflicting data
affect the ontology’s accuracy and reliability [31, 32].
Scalability: Ontology learning must accommodate large-scale data and knowledge sources while maintaining compu-
tational efficiency. Scaling ontology construction methods to handle substantial volumes of data without sacrificing
accuracy remains a significant challenge [38, 39].
Heterogeneity of data: Integrating heterogeneous data from diverse sources, each with different structures, formats,
and semantics, presents challenges. Aligning and reconciling conflicting data representations and resolving semantic
mismatches is crucial for creating coherent and comprehensive ontologies [14, 33, 31, 32].
3

Evaluation and validation: Properly evaluating ontologies for accuracy, completeness, and usability is complex.
Defining reliable evaluation metrics, validation methods, and assessing ontology quality pose challenges due to the
subjective nature of evaluating knowledge representations [31, 32, 40, 14].
3 Ontology Learning Approaches
3.1 Shallow-learning-based Approaches
Before the rise of deep learning, shallow learning methods grounded in traditional machine learning and classical neural
networks was predominant in ontology learning tasks such as term extraction, concept formation, taxonomy discovery,
non-taxonomic relation extraction, and axiom extraction [3]. These techniques mainly fall into three categories [3, 41]:
• Linguistics-based approaches. Linguistic techniques are based on characteristics of language, such as pattern-
based extraction [42], POS tagging and sentence parsing [43], syntactic structure analysis and dependency
structure analysis [44, 45] and etc.
• Statistics-based approaches. Statistical techniques are based on statistics of the underlying corpora. Typical
methods include co-occurrence analysis [ 46],

## 한국어 번역

온톨로지 학습에 대한 간략한 검토: S TRIDE TO
대규모 언어 모델 동향
Rick Du, Huilong An, Keyu Wang
BSH Home Appliances Holding (China) Co., Ltd.
{Rick.Du, Huilong.An, Keyu.Wang}@bshg.com
리우 웨이동
청화대학교 컴퓨터공학과
liuwd@tsinghua.edu.cn
개요
온톨로지는 시맨틱 웹 애플리케이션 내에서 공유되는 지식의 공식적인 표현을 제공합니다.
온톨로지 학습에는 주어진 코퍼스로부터 온톨로지를 구성하는 작업이 포함됩니다. 지난 몇 년 동안,
온톨로지 학습은 얕은 학습과 깊은 학습 방법론을 거쳐 왔습니다.
지식 추출 및 표현을 추구하는 데 있어 뚜렷한 장점과 한계를 제공합니다.
이러한 접근 방식의 새로운 추세는 온톨로지를 향상시키기 위해 LLM(대형 언어 모델)에 의존하는 것입니다.
학습. 이 논문은 온톨로지 학습의 접근 방식과 과제에 대한 검토를 제공합니다. 분석한다
얕은 학습 기반 기술과 딥러닝 기반 기술의 방법론과 한계
온톨로지 학습을 통해 LLM을 사용하는 최전선 작업에 대한 포괄적인 지식을 제공합니다.
온톨로지 학습을 강화합니다. 또한, 향후 몇 가지 주목할만한 미래 방향을 제안합니다.
온톨로지 학습 작업과 LLM의 통합에 대한 탐구.
1 소개
의미 있는 개념 지식의 추출과 조직은 기계 향상을 추구하는 데 핵심이었습니다.
이해력과 추론력 [1] 이 영역의 근본적인 초석인 온톨로지 학습은
복잡성을 캡슐화하는 구조화된 온톨로지의 추출, 표현 및 개선을 담당합니다.
다양한 도메인 [2].
지난 몇 년 동안 온톨로지 학습은 얕은 학습과 깊은 학습 방법론을 거쳐 왔습니다.
지식 추출 및 표현을 추구하는 데 있어 뚜렷한 장점과 한계를 제공합니다[3]. 얕은
단순성과 구현 용이성을 특징으로 하는 학습 기술은 오랫동안 교육의 기반이 되어 왔습니다.
온톨로지 학습 [4]. 이러한 방법은 특정 상황에서는 효과적이지만 종종 확장성 문제로 어려움을 겪습니다.
엔터티 간의 미묘하고 복잡한 관계를 추출합니다. 반대로 딥러닝의 등장
기술은 보다 복잡한 표현과 기본 요소에 대한 향상된 식별력을 약속하면서 새로운 시대를 예고했습니다.
데이터 내의 패턴. 그러나 딥러닝 기술에는 다음과 같은 한계가 있습니다.
주석이 달린 대량의 데이터와 계산 리소스에 대한 탐욕스러운 욕구.
이러한 환경 속에서 대규모 언어 모델의 출현은 윤곽을 재형성하는 파괴적인 힘으로 작용합니다.
온톨로지 학습 [6, 7]. 사전 훈련된 언어 표현의 능력을 활용하는 이러한 모델은
의미론적 뉘앙스를 이해하고, 맥락을 파악하고, 개체 간의 관계를 추론하는 놀라운 능력
[6, 7, 8, 9]. 온톨로지 학습에 대한 그들의 적용은
이러한 모델에 내재된 고유한 언어적, 개념적 이해를 활용합니다.
이 논문의 목적은 LLM 시대의 온톨로지 학습에 대한 접근 방식과 과제를 검토하는 것입니다. 그것은 선물한다
얕은 학습 기반과 딥 러닝 기반 기술의 한계점을 분석하고 방법을 제공합니다.
온톨로지 학습을 향상시키기 위해 LLM을 사용하는 현재 작업에 대한 포괄적인 지식. 게다가 제안한다.
대규모 언어 모델과 온톨로지의 통합에 대한 추가 탐구를 위한 몇 가지 주목할만한 미래 방향
arXiv:2404.14991v2 [cs.IR] 2024년 6월 17일

학습 과제. 본 논문의 나머지 부분은 다음과 같이 구성됩니다. 2장에서는 온톨로지, 온톨로지 학습 및
온톨로지 학습의 과제를 요약합니다. 섹션 3에서는 얕은 기반의 온톨로지 학습 접근법을 제시합니다.
학습과 딥러닝, 그리고 그 한계. 섹션 4에서는 대규모 언어 모델이 어떻게 기여하는지 보여줍니다.
최근 온톨로지 학습 절차를 다루고, 온톨로지를 촉진하기 위해 대규모 언어 모델을 사용할 가능성에 대해 논의합니다.
학습. 섹션 5에서는 대규모 언어 모델을 사용하여 추가 탐색을 위한 몇 가지 향후 방향을 제안합니다.
온톨로지 학습을 강화합니다. 마지막으로 6장에서 결론을 맺는다.
2 온톨로지 학습
2.1 온톨로지
일반적으로 온톨로지는 담론의 영역을 형식적으로 설명합니다. 일반적으로 온톨로지는 용어와
여기서 용어는 도메인의 중요한 개념을 나타냅니다 [10]. 온톨로지는 반드시
형식적이고 기계 판독이 가능하므로 다양한 애플리케이션에서 공유 어휘로 사용할 수 있습니다. 공식적으로,
온톨로지는 다음 튜플 [11]로 설명될 수 있습니다.
O =< C, H, R, A > (1)
여기서 O는 온톨로지를 나타내고, C는 클래스(개념) 집합을 나타내며, H는 클래스 간의 계층적 링크 집합을 나타냅니다.
개념(분류학적 관계), R은 일련의 개념적 링크(비분류학적 관계)를 나타내고, A는
일련의 규칙과 공리.
2.2 온톨로지 학습
텍스트로부터 온톨로지 학습(OL)은 주어진 텍스트 코퍼스로부터 온톨로지를 구성하는 것을 포함합니다[12, 13]. 따르면
OL [15]의 초석으로 널리 받아들여지고 있는 [14]에서 제안한 그림 1의 온톨로지 학습 레이어 케이크에,
텍스트에서 OL을 처리하는 과정은 다음과 같이 6가지 하위 작업으로 나눌 수 있습니다.
용어
동의어
개념
개념 계층
관계
규칙
질병, 병, 병원
{질병, 질병}
질병 ≔< 𝐼, 𝐸, 𝐿 >
𝑖𝑠_𝑎(𝐷𝑂𝐶𝑇𝑂𝑅, 𝑃𝐸𝑅𝑆𝑂𝑁)
𝑐𝑢𝑟𝑒(𝑑𝑜𝑚: 𝐷𝑂𝐶𝑇𝑂𝑅, 𝑟𝑎𝑛𝑔𝑒: 𝑃𝐸𝑅𝑆𝑂𝑁)
∀𝑥, 𝑦(𝑚𝑎𝑟𝑟𝑖𝑒𝑑 𝑥, 𝑦 → 𝑙𝑜𝑣𝑒(𝑥, 𝑦)
그림 1: 온톨로지 학습 레이어 케이크 [14]
1. 용어 추출: 이 초기 단계에는 주어진 텍스트나 데이터세트에서 관련 용어나 개체를 식별하는 작업이 포함됩니다.
이러한 용어는 온톨로지를 구성하기 위한 구성 요소 역할을 합니다.
2. 동의어 추출: 동의어는 동일한 개념을 가리키는 다른 용어입니다. 온톨로지 학습에서는
포괄적인 적용 범위를 보장하고 중복을 방지하려면 동의어를 식별하는 것이 중요합니다.
3. 개념 형성: 용어 및 동의어가 추출되면 다음 단계는 이를 다음과 같이 그룹화하는 것입니다.
의미 있는 개념이나 수업. 여기에는 관련 용어를 다음을 기반으로 계층 구조 또는 범주로 구성하는 작업이 포함됩니다.
유사성, 기능 또는 의미론적 관계.
2

4. 분류학적 관계 추출: 분류학적 관계는 개념 간의 계층적 관계를 설정하고,
"is-a" 관계를 정의합니다(예: "car"는 "vehicle"입니다). 온톨로지 학습에는 식별과
분류법 또는 온톨로지 계층 구조에서 개념을 배열하기 위해 이러한 계층적 관계를 구조화합니다.
5. 비분류학적 관계 추출: 분류학적 관계와 달리 비분류학적 관계는 다양한
계층적 관계를 넘어서는 개념 간의 연관. 이러한 관계는 "~의 일부", "~"일 수 있습니다.
속성" 또는 온톨로지의 표현력을 풍부하게 하는 기타 연관 연결.
6. 규칙 또는 공리 추출: 규칙 또는 공리는 둘 사이의 제약, 종속성 또는 논리적 관계를 정의합니다.
온톨로지의 엔터티 또는 개념. 규칙이나 공리를 추출하는 것은 도메인 지식을 공식화하고
온톨로지 내에서 논리적 제약 조건을 설정합니다.
일반적으로 온톨로지 학습 과정은 앞서 언급한 단계를 따릅니다. 그러나 일부에게는 드문 일이 아닙니다.
온톨로지 학습 프로세스는 다양한 요구 사항에 따라 위에 설명된 6단계를 부분적으로만 완료합니다. 온톨로지
학습 방법은 대략 다음 세 가지 범주로 나눌 수 있습니다 [16, 17, 18, 19].
• 수동: 온톨로지는 인간의 전문 지식과 개입에 크게 의존하는 프로세스를 통해 개발됩니다.
예를 들면 Gene Ontology(GO) [ 20], WordNet [ 21], SNOMED CT(Systematized Nomenclature of
의학 - 임상 용어) [22], Cyc [23] 및 FMA(Foundational Model of Anatomy) [24].
• 반자동: 자동화된 기능을 통합하여 온톨로지 개발을 촉진하고 간소화합니다.
인간의 입력으로 프로세스를 진행합니다. 이러한 목적을 위해 Text2Onto [ 25]와 같은 다양한 도구를 사용할 수 있습니다.
OntoGen [26] 및 OntoStudio [27].
• 완전 자동: 수동 개입 없이 시스템이 전체 구성을 관리합니다. 동안
완전 자동 온톨로지 구축 아이디어는 특히 대용량 데이터를 처리하거나
복잡한 도메인에서는 시스템에 의한 온톨로지를 위한 완전 자동 구성이 여전히
중대한 도전이며 불가능할 것 같습니다 [28, 29, 30].
2.3 온톨로지 학습의 과제
온톨로지 학습은 발전에도 불구하고 여전히 다양한 과제에 직면해 있습니다. 아래는 핵심을 강조한 목록입니다.
온톨로지 학습의 주요 과제를 특징짓는 측면:
노동 집약성: 온톨로지 구축에는 종종 상당한 수작업이 필요합니다. 식별, 추출 및
다양한 출처의 지식을 구조화하려면 광범위한 인간 개입이 필요합니다. 이 노동집약적인 과정은
시간이 많이 걸리고 리소스 집약적이어서 온톨로지 개발의 확장성과 효율성을 방해할 수 있습니다.
[15, 31, 32, 14].
공리 공식화: 도메인 지식을 정확하게 표현하는 정확한 공리 또는 규칙을 공식화하는 것은
도전. 표현력과 계산 효율성의 균형을 맞추는 것이 중요합니다. 공리는 의미 있고 정확해야 합니다.
온톨로지의 유용성에 효과적으로 기여합니다. 이를 위해서는 전문적인 전문 지식이 필요하며 종종 반복적인 작업이 필요합니다.
개선 [33, 31, 32].
도메인 특정 지식 획득: 온톨로지 내에서 도메인 특정 지식을 획득하고 표현합니다.
도전적이다. 복잡한 도메인 뉘앙스, 개념 및 관계를 이해하고 포착하려면 전문가가 필요합니다.
도메인 지식. 진화하거나 전문화된 도메인 용어를 온톨로지에 정확하게 통합하는 것은 복잡합니다.
[34, 35].
동적 환경: 동적이거나 진화하는 환경에 온톨로지를 적용하는 것은 어렵습니다. 온톨로지 보장
영역 개념, 용어 또는 관계 요구 사항의 변화를 수용하면서 일관성과 일관성을 유지합니다.
지속적인 업데이트 및 버전 제어 메커니즘 [36, 37].
모호함과 불확실성: 모호한 용어, 불확실한 지식 표현 또는 상충되는 내용 처리
데이터 소스 내의 정보는 문제를 야기합니다. 모호함을 해결하고 불확실하거나 상충되는 데이터 처리
온톨로지의 정확성과 신뢰성에 영향을 미칩니다 [31, 32].
확장성: 온톨로지 학습은 컴퓨팅을 유지하면서 대규모 데이터와 지식 소스를 수용해야 합니다.
국력 효율성. 희생 없이 상당한 양의 데이터를 처리하기 위한 온톨로지 구축 방법 확장
정확성은 여전히 중요한 과제로 남아 있습니다[38, 39].
데이터의 이질성: 각기 다른 구조, 형식,
그리고 의미론은 도전 과제를 제시합니다. 상충되는 데이터 표현을 정렬 및 조정하고 의미 체계를 해결합니다.
불일치는 일관되고 포괄적인 온톨로지를 생성하는 데 중요합니다 [14, 33, 31, 32].
3

평가 및 검증: 온톨로지의 정확성, 완전성 및 유용성을 적절하게 평가하는 것은 복잡합니다.
신뢰할 수 있는 평가 지표, 검증 방법을 정의하고 온톨로지 품질을 평가하는 것은 다음과 같은 문제로 인해 어려움을 겪습니다.
지식 표현 평가의 주관적 성격 [31, 32, 40, 14].
3 온톨로지 학습 접근법
3.1 얕은 학습 기반 접근 방식
딥러닝이 등장하기 전, 전통적인 머신러닝과 고전적 신경망을 기반으로 한 얕은 학습 방법
네트워크는 용어 추출, 개념 형성, 분류법 발견,
비분류학적 관계 추출, 공리 추출 [3]. 이러한 기술은 주로 세 가지 범주로 분류됩니다[3, 41].
• 언어학 기반 접근 방식. 언어학적 기법은 패턴-언어와 같은 언어의 특성을 기반으로 합니다.
기반 추출[42], POS 태깅 및 문장 파싱[43], 구문 구조 분석 및 종속성
구조 분석 [44, 45] 등
• 통계 기반 접근 방식. 통계 기법은 기본 말뭉치의 통계를 기반으로 합니다. 전형적인
방법에는 동시 발생 분석이 포함됩니다 [ 46],
