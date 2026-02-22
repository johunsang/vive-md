# [44] OLaLa: 대규모 언어모델 기반 온톨로지 매칭

- 영문 제목: OLaLa: Ontology Matching with Large Language Models
- 연도: 2023
- 원문 링크: https://doi.org/10.1145/3587259.3627571
- DOI: 10.1145/3587259.3627571
- 원문 저장 상태: not_downloaded
- 원문 파일: N/A
- 번역 상태: ok

## 원문(추출 텍스트)

Ontology (and more generally: Knowledge Graph) Matching is a challenging task\nwhere information in natural language is one of the most important signals to\nprocess. With the rise of Large Language Models, it is possible to incorporate\nthis knowledge in a better way into the matching pipeline. A number of\ndecisions still need to be taken, e.g., how to generate a prompt that is useful\nto the model, how information in the KG can be formulated in prompts, which\nLarge Language Model to choose, how to provide existing correspondences to the\nmodel, how to generate candidates, etc. In this paper, we present a prototype\nthat explores these questions by applying zero-shot and few-shot prompting with\nmultiple open Large Language Models to different tasks of the Ontology\nAlignment Evaluation Initiative (OAEI). We show that with only a handful of\nexamples and a well-designed prompt, it is possible to achieve results that are\nen par with supervised matching systems which use a much larger portion of the\nground truth.\n

## 한국어 번역

온톨로지(더 일반적으로는 지식 그래프) 매칭은 자연어로 된 정보가 처리해야 할 가장 중요한\n신호 중 하나인 어려운 작업입니다. 대규모 언어 모델의 등장으로 이 지식을\n더 나은 방식으로 일치 파이프라인에 통합하는 것이 가능해졌습니다. 모델에 유용한 프롬프트를 생성하는 방법,\nKG의 정보를 프롬프트에서 공식화하는 방법,\n대형 언어 모델을 선택할지, 모델에 대한 기존 대응을\n제공하는 방법, 후보를 생성하는 방법 등과 같은\n다양한 결정을 내려야 합니다. 이 백서에서는\n여러 개방형 대형 언어 모델을 사용하여\n제로샷 및 퓨샷 프롬프트를 다양한 작업에 적용하여 이러한 질문을 탐색하는 프로토타입을 제시합니다. 온톨로지 정렬 평가 이니셔티브(OAEI)의\n 우리는 단지 소수의\n예제와 잘 설계된 프롬프트만으로 훨씬 더 많은 실제 정보를 사용하는 지도 매칭 시스템과\n동등한 결과를 얻을 수 있음을\n보여줍니다.\n
