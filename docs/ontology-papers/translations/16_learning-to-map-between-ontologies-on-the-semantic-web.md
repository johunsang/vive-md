# [16] 시맨틱 웹에서 온톨로지 간 매핑 학습

- 영문 제목: Learning to map between ontologies on the semantic web
- 연도: 2002
- 원문 링크: https://doi.org/10.1145/511446.511532
- DOI: 10.1145/511446.511532
- 원문 저장 상태: not_downloaded
- 원문 파일: N/A
- 번역 상태: ok

## 원문(추출 텍스트)

Ontologies play a prominent role on the Semantic Web. They make possible the widespread publication of machine understandable data, opening myriad opportunities for automated information processing. However, because of the Semantic Web's distributed nature, data on it will inevitably come from many different ontologies. Information processing across ontologies is not possible without knowing the semantic mappings between their elements. Manually finding such mappings is tedious, error-prone, and clearly not possible at the Web scale. Hence, the development of tools to assist in the ontology mapping process is crucial to the success of the Semantic Web.We describe glue, a system that employs machine learning techniques to find such mappings. Given two ontologies, for each concept in one ontology glue finds the most similar concept in the other ontology. We give well-founded probabilistic definitions to several practical similarity measures, and show that glue can work with all of them. This is in contrast to most existing approaches, which deal with a single similarity measure. Another key feature of glue is that it uses multiple learning strategies, each of which exploits a different type of information either in the data instances or in the taxonomic structure of the ontologies. To further improve matching accuracy, we extend glue to incorporate commonsense knowledge and domain constraints into the matching process. For this purpose, we show that relaxation labeling, a well-known constraint optimization technique used in computer vision and other fields, can be adapted to work efficiently in our context. Our approach is thus distinguished in that it works with a variety of well-defined similarity notions and that it efficiently incorporates multiple types of knowledge. We describe a set of experiments on several real-world domains, and show that glue proposes highly accurate semantic mappings.

## 한국어 번역

온톨로지는 시맨틱 웹에서 중요한 역할을 합니다. 이를 통해 기계가 이해할 수 있는 데이터의 광범위한 게시가 가능해지며 자동화된 정보 처리를 위한 무수한 기회가 열립니다. 그러나 시맨틱 웹의 분산 특성으로 인해 이에 대한 데이터는 필연적으로 다양한 온톨로지에서 나옵니다. 온톨로지 전반에 걸친 정보 처리는 해당 요소 간의 의미 매핑을 알지 못하면 불가능합니다. 이러한 매핑을 수동으로 찾는 것은 지루하고 오류가 발생하기 쉬우며 웹 규모에서는 확실히 불가능합니다. 따라서 온톨로지 매핑 프로세스를 지원하는 도구의 개발은 시맨틱 웹의 성공에 매우 중요합니다. 우리는 그러한 매핑을 찾기 위해 기계 학습 기술을 사용하는 시스템인 글루에 대해 설명합니다. 두 개의 온톨로지가 주어지면 하나의 온톨로지의 각 개념에 대해 글루는 다른 온톨로지에서 가장 유사한 개념을 찾습니다. 우리는 몇 가지 실제 유사성 측정에 대해 근거가 있는 확률론적 정의를 제공하고 접착제가 모든 측정에 사용할 수 있음을 보여줍니다. 이는 단일 유사성 측정을 다루는 대부분의 기존 접근 방식과 대조됩니다. Glue의 또 다른 주요 특징은 여러 학습 전략을 사용한다는 것입니다. 각 전략은 데이터 인스턴스 또는 온톨로지의 분류 구조에서 서로 다른 유형의 정보를 활용합니다. 매칭 정확도를 더욱 향상시키기 위해 글루를 확장하여 상식적인 지식과 도메인 제약 조건을 매칭 프로세스에 통합합니다. 이를 위해 우리는 컴퓨터 비전 및 기타 분야에서 사용되는 잘 알려진 제약 최적화 기술인 완화 라벨링이 우리 상황에서 효율적으로 작동하도록 조정할 수 있음을 보여줍니다. 따라서 우리의 접근 방식은 잘 정의된 다양한 유사성 개념과 함께 작동하고 여러 유형의 지식을 효율적으로 통합한다는 점에서 구별됩니다. 우리는 여러 실제 영역에 대한 일련의 실험을 설명하고 Glue가 매우 정확한 의미 매핑을 제안한다는 것을 보여줍니다.
