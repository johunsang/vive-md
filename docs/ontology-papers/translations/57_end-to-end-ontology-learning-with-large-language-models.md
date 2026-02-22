# [57] LLM 기반 종단간 온톨로지 학습

- 영문 제목: End-to-End Ontology Learning with Large Language Models
- 연도: 2024
- 원문 링크: https://doi.org/10.48550/arXiv.2410.23584
- DOI: 10.48550/arxiv.2410.23584
- 원문 저장 상태: pdf_saved
- 원문 파일: /Volumes/SAMSUNG/apps/projects/vive-md/docs/ontology-papers/originals/57_end-to-end-ontology-learning-with-large-language-models.pdf
- 번역 상태: partial_translated

## 원문(추출 텍스트)

End-to-End Ontology Learning with
Large Language Models
Andy Lo
University of Cambridge
cyal4@cam.ac.uk
Albert Q. Jiang
University of Cambridge
qj213@cam.ac.uk
Wenda Li
University of Edinburgh
wenda.li@ed.ac.uk
Mateja Jamnik
University of Cambridge
mateja.jamnik@cl.cam.ac.uk
Abstract
Ontologies are useful for automatic machine processing of domain knowledge
as they represent it in a structured format. Yet, constructing ontologies requires
substantial manual effort. To automate part of this process, large language models
(LLMs) have been applied to solve various subtasks of ontology learning. However,
this partial ontology learning does not capture the interactions between subtasks.
We address this gap by introducing OLLM, a general and scalable method for
building the taxonomic backbone of an ontology from scratch. Rather than fo-
cusing on subtasks, like individual relations between entities, we model entire
subcomponents of the target ontology by finetuning an LLM with a custom regu-
lariser that reduces overfitting on high-frequency concepts. We introduce a novel
suite of metrics for evaluating the quality of the generated ontology by measuring
its semantic and structural similarity to the ground truth. In contrast to standard
syntax-based metrics, our metrics use deep learning techniques to define more
robust distance measures between graphs. Both our quantitative and qualitative
results on Wikipedia show that OLLM outperforms subtask composition methods,
producing more semantically accurate ontologies while maintaining structural
integrity. We further demonstrate that our model can be effectively adapted to new
domains, like arXiv, needing only a small number of training examples. Our source
code and datasets are available at https://github.com/andylolu2/ollm.
1 Introduction
An ontology is a formal and structural way of representing domain-specific concepts and their
relations [16]. They can be simple (e.g., Wikipedia categories) consisting of concepts and only a
small number of types of taxonomic relations (e.g., is-a relationships), or they can be complex (e.g.,
Schema.org) consisting of axioms or many types of relations. For example, a simple ontology for
programming languages might contain two concepts “Dynamically-typed language” and “Python”,
and one relation “Dynamically-typed language → Python”, representing the knowledge that Python
is a dynamically-typed language. A more complex ontology might contain axioms too, for example,
“all programming languages are either dynamically or statically typed”. In this paper, we focus on
ontologies with only concepts and taxonomic relations. Compared to typical deep learning models,
which represent knowledge implicitly in its weights, ontologies capture knowledge in a structured
and explicit manner, making them reliable, easy to edit and human-interpretable. Such benefits of
ontologies have led to their wide adoption in practice. For example, Wikipedia categories have been
38th Conference on Neural Information Processing Systems (NeurIPS 2024).
arXiv:2410.23584v1  [cs.LG]  31 Oct 2024

Dataset
... ... LLM Mask-regularised loss
Backpropagate
T arget
LLM
...
Output
Sum and prune
Gold standard evaluation
T rainingEvaluation /
Inference
Document
Concept
Is-a relation
Figure 1: OLLM: Using annotations of documents with their relevant concepts, we train an LLM
to model relevant subgraphs of the target ontology with a custom regulariser. During inference, the
generated subgraphs for each document are summed and pruned to give the final output ontology.
For evaluation, we measure the similarity between the generated ontology and the ground truth.
used for entity ranking [46] and information retrieval [42], or Schema.org [40] is a core component
of the Semantic Web [1] initiative.
While ontologies are useful, building ontologies often requires substantial manual effort. Ontology
learning (OL) is the study of automating the construction of high-quality ontologies at scale. For a
simple ontology, this amounts to discovering the concepts and taxonomic relations, usually based
on a source corpus. In this paper we aim to develop domain-independent methods for OL that are
scalable and produce better ontologies.
Traditionally, OL is viewed as a composition of subtasks [3], such as concept discovery and relation
extraction. In particular, prior works have demonstrated that state-of-the-art large language models
(LLMs) can solve such subtasks effectively [4]. While studying subtasks permits fine-grained analysis
and evaluation, it does not directly indicate the subsequent impact on the quality of the final ontology.
Moreover, there is potential room for improvement by combining several subtasks into one, such as
by modelling concepts and relations in conjunction. In this paper, we instead develop and evaluate
methods that construct ontologies in an end-to-end fashion to answer the following research questions:
1. How can we leverage LLMs’ knowledge base to build ontologies from scratch?
2. Does our method scale efficiently to practical problem sizes?
3. How well does our method generalise to new domains?
We introduce OLLM, an end-to-end method for using LLMs to construct ontologies at scale. Rather
than focusing on individual relations between concepts, we finetune an LLM to model entire sub-
components of the target ontology. The output ontology is generated by taking the sum of generated
sub-components and applying simple post-processing. An overview of the pipeline is shown in
Figure 1. To train OLLM, we collect the categorisation metadata for a subset of Wikipedia articles.
We attempt to adapt an LLM to model the relevant categorisation subgraph for a particular Wikipedia
article, but discover that direct finetuning leads to poor generalisation due to overfitting to high-level,
frequently occurring concepts. Instead, we propose a custom regulariser that reweights each concept
based on its frequency of occurrence, which substantially improves generalisation.
We evaluate OLLM by measuring the similarity of the generated ontology with the ground truth.
Current approaches for comparing ontologies rely on mapping components of the two ontologies
onto each other, most commonly by literal text matching [30, 45]. This is unreliable when the two
ontologies are not already sufficiently similar. Instead, we propose a suite of evaluation metrics
suitable for comparing arbitrary labelled graphs. These metrics compare edges and subgraphs of
the two ontologies using pretrained text embedders to test for semantic and structural similarity.
Both our quantitative and qualitative results reveal that an LLM can already outperform existing
2

extraction-based methods out of the box, and the performance is further improved by finetuning with
our custom regulariser. We additionally demonstrate that OLLM can be adapted to build the arXiv
ontology using only a small number of training examples, suggesting that our model can be applied
to new domains in a data-efficient way. In summary, our contributions are:
1. We constructed two datasets based on Wikipedia and arXiv, which can serve as standard datasets
for future work studying end-to-end OL.
2. We created OLLM, a method that utilises LLMs to build ontologies from scratch. OLLM produces
high-quality ontologies and serves as a strong baseline for end-to-end OL.
3. We developed new evaluation metrics for assessing the quality of the generated ontologies.
2 Background
An ontology is a structured way of representing concepts and relations of a shared conceptualisation,
that is, domain knowledge [ 15, 16]. Ontologies can span a wide range of complexities. A fully-
fledged ontology might contain concepts, relations, constraints, and axioms that enable complex
automated reasoning. In this paper, we focus on the core building blocks of an ontology: concepts and
taxonomic relations which represent is-a or is-subclass-of relationships between concepts. In some
cases, the is-part-of relation is also considered a taxonomic relation. We treat such an ontology as a
rooted labelled directed graph where nodes represent concepts, edges represent taxonomic relations
and the root node is the special concept of all concepts. A strict ontology asserts that the taxonomic
relation is asymmetric and thus the graph must be acyclic, though in practice some ontologies, such
as the Wikipedia ontology studied in this paper, may contain cycles. We therefore do not assume
that an ontology graph is necessarily acyclic. Examples of ontologies include WordNet [ 33] with
117,659 concepts and 89,089 taxonomic relations, and the Gene Ontology [2] with 42,255 concepts
and 66,810 taxonomic relations.
Ontology learning is the automatic extraction of ontological elements [17]. The most studied source
of input is unstructured text, though there are also works on semi-structured data like HTML [22]. In
this paper, the input is a set of documents, each consisting of some unstructured text. We additionally
assume each document is associated with one or more concepts in the ground truth ontology, which
we utilise for training. The goal is to reconstruct the ground truth ontology given the set of documents.
Prior works view OL as a composition of subtasks, and study each subtask in isolation [ 3, 6]. A
typical pipeline for building a simple ontology is to first perform concept discovery (identify the
nodes), and then relation extraction (identify the edges) [ 8, 24]. A notable approach for relation
extraction is Hearst patterns [ 18]. Hearst patterns are hand-crafted lexico-syntactic patterns that
exploit natural language structure to discover taxonomic relations. For example, the pattern “[noun
phrase] such as [noun phrase]” matches phrases like “dogs such as chihuahuas”, and thus can be
processed by regular expressions to identify the relation “dog → chihuahua”. Hearst patterns suffer
from low recall, as the relations must occur in exact configurations to be identified by the rules. Roller
et al. [39] suggest smoothing techniques to alleviate this issue though at the cost of lower precision.
Recently, language models have been used for OL. REBEL [7] treats relation discovery as a translation
task, and finetunes encoder-decoder LLMs to extract both taxonomic and non-taxonomic relations.
Babaei Giglou et al. [4] benchmarked a wide family of LLMs for concept and relation discovery,
and showed promising results. However, the quadratic complexity of link prediction makes this
approach unscalable to large ontologies. We provide more discussion in Appendix A.2.3. There are
also proof-of-concept works for building ontologies end-to-end with LLMs. Funk et al. [13] proposes
to build an ontology by recursively prompting LLMs, while Trajanoska et al. [44] generate the entire
ontology in one completion. However, both studies are limited in the scale of the task and evaluation:
they only considered ontologies of up to 1000 concepts and relied on manual qualitative evaluation.
We bridge this gap by proposing a method that can scale to practical problem sizes and new metrics
for systematic qualitative evaluation.
The evaluation of ontologies is an open research area. The main approaches are gold standard
evaluation [51], which matches elements of the generated ontology with a predefined target ontology;
task-based evaluation [36], which measures the usefulness of the ontology on a specific application;
and human evaluation [5, 37]. In this paper, we evaluate by the gold standard metric as it is the
most straightforward approach when ground-truth ontology exists. Prior works have considered
3

Main topic classiﬁcations
Humanities
Politics
Culture
Human behavior
Politics by issue
Sociology of culture
Human activities
Politics and race
<s>[INST] Title: Hybridity
Hybridity, in its most basic sense ... [/INST]
Main topic classifications -> Human behavior
-> Human activities -> Culture ->
Sociology of culture
Main topic classifications -> Humanities ->
Politics -> Politics

## 한국어 번역

엔드투엔드 온톨로지 학습
대규모 언어 모델
앤디 로
케임브리지대학교
cial4@cam.ac.uk
앨버트 Q. 지앙
케임브리지대학교
qj213@cam.ac.uk
웬다 리
에든버러 대학교
wenda.li@ed.ac.uk
마테야 잼니크
케임브리지대학교
mateja.jamnik@cl.cam.ac.uk
초록
온톨로지는 도메인 지식의 자동 기계 처리에 유용합니다.
구조화된 형식으로 표현하기 때문입니다. 그러나 온톨로지를 구축하려면 다음이 필요합니다.
상당한 수작업. 이 프로세스의 일부를 자동화하기 위해 대규모 언어 모델
(LLM)은 온톨로지 학습의 다양한 하위 작업을 해결하기 위해 적용되었습니다. 그러나,
이 부분 온톨로지 학습은 하위 작업 간의 상호 작용을 캡처하지 않습니다.
우리는 일반적이고 확장 가능한 방법인 OLLM을 도입하여 이러한 격차를 해소합니다.
온톨로지의 분류학적 백본을 처음부터 구축합니다. fo보다는-
엔터티 간의 개별 관계와 같은 하위 작업을 사용하여 전체를 모델링합니다.
사용자 정의 규정으로 LLM을 미세 조정하여 대상 온톨로지의 하위 구성 요소
고주파수 개념에 대한 과적합을 줄이는 레이저입니다. 소설을 소개합니다
측정을 통해 생성된 온톨로지의 품질을 평가하기 위한 측정항목 모음
실제 사실과 의미론적 및 구조적 유사성을 갖습니다. 표준과 달리
구문 기반 측정항목인 우리 측정항목은 딥러닝 기술을 사용하여 더 많은 것을 정의합니다.
그래프 사이의 강력한 거리 측정. 우리의 양적, 질적
Wikipedia의 결과에 따르면 OLLM은 하위 작업 구성 방법보다 성능이 뛰어납니다.
구조를 유지하면서 보다 의미적으로 정확한 온톨로지를 생성합니다.
무결성. 우리는 우리 모델이 새로운 환경에 효과적으로 적응할 수 있음을 추가로 보여줍니다.
arXiv와 같은 도메인에는 소수의 훈련 예제만 필요합니다. 우리의 소스
코드와 데이터 세트는 https://github.com/andylolu2/ollm에서 확인할 수 있습니다.
1 소개
온톨로지는 도메인별 개념과 그 개념을 표현하는 공식적이고 구조적인 방법입니다.
관계 [16]. 이는 개념과 단지
분류학적 관계 유형이 적거나(예: is-a 관계) 복잡할 수 있습니다(예:
Schema.org)는 공리 또는 다양한 유형의 관계로 구성됩니다. 예를 들어, 다음과 같은 간단한 온톨로지는
프로그래밍 언어에는 "동적 유형 언어"와 "Python"이라는 두 가지 개념이 포함될 수 있습니다.
그리고 하나의 관계 "동적 유형 언어 → Python"은 Python에 대한 지식을 나타냅니다.
동적 유형 언어입니다. 더 복잡한 온톨로지는 공리도 포함할 수 있습니다. 예를 들어,
"모든 프로그래밍 언어는 동적으로 또는 정적으로 유형이 지정됩니다." 이 논문에서 우리는 다음에 중점을 둡니다.
개념과 분류학적 관계만을 가진 온톨로지. 일반적인 딥러닝 모델과 비교하면,
지식을 가중치로 암묵적으로 표현하는 온톨로지는 지식을 구조화된 방식으로 포착합니다.
명시적인 방식으로 신뢰할 수 있고 편집하기 쉽고 사람이 해석할 수 있게 만듭니다. 이러한 이점은
온톨로지는 실제로 널리 채택되었습니다. 예를 들어 Wikipedia 카테고리는 다음과 같습니다.
제38차 신경정보처리시스템 컨퍼런스(NeurIPS 2024).
arXiv:2410.23584v1 [cs.LG] 2024년 10월 31일

데이터세트
... ... LLM 마스크 정규화 손실
역전파
타겟
법학대학원
...
출력
합계 및 정리
최적의 평가
훈련평가 /
추론
문서
개념
Is-a 관계
그림 1: OLLM: 관련 개념이 포함된 문서의 주석을 사용하여 LLM을 교육합니다.
맞춤형 정규화 도구를 사용하여 대상 온톨로지의 관련 하위 그래프를 모델링합니다. 추론하는 동안,
각 문서에 대해 생성된 하위 그래프를 합산하고 정리하여 최종 출력 온톨로지를 제공합니다.
평가를 위해 생성된 온톨로지와 Ground Truth 간의 유사성을 측정합니다.
엔터티 순위[46] 및 정보 검색[42]에 사용되거나 Schema.org[40]가 핵심 구성 요소입니다.
시맨틱 웹 [1] 이니셔티브의 일부입니다.
온톨로지는 유용하지만, 온톨로지를 구축하려면 상당한 수작업이 필요한 경우가 많습니다. 온톨로지
학습(OL)은 대규모로 고품질 온톨로지 구축을 자동화하는 연구입니다. 에 대한
단순한 온톨로지는 일반적으로 기반이 되는 개념과 분류학적 관계를 발견하는 것과 같습니다.
소스 코퍼스에서. 이 논문에서 우리는 OL에 대한 도메인 독립적인 방법을 개발하는 것을 목표로 합니다.
확장 가능하고 더 나은 온톨로지를 생성합니다.
전통적으로 OL은 개념 발견, 관계 등 하위 작업의 구성으로 간주됩니다[3].
추출. 특히, 이전 연구에서는 최첨단 대규모 언어 모델이
(LLM)은 이러한 하위 작업을 효과적으로 해결할 수 있습니다[4]. 하위 작업을 공부하면서 세밀한 분석이 가능합니다.
및 평가는 최종 온톨로지의 품질에 대한 후속 영향을 직접적으로 나타내지 않습니다.
또한 다음과 같은 여러 하위 작업을 하나로 결합하면 개선의 여지가 있습니다.
개념과 관계를 함께 모델링함으로써. 이 논문에서는 대신에 개발하고 평가합니다.
다음 연구 질문에 답하기 위해 엔드 투 엔드 방식으로 온톨로지를 구성하는 방법:
1. LLM의 지식 기반을 어떻게 활용하여 처음부터 온톨로지를 구축할 수 있습니까?
2. 우리의 방법이 실제 문제 크기에 맞게 효율적으로 확장됩니까?
3. 우리의 방법은 새로운 영역에 얼마나 잘 일반화됩니까?
LLM을 사용하여 규모에 맞게 온톨로지를 구성하는 엔드투엔드 방법인 OLLM을 소개합니다. 오히려
개념 간의 개별 관계에 초점을 맞추는 대신 LLM을 미세 조정하여 전체 하위 항목을 모델링합니다.
타겟 온톨로지의 구성 요소. 출력 온톨로지는 생성된 온톨로지의 합을 취하여 생성됩니다.
하위 구성 요소 및 간단한 후처리를 적용합니다. 파이프라인의 개요는 다음과 같습니다.
그림 1. OLLM을 훈련하기 위해 Wikipedia 기사의 하위 집합에 대한 분류 메타데이터를 수집합니다.
우리는 특정 Wikipedia에 대한 관련 분류 하위 그래프를 모델링하기 위해 LLM을 적용하려고 시도합니다.
그러나 직접적인 미세 조정은 상위 수준에 대한 과적합으로 인해 일반화가 좋지 않음을 발견했습니다.
자주 발생하는 개념. 대신에 우리는 각 개념에 다시 가중치를 부여하는 맞춤형 정규화 도구를 제안합니다.
발생 빈도에 따라 일반화가 크게 향상됩니다.
우리는 생성된 온톨로지와 Ground Truth의 유사성을 측정하여 OLLM을 평가합니다.
온톨로지를 비교하기 위한 현재 접근 방식은 두 온톨로지의 매핑 구성 요소에 의존합니다.
가장 일반적으로 문자 그대로의 텍스트 일치를 통해 서로 연결됩니다[30, 45]. 이는 두 가지가 있을 때 신뢰할 수 없습니다.
온톨로지는 아직 충분히 유사하지 않습니다. 대신에 우리는 일련의 평가 지표를 제안합니다.
임의의 레이블이 지정된 그래프를 비교하는 데 적합합니다. 이 측정항목은 가장자리와 하위 그래프를 비교합니다.
의미론적 및 구조적 유사성을 테스트하기 위해 사전 훈련된 텍스트 임베더를 사용하는 두 가지 온톨로지.
양적 및 질적 결과 모두 LLM이 이미 기존보다 더 나은 성과를 낼 수 있음을 보여줍니다.
2

기본적으로 추출 기반 방법을 사용하고 미세 조정을 통해 성능이 더욱 향상됩니다.
우리의 맞춤형 정규화기. 우리는 또한 OLLM을 arXiv 구축에 적용할 수 있음을 보여줍니다.
소수의 훈련 예제만을 사용하는 온톨로지를 통해 우리 모델이 적용될 수 있음을 시사
데이터 효율적인 방식으로 새로운 도메인으로 확장합니다. 요약하면 우리의 기여는 다음과 같습니다.
1. 표준 데이터세트로 사용할 수 있는 Wikipedia와 arXiv를 기반으로 두 개의 데이터세트를 구축했습니다.
엔드투엔드 OL을 연구하는 향후 작업을 위해.
2. 우리는 LLM을 활용하여 처음부터 온톨로지를 구축하는 방법인 OLLM을 만들었습니다. OLLM이 생산하는
고품질 온톨로지를 제공하며 엔드투엔드 OL의 강력한 기준선 역할을 합니다.
3. 우리는 생성된 온톨로지의 품질을 평가하기 위한 새로운 평가 지표를 개발했습니다.
2 배경
온톨로지는 공유된 개념화의 개념과 관계를 표현하는 구조화된 방식입니다.
즉, 도메인 지식 [ 15, 16]. 온톨로지는 광범위한 복잡성을 포괄할 수 있습니다. 완전-
본격적인 온톨로지는 복잡한 작업을 가능하게 하는 개념, 관계, 제약 및 공리를 포함할 수 있습니다.
자동화된 추론. 이 논문에서 우리는 온톨로지의 핵심 구성 요소인 개념과
개념 간의 is-a 또는 is-subclass-of 관계를 나타내는 분류학적 관계입니다. 일부에서는
경우에는 is-part-of 관계도 분류학적 관계로 간주됩니다. 우리는 그러한 온톨로지를 다음과 같이 취급합니다.
노드가 개념을 나타내고 가장자리가 분류학적 관계를 나타내는 루트 레이블 지정 그래프
루트 노드는 모든 개념의 특별한 개념입니다. 엄격한 온톨로지는 분류학적으로 다음과 같이 주장합니다.
관계는 비대칭이므로 그래프는 비순환적이어야 합니다. 그러나 실제로는 일부 온톨로지가 다음과 같습니다.
이 문서에서 연구된 Wikipedia 온톨로지는 주기를 포함할 수 있습니다. 그러므로 우리는 가정하지 않습니다
온톨로지 그래프는 필연적으로 비순환적입니다. 온톨로지의 예에는 WordNet [ 33]이 포함됩니다.
117,659개의 개념과 89,089개의 분류학적 관계, 그리고 42,255개의 개념을 가진 유전자 온톨로지[2]
그리고 66,810개의 분류학적 관계.
온톨로지 학습은 온톨로지 요소를 자동으로 추출하는 것이다[17]. 가장 많이 연구된 소스
입력의 대부분은 구조화되지 않은 텍스트이지만 HTML [22]과 같은 반구조화된 데이터에 대한 작업도 있습니다. 에서
이 논문에서 입력은 각각 구조화되지 않은 텍스트로 구성된 문서 세트입니다. 우리는 추가적으로
각 문서가 Ground Truth 온톨로지의 하나 이상의 개념과 연관되어 있다고 가정합니다.
우리는 훈련에 활용합니다. 목표는 문서 세트가 주어지면 Ground Truth 온톨로지를 재구성하는 것입니다.
이전 연구에서는 OL을 하위 작업의 구성으로 보고 각 하위 작업을 별도로 연구했습니다[3, 6]. 에이
간단한 온톨로지를 구축하기 위한 일반적인 파이프라인은 먼저 개념 발견을 수행하는 것입니다(
노드), 관계 추출(에지 식별) [8, 24]. 관계에 대한 주목할만한 접근 방식
추출은 Hearst 패턴입니다 [18]. 허스트 패턴은 손으로 만든 어휘-구문 패턴입니다.
분류학적 관계를 발견하기 위해 자연어 구조를 활용합니다. 예를 들어, “[명사
Phrase] such as [명사구]”는 “dogs such as chihuahuas”와 같은 구문과 일치하므로 다음과 같을 수 있습니다.
"개 → 치와와" 관계를 식별하기 위해 정규식으로 처리됩니다. 허스트 패턴이 어려움
규칙에 의해 식별되려면 관계가 정확한 구성으로 발생해야 하기 때문에 재현율이 낮습니다. 롤러
외. [39]는 낮은 정밀도를 희생하면서 이 문제를 완화하기 위한 평활화 기술을 제안했습니다.
최근에는 OL에 언어 모델이 사용되었습니다. REBEL [7]은 관계 발견을 번역으로 취급합니다.
작업을 수행하고 인코더-디코더 LLM을 미세 조정하여 분류학적 관계와 비분류학적 관계를 모두 추출합니다.
Babaei Giglouet al. [4]는 개념 및 관계 발견을 위해 광범위한 LLM 제품군을 벤치마킹했습니다.
그리고 유망한 결과를 보여주었다. 그러나 링크 예측의 2차 복잡성으로 인해
대규모 온톨로지에 확장 불가능하게 접근합니다. 부록 A.2.3에서 더 많은 논의를 제공합니다. 있다
또한 개념 증명은 LLM을 사용하여 엔드 투 엔드 온톨로지를 구축하는 데에도 작동합니다. Funket al. [13] 제안하다
LLM을 재귀적으로 프롬프트하여 온톨로지를 구축하는 반면 Trajanoska et al. [44] 전체를 생성
한 번의 완성으로 온톨로지. 그러나 두 연구 모두 과제와 평가의 규모가 제한되어 있습니다.
그들은 최대 1000개 개념의 온톨로지만을 고려했으며 수동적인 정성적 평가에 의존했습니다.
우리는 실제적인 문제 크기와 새로운 지표로 확장할 수 있는 방법을 제안하여 이러한 격차를 해소합니다.
체계적인 정성평가를 위해
온톨로지의 평가는 공개된 연구 분야입니다. 주요 접근 방식은 금본위제입니다.
생성된 온톨로지의 요소를 미리 정의된 대상 온톨로지와 일치시키는 평가 [51];
특정 애플리케이션에 대한 온톨로지의 유용성을 측정하는 작업 기반 평가[36];
인간 평가 [5, 37]. 본 논문에서는 금본위제 기준으로 평가합니다.
Ground Truth 온톨로지가 존재할 때 가장 간단한 접근 방식입니다. 이전 작품을 고려
3

주요 주제 분류
인문학
정치
문화
인간 행동
이슈별 정치
문화사회학
인간 활동
정치와 인종
<s>[INST] 제목: 하이브리드
가장 기본적인 의미에서의 혼종성... [/INST]
주요 주제 분류 -> 인간 행동
-> 인간활동 -> 문화 ->
문화사회학
주요주제 분류 -> 인문학 ->
정치 -> 정치
