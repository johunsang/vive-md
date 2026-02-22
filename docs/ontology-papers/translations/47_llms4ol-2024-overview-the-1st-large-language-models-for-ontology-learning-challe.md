# [47] LLMs4OL 2024 개요

- 영문 제목: LLMs4OL 2024 Overview: The 1st Large Language Models for Ontology Learning Challenge
- 연도: 2024
- 원문 링크: https://doi.org/10.52825/ocp.v4i.2473
- DOI: 10.52825/ocp.v4i.2473
- 원문 저장 상태: pdf_saved
- 원문 파일: /Volumes/SAMSUNG/apps/projects/vive-md/docs/ontology-papers/originals/47_llms4ol-2024-overview-the-1st-large-language-models-for-ontology-learning-challe.pdf
- 번역 상태: partial_translated

## 원문(추출 텍스트)

LLMs4OL 2024: The 1st Large Language Models for Ontology Learning Challenge at the 23rd ISWC
LLMs4OL 2024 Task Overview
https://doi.org/10.52825/ocp.v4i.2473
© Authors. This work is licensed under a Creative Commons Attribution 4.0 International License
Published: 02 Oct. 2024
LLMs4OL 2024 Overview: The 1st Large Language
Models for Ontology Learning Challenge
Hamed Babaei Giglou , Jennifer D’Souza , and S¨oren Auer
TIB Leibniz Information Centre for Science and Technology, Hannover, Germany
{hamed.babaei, jennifer.dsouza, auer}@tib.eu
*Correspondence: Hamed Babaei Giglou, hamed.babaei@tib.eu
Abstract: This paper outlines the LLMs4OL 2024, the first e dition o f t he L arge Lan-
guage Models for
 Ontology Learning Challenge. LLMs4OL is a community develop-
ment initiative
 collocated with the 23rd International Semantic Web Conference (ISWC) 
to explore the potential of Large Language Models (LLMs) in Ontology Learning (OL), a 
vital process
 for enhancing the web with structured knowledge to improve interoperabil-
ity. By leveraging LLMs, the challenge aims to advance understanding and innovation 
in OL, aligning with the goals of the Semantic Web to create a more intelligent and user-
friendly web. In this paper, we give an overview of the  2024 edition of the LLMs4OL 
challenge1 and summarize the contributions.
Keywords: LLMs4OL Challenge, Ontology Learning, Large Language Models
1 Introduction
The Semantic Web aims to enrich the current web with structured knowledge and meta-
data, enabling enhanced interoperability and  understanding across diverse systems. 
At the core of this endeavor is Ontology Learning (OL), a process that  automates the 
extraction of structured knowledge from unstructured data [1],  essential for construct-
ing dynamic ontologies that underpin the Semantic Web. The emergence of Large 
Language Models (LLMs) like GPT -3 [2] and  GPT -4 [3] has revolutionized natural lan-
guage processing (NLP), demonstrating remarkable performance across tasks such as 
language translation, question answering, and text generation. These models are par-
ticularly adept at crystallizing existing textual knowledge from a v ast array of sources,  
making them potentially valuable for OL, where the goal is to extract a shared concep-
tualization of concepts and relationships from diverse inputs [4] . The introduction of 
LLMs has thus opened up new avenues of research, including the exploration of their 
potential in automating the OL process .
In our prior work published in the ISWC 2023 research track proceedings titled 
“LLMs4OL: Large Language Models for Ontology Learning” [5], marked a notable di-
rection towards employing LLMs in OL, demonstrating  their potential in automating 
knowledge acquisition and representation for the Semantic Web. Based on this re-
search, the The 1st
 Large Languag e Models for Ontology Learning Challenge at
1https://sites.google.com/view/llms4ol
3

Babaei Giglou et al. | Open Conf Proc 4 (2024) ”LLMs4OL 2024: The 1st Large Language Models for Ontology Learning
Challenge at the 23rd ISWC”
Corpus
Preparation
Conceptualization
 (1) Term Typing  (2) Types Taxonomy  (3) Relationships Extraction
Terminology
Extraction
Axiom
Discovery
Task A: Term Typing Task B:  Types Taxonomy Task C: Relation Extraction 
Ontology Learning
LLMs4OL
Figure 1. The LLMs4OL task paradigm is an end-to-end framework for ontology learning. The three
OL tasks that empirically validated in the LLMs4OL 2024 challenge, based on our prior re-
search [5], are depicted within the blue arrow, aligned with the greater LLMs4OL paradigm.
the 23rd ISWC 2024 (1st LLMs4OL Challenge @ ISWC 2024) was introduced as a
call for community development. With the LLMs4OL challenge, we aimed to catalyze
community-wide engagement in validating and expanding the use of LLMs in OL. This
initiative is poised to advance our comprehension of LLMs’ roles within the Semantic
Web, encouraging innovation and collaboration in developing scalable and accurate
ontology learning methods.
LLMs4OL consists of three OL tasks, Task A – Term Typing, Task B – Taxonomy
Discovery, and Task C – Non-Taxonomic Relation Extraction. While participation in all
three tasks in the LLMs4OL 2024 challenge is stipulated as desirable, but not manda-
tory. Thus participants choose to enroll only in Task A or B or C, or Task A and B, or
Task A and C, or Task B and C. Furthermore, participants are required to implement
LLM-based solutions, we did not impose any restrictions on the LLM prompting meth-
ods. For instance, they can choose to bring in additional context information from the
World Wide Web to enrich the training and test instances. To thoroughly explore the
potential of LLMs for OL, we structured the challenge around two distinct evaluation
phases: (1) Few-shot testing phase and (2) Zero-shot testing phase. Through this
work, we aim to contribute to the ongoing discourse on the capabilities of LLMs, par-
ticularly in the context of OL, and to provide insights into their potential for enhancing
the Semantic Web. Thus, in the remainder of this paper, we detail the challenge tasks,
what LLMs are being used, participant contributions, and findings.
2 LLMs4OL 2024 Tasks
In the LLMs4OL 2024 challenge, we have organized three main tasks which are cen-
tered around the ontology primitives [6] that comprise the following: 1. a set of strings
that describe terminological lexical entries L for conceptual types; 2. a set of concep-
tual types T; 3. a taxonomy of types in a hierarchy HT ; 4. a set of non-taxonomic
relations R described by their domain and range restrictions arranged in a heterarchy
of relations HR; and 5. a set of axioms A that describe additional constraints on the
ontology and make implicit facts explicit.
To address these primitives, the tasks for OL [7] are: 1) Corpus preparation – collect-
ing source texts for building ontology. 2) Terminology extraction – extracting relevant
terms from the texts. 3) Term typing – grouping similar terms into conceptual types.
4) Taxonomy construction – establishing “is-a” hierarchies between types. 5) Rela-
tionship extraction – extracting semantic relationships beyond “is-a” between types. 6)
Axiom discovery – finding constraints rules for the ontology. These tasks constitute the
LLMs4OL task paradigm as depicted in Figure 1. Assuming the corpus preparation
step is done by reusing ontologies publicly released in the community, we introduced
the following three main tasks for the first edition of the LLMs4OL challenge.
4

Babaei Giglou et al. | Open Conf Proc 4 (2024) ”LLMs4OL 2024: The 1st Large Language Models for Ontology Learning
Challenge at the 23rd ISWC”
Table 1. LLMs4OL 2024 challenge, subtasks, domains, number of participants per subtasks, and evalu-
ation phases.
Task SubTask Domain Participants Phase
A
A.1 - WordNet lexicosemantics 7
Few-shot
A.2 - GeoNames geographical locations 5
A.3 - UMLS - NCI
biomedical
5
A.3 - UMLS - MEDCIN 4
A.3 - UMLS - SNOMEDCT US 4
A.4 - GO - Biological Process
biological
5
A.4 - GO - Cellular Component 5
A.4 - GO - Molecular Function 5
A.5 - DBO general knowledge 2 Zero-shotA.6 - FoodOn food 2
B
B.1 - GeoNames geographical locations 5
Few-shotB.2 - Schema.org web content types 3
B.3 - UMLS biomedical 3
B.4 - GO biological 1
B.5 - DBO general knowledge 2 Zero-shotB.6 - FoodOn food 1
C
C.1 - UMLS biomedical 2 Few-shotC.2 - GO biological 0
C.3 - FoodOn food 0 Zero-shot
2.1 Task A – Term Typing
The Table 1 shows 10 subtasks for Task A across 6 distinct domains such as lexi-
cosemantics, geographical locations, biomedical, biological, general knowledge, and
food domains. This task is defined as ”discover the generalized type for a given lexical
term”. For this task, for each ontology, participants are given training instances defined
as following formalism.
f T askA
prompt(L) := [S ?]. ([L], [T ])
Where S is an optional context sentence (if available in the source ontology), L is the
lexical term prompted for, and T is the conceptual term type. In the test phase, types
are hidden, and participants predict them for given terms using their trained models.
2.2 Task B – Taxonomy Discovery
After grouping terms under a conceptual type, in Task B, the goal is for given types
”discover the taxonomic hierarchy between types”, where the hierarchy between types
is defined with an ”is-a” relationship. Participants receive training instances for 6 distinct
subtasks (described in Table 1) as :
f T askB
prompt(a, b) := (T a, T b)
Where Ta is the parent (superclass) of Tb, and Tb is the child (subclass) of Ta. The
goal is to train a system to correctly identify the taxonomy between type. The training
dataset will include term types and taxonomically related type pairs. In the test phase,
participants work with just term types and must use their trained models to identify
correct taxonomic relationships (type pairs). The types for the training and test phases
are mutually exclusive. Furthermore, for the testing phase participants are required
to post-process their outputs to return type pairs that follow the order of superclass-
subclass related types.
5

Babaei Giglou et al. | Open Conf Proc 4 (2024) ”LLMs4OL 2024: The 1st Large Language Models for Ontology Learning
Challenge at the 23rd ISWC”
2.3 Task C – Non-Taxonomic Relation Extraction
Nonetheless, the ”is-a” relations are not the only relations in ontologies. So, Task C
aims to ”identify non-taxonomic, semantic relations between types”. Training instances
are given for three subtasks C.1 - UMLS, C.2 - GO, and C.3 - FoodOn as:
f T askC
prompt(h, r, t) := (T h, r, Tt)
Where, Th and Tt are head and tail taxonomic types, respectively, and r is the non-
taxonomic semantic relation between them, chosen from a predefined setR of seman-
tic relations. Participants aimed to train a system to identify pairs of types, and then
classify pairs of types into semantic relations. The training phase involves types, re-
lations, and triples of semantic relations; the test phase requires applying the trained
system to predict semantically related triples from given types and the set of relations.
The caveat here is that we do not expect participant systems to infer a semantic
relation but rather establish semantically related types and classify their relation from
a known set of predetermined relations. This implies that any manual ontology spec-
ification task predetermines which semantic relations hold for the given ontology. In
an alternative scenario, where participants might have had to infer the semantic re-
lation, we realize that the possibilities of semantic relations might have been rather
vast. Hence we posit a more realistic task design by predetermining the possible set of
semantic relations.
3 Evaluation
There are two main evaluation phases for the challenge, which are the following:
• Few-shot testing phase. Each ontology selected for system training will be di-
vided into two parts: one part will be released for the training of the systems and
another part will be reserved for the testing of systems in this phase.
• Zero-shot testing phase. New ontologies that are unseen during training will be
introduced. The objective is to evaluate the generalizability and transferability of
the LLMs developed in this challenge.
For evaluation, we used the challenge datasets [8] – available at challenge GitHub 2
repository – with standard evaluation metrics used for all tasks. Given G(i) as a set of
ground truth labels for sample i, and P(i) as a set of predicted labels for sample i, the
precision P, recall R, and F1-score F 1 are being calculated as follows:
P =
P
i |G(i) ∩ P (i)|
P
i |P(i)| , R =
P
i |G(i) ∩ P (i)|
P
i |G(i)| , F 1 = 2 × P × R
P + R
With precision, we assessed the percentage of the returned related pairs, while recall
was used to measure the proportion of correct pairs that were accurately retrieved.
In the end, the F1-score was calculated as the harmonic mean of precision and re-
call, serv

## 한국어 번역

LLMs4OL 2024: 제23회 ISWC에서 온톨로지 학습 챌린지를 위한 최초의 대규모 언어 모델
LLMs4OL 2024 작업 개요
https://doi.org/10.52825/ocp.v4i.2473
© 저자. 이 저작물은 Creative Commons Attribution 4.0 국제 라이선스에 따라 라이선스가 부여됩니다.
게시일: 2024년 10월 2일
LLMs4OL 2024 개요: 최초의 대규모 언어
온톨로지 학습 과제를 위한 모델
Hamed Babaei Giglou, Jennifer D'Souza, S¨oren Auer
TIB 라이프니츠 과학기술정보센터, 독일 하노버
{hamed.babaei, jennifer.dsouza, auer}@tib.eu
*서신: Hamed Babaei Giglou, hamed.babaei@tib.eu
개요: 이 문서는 LLMs4OL 2024의 개요를 설명합니다.
게이지 모델
 온톨로지 학습 챌린지. LLMs4OL은 커뮤니티 개발입니다.
멘티 이니셔티브
 제23회 국제시맨틱웹컨퍼런스(ISWC)와 동시 개최 
온톨로지 학습(OL)에서 대규모 언어 모델(LLM)의 잠재력을 탐색합니다. 
중요한 과정
 구조화된 지식으로 웹을 강화하여 상호 운용성을 향상시킵니다.
ity. LLM을 활용하여 이 과제는 이해와 혁신을 발전시키는 것을 목표로 합니다. 
OL에서는 보다 지능적이고 사용자 친화적인 웹 서비스를 만들기 위해 Semantic Web의 목표에 부합합니다.
친절한 웹. 이 백서에서는 LLMs4OL 2024년판에 대한 개요를 제공합니다. 
Challenge1을 작성하고 기여를 요약합니다.
키워드: LLMs4OL 챌린지, 온톨로지 학습, 대규모 언어 모델
1 소개
시맨틱 웹은 구조화된 지식과 메타데이터를 통해 현재의 웹을 풍부하게 만드는 것을 목표로 합니다.
다양한 시스템 전반에 걸쳐 향상된 상호 운용성과 이해를 가능하게 합니다. 
이러한 노력의 핵심에는 온톨로지 학습(OL)이 있습니다. 
구조화되지 않은 데이터에서 구조화된 지식을 추출합니다. [1], 구성에 필수적입니다.
시맨틱 웹을 뒷받침하는 동적 온톨로지를 제공합니다. 대형의 등장 
GPT -3 [2] 및 GPT -4 [3]와 같은 언어 모델(LLM)은 자연 언어에 혁명을 일으켰습니다.
게이지 처리(NLP) 등의 작업 전반에 걸쳐 놀라운 성능을 발휘합니다. 
언어 번역, 질문 답변 및 텍스트 생성. 이 모델은 동등합니다.
광범위한 소스에서 기존 텍스트 지식을 결정화하는 데 특히 능숙하며,  
공유된 개념을 추출하는 것이 목표인 OL에 잠재적으로 가치가 있습니다.
다양한 입력으로부터 개념과 관계를 통합합니다 [4] . 소개 
따라서 LLM은 자신의 분야에 대한 탐구를 포함하여 새로운 연구 방법을 열었습니다. 
OL 프로세스 자동화의 잠재력.
ISWC 2023 연구 트랙 절차에 게시된 이전 작업에서 
"LLMs4OL: 온톨로지 학습을 위한 대규모 언어 모델"[5]은 주목할만한 분야로 표시되었습니다.
OL에서 LLM을 채용하는 것에 대한 반응을 통해 자동화의 잠재력을 보여줍니다. 
시맨틱 웹을 위한 지식 획득 및 표현. 이 재검토를 바탕으로
검색, 1위
 온톨로지 학습 과제를 위한 대규모 언어 모델
1https://sites.google.com/view/llms4ol
3

Babaei Giglouet al. | Open Conf Proc 4(2024) ”LLMs4OL 2024: 온톨로지 학습을 위한 최초의 대규모 언어 모델
제23회 ISWC에 도전하세요”
코퍼스
준비
개념화
 (1) 용어 유형 지정 (2) 유형 분류 (3) 관계 추출
용어
추출
공리
발견
작업 A: 용어 입력 작업 B: 유형 분류 작업 C: 관계 추출 
온톨로지 학습
LLM4OL
그림 1. LLMs4OL 작업 패러다임은 온톨로지 학습을 위한 엔드투엔드 프레임워크입니다. 세 가지
이전 리소스를 기반으로 LLMs4OL 2024 챌린지에서 경험적으로 검증된 OL 작업
검색 [5]는 더 큰 LLMs4OL 패러다임에 맞춰 파란색 화살표 안에 표시됩니다.
제23회 ISWC 2024(제1회 LLMs4OL Challenge @ ISWC 2024)가
지역사회 발전을 촉구합니다. LLMs4OL 챌린지를 통해 우리는
OL에서 LLM 사용을 검증하고 확장하는 데 커뮤니티 전체가 참여합니다. 이
이니셔티브는 의미 체계 내에서 LLM의 역할에 대한 이해를 향상시킬 준비가 되어 있습니다.
확장 가능하고 정확한 개발을 위한 혁신과 협업을 장려하는 웹
온톨로지 학습 방법.
LLMs4OL은 세 가지 OL 작업, 작업 A – 용어 입력, 작업 B – 분류로 구성됩니다.
발견 및 작업 C – 비분류학적 관계 추출. 모두 참여하면서
LLMs4OL 2024 챌린지의 세 가지 작업은 바람직하다고 규정되어 있지만 필수는 아닙니다.
토리. 따라서 참가자는 작업 A, B, C, 작업 A 및 B에만 등록하도록 선택합니다.
작업 A와 C, 또는 작업 B와 C. 또한 참가자는 다음을 구현해야 합니다.
LLM 기반 솔루션에서는 LLM 프롬프트 방법에 어떠한 제한도 두지 않았습니다.
ods. 예를 들어, 사용자는 다음에서 추가 컨텍스트 정보를 가져오도록 선택할 수 있습니다.
훈련 및 테스트 인스턴스를 강화하는 World Wide Web. 철저하게 탐구하기 위해
OL에 대한 LLM의 잠재력을 고려하여 우리는 두 가지 평가를 중심으로 과제를 구성했습니다.
단계: (1) 퓨샷 테스트 단계 및 (2) 제로샷 테스트 단계. 이를 통해
우리는 LLM의 역량에 대한 지속적인 담론에 기여하는 것을 목표로 합니다.
특히 OL의 맥락에서 향상을 위한 잠재력에 대한 통찰력을 제공합니다.
시맨틱 웹. 따라서 이 문서의 나머지 부분에서는 도전과제에 대해 자세히 설명합니다.
사용되는 LLM, 참가자 기여 및 결과.
2 LLM4OL 2024 작업
LLMs4OL 2024 챌린지에서 우리는 다음과 같은 세 가지 주요 작업을 구성했습니다.
다음으로 구성된 온톨로지 프리미티브[6]를 중심으로 구성됩니다. 1. 문자열 세트
개념적 유형에 대한 용어적 어휘 항목 L을 설명합니다. 2. 일련의 개념-
실제 유형 T; 3. 계층 구조 HT의 유형 분류; 4. 비분류학적 집합
Heterarchy로 배열된 도메인 및 범위 제한으로 설명되는 관계 R
관계 HR; 그리고 5. 다음에 대한 추가적인 제약을 설명하는 일련의 공리 A
온톨로지와 암묵적인 사실을 명시적으로 만듭니다.
이러한 기본 요소를 해결하기 위해 OL [7]의 작업은 다음과 같습니다. 1) 코퍼스 준비 – 수집
온톨로지를 구축하기 위한 소스 텍스트를 작성합니다. 2) 용어 추출 - 관련 추출
텍스트의 용어. 3) 용어 유형화 – 유사한 용어를 개념 유형으로 그룹화합니다.
4) 분류 구성 - 유형 간 "is-a" 계층 구조를 설정합니다. 5) 관계-
tionship 추출 – 유형 간 "is-a" 이상의 의미 관계를 추출합니다. 6)
공리 발견 – 온톨로지에 대한 제약 규칙을 찾는 것입니다. 이러한 작업은
그림 1에 묘사된 LLMs4OL 작업 패러다임. 코퍼스 준비를 가정
단계는 커뮤니티에 공개적으로 공개된 온톨로지를 재사용하여 수행됩니다.
LLMs4OL 챌린지의 첫 번째 버전에서는 다음 세 가지 주요 작업을 수행합니다.
4

Babaei Giglouet al. | Open Conf Proc 4(2024) ”LLMs4OL 2024: 온톨로지 학습을 위한 최초의 대규모 언어 모델
제23회 ISWC에 도전하세요”
표 1. LLMs4OL 2024 챌린지, 하위 작업, 도메인, 하위 작업당 참가자 수 및 평가
이온화 단계.
작업 하위 작업 도메인 참가자 단계
에이
A.1 - WordNet 어휘 의미론 7
퓨샷
A.2 - GeoNames 지리적 위치 5
A.3 - UMLS - NCI
생물의학
5
A.3 - UMLS - MEDCIN 4
A.3 - UMLS - SNOMEDCT US 4
A.4 - GO - 생물학적 과정
생물학적
5
A.4 - GO - 셀룰러 구성 요소 5
A.4 - GO - 분자 기능 5
A.5 - DBO 일반 지식 2 Zero-shotA.6 - FoodOn 음식 2
비
B.1 - GeoNames 지리적 위치 5
Few-shotB.2 - Schema.org 웹 콘텐츠 유형 3
B.3 - UMLS 생물의학 3
B.4 - GO 생물학적 1
B.5 - DBO 일반 지식 2 Zero-shotB.6 - FoodOn 음식 1
C
C.1 - UMLS 생물의학 2 Few-shotC.2 - GO 생물학적 0
C.3 - FoodOn 음식 0 제로샷
2.1 작업 A – 용어 입력
표 1은 어휘와 같은 6개의 개별 도메인에 걸쳐 작업 A에 대한 10개의 하위 작업을 보여줍니다.
의미론, 지리적 위치, 생물의학, 생물학, 일반 지식 및
음식 도메인. 이 작업은 "주어진 어휘에 대한 일반화된 유형을 발견하는 것"으로 정의됩니다.
용어”. 이 작업을 위해 각 온톨로지에 대해 참가자에게는 정의된 교육 인스턴스가 제공됩니다.
형식주의를 따른다.
f T에게 물어보세요A
프롬프트(L) := [S ?]. ([엘], [티 ])
여기서 S는 선택적인 문맥 문장(소스 온톨로지에서 사용 가능한 경우)이고, L은
어휘 용어가 프롬프트되고 T는 개념 용어 유형입니다. 테스트 단계에서는 다음을 입력합니다.
숨겨져 있으며 참가자는 훈련된 모델을 사용하여 주어진 용어에 대해 예측합니다.
2.2 작업 B – 분류 발견
개념 유형별로 용어를 그룹화한 후 Task B에서는 해당 유형에 대한 목표를 설정합니다.
"유형 간 분류학적 계층 구조를 발견합니다", 여기서 유형 간 계층 구조는
"is-a" 관계로 정의됩니다. 참가자는 6가지 개별 교육 인스턴스를 받습니다.
하위 작업(표 1에 설명됨)은 다음과 같습니다.
f T 물어봐B
프롬프트(a, b) := (T a, T b)
여기서 Ta는 Tb의 상위(수퍼클래스)이고 Tb는 Ta의 하위(하위 클래스)입니다. 는
목표는 유형 간의 분류를 올바르게 식별하도록 시스템을 훈련시키는 것입니다. 훈련
데이터세트에는 용어 유형과 분류학적으로 관련된 유형 쌍이 포함됩니다. 테스트 단계에서는
참가자는 용어 유형만 사용하고 훈련된 모델을 사용하여 식별해야 합니다.
올바른 분류학적 관계(유형 쌍). 학습 및 테스트 단계의 유형
상호 배타적입니다. 또한 테스트 단계에는 참가자가 필요합니다.
슈퍼클래스의 순서를 따르는 유형 쌍을 반환하기 위해 출력을 사후 처리합니다.
하위 클래스 관련 유형.
5

Babaei Giglouet al. | Open Conf Proc 4(2024) ”LLMs4OL 2024: 온톨로지 학습을 위한 최초의 대규모 언어 모델
제23회 ISWC에 도전하세요”
2.3 작업 C – 비분류학적 관계 추출
그럼에도 불구하고 "is-a" 관계가 온톨로지의 유일한 관계는 아닙니다. 그래서 태스크 C
"유형 간의 비분류학적, 의미론적 관계를 식별"하는 것을 목표로 합니다. 훈련 인스턴스
세 가지 하위 작업 C.1 - UMLS, C.2 - GO 및 C.3 - FoodOn에 대해 다음과 같이 제공됩니다.
f T에게 물어보세요C
프롬프트(h, r, t) := (T h, r, Tt)
여기서 Th와 Tt는 각각 머리와 꼬리 분류 유형이고 r은 비-
미리 정의된 의미 집합R에서 선택된 그들 사이의 분류학적 의미 관계
틱 관계. 참가자들은 유형 쌍을 식별하는 시스템을 훈련하는 것을 목표로 삼았습니다.
유형 쌍을 의미 관계로 분류합니다. 훈련 단계에는 유형이 포함됩니다.
관계 및 의미론적 관계의 삼중; 테스트 단계에서는 훈련된 기술을 적용해야 합니다.
주어진 유형과 관계 세트로부터 의미상 관련된 트리플을 예측하는 시스템입니다.
여기서 주의할 점은 참가자 시스템이 의미론을 추론할 것으로 기대하지 않는다는 것입니다.
오히려 의미적으로 관련된 유형을 설정하고 그 관계를 다음과 같이 분류합니다.
미리 결정된 관계의 알려진 집합. 이는 모든 수동 온톨로지 사양이
화 작업은 주어진 온톨로지에 대해 어떤 의미론적 관계가 유지되는지 미리 결정합니다. 에서
참가자가 의미론적 재검토를 추론해야 했던 대체 시나리오
따라서 우리는 의미론적 관계의 가능성이 오히려
광대하다. 따라서 우리는 가능한 세트를 미리 결정하여 보다 현실적인 작업 설계를 가정합니다.
의미론적 관계.
3 평가
챌린지에는 다음과 같은 두 가지 주요 평가 단계가 있습니다.
• 퓨샷 테스트 단계. 시스템 교육을 위해 선택된 각 온톨로지는 다음과 같습니다.
두 부분으로 나누어져 있습니다. 한 부분은 시스템 교육용으로 출시될 예정이며,
이 단계의 시스템 테스트를 위해 다른 부분이 예약됩니다.
• 제로샷 테스트 단계. 훈련 중에 보이지 않는 새로운 온톨로지는
소개되었습니다. 목표는 일반화 가능성과 전달 가능성을 평가하는 것입니다.
이 과제를 통해 LLM이 개발되었습니다.
평가를 위해 챌린지 GitHub 2에서 사용할 수 있는 챌린지 데이터세트[8]를 사용했습니다.
저장소 – 모든 작업에 사용되는 표준 평가 지표가 있습니다. G(i)를 다음의 집합으로 가정하면
샘플 i에 대한 정답 레이블, 샘플 i에 대한 예측 레이블 집합인 P(i)
정밀도 P, 재현율 R 및 F1 점수 F 1은 다음과 같이 계산됩니다.
피 =
피
나는 |G(i) ∩ P(i)|
피
나는 |P(i)| , R =
피
나는 |G(i) ∩ P(i)|
피
나는 |G(i)| , F1 = 2 × P × R
P + R
우리는 반환된 관련 쌍의 백분율을 정확하게 평가했으며,
정확하게 검색된 올바른 쌍의 비율을 측정하는 데 사용되었습니다.
결국 F1-점수는 정밀도와 재검토의 조화평균으로 계산되었습니다.
전화하다, 봉사하다
