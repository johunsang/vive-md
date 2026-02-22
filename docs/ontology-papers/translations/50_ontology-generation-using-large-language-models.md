# [50] 대규모 언어모델을 이용한 온톨로지 생성

- 영문 제목: Ontology Generation Using Large Language Models
- 연도: 2025
- 원문 링크: https://doi.org/10.1007/978-3-031-94575-5_18
- DOI: 10.1007/978-3-031-94575-5_18
- 원문 저장 상태: html_saved
- 원문 파일: /Volumes/SAMSUNG/apps/projects/vive-md/docs/ontology-papers/originals/50_ontology-generation-using-large-language-models.html
- 번역 상태: partial_translated

## 원문(추출 텍스트)

Ontology Generation Using Large Language Models | Springer Nature Link
Skip to main content
Advertisement
Log in
Menu
Find a journal
Publish with us
Track your research
Search
Saved research
Cart
Home
The Semantic Web
Conference paper
Ontology Generation Using Large Language Models
Conference paper
First Online:
01 June 2025
pp 321–341
Cite this conference paper
The Semantic Web
(ESWC 2025)
Anna Sofia Lippolis
16
,
17
,
Mohammad Javad Saeedizade
18
,
Robin Keskisärkkä
18
,
Sara Zuppiroli
17
,
Miguel Ceriani
17
,
Aldo Gangemi
16
,
17
,
Eva Blomqvist
18
&
…
Andrea Giovanni Nuzzolese
17
Show authors
Part of the book series:
Lecture Notes in Computer Science
((LNCS,volume 15718))
Included in the following conference series:
European Semantic Web Conference
1091
Accesses
14
Citations
6
Altmetric
Abstract
The ontology engineering process is complex, time-consuming, and error-prone, even for experienced ontology engineers. In this work, we investigate the potential of Large Language Models (LLMs) to provide effective OWL ontology drafts directly from ontological requirements described using user stories and competency questions. Our main contribution is the presentation and evaluation of two new prompting techniques for automated ontology development: Memoryless CQbyCQ and Ontogenia. We also emphasize the importance of three structural criteria for ontology assessment, alongside expert qualitative evaluation, highlighting the need for a multi-dimensional evaluation in order to capture the quality and usability of the generated ontologies. Our experiments, conducted on a benchmark dataset of ten ontologies with 100 distinct Competency Questions (CQs) and 29 different user stories, compare the performance of three LLMs using the two prompting techniques. The results demonstrate improvements over the current state-of-the-art in LLM-supported ontology engineering. More specifically, the model
OpenAI o1-preview
with Ontogenia produces ontologies of sufficient quality to meet the requirements of ontology engineers, significantly outperforming novice ontology engineers in modelling ability. However, we still note some common mistakes and variability of result quality, which is important to take into account when using LLMs for ontology authoring support. We discuss these limitations and propose directions for future research.
A. S. Lippolis and M. J. Saeedizade—Equal contribution.
This is a preview of subscription content,
log in via an institution
to check access.
Access this chapter
Log in via an institution
Subscribe and save
Springer+
from €37.37 /Month
Starting from 10 chapters or articles per month
Access and download chapters and articles from more than 300k books and 2,500 journals
Cancel anytime
View plans
Buy Now
Chapter
EUR 29.95
Price includes VAT (Korea(Rep.))
Available as PDF
Read on any device
Instant download
Own it forever
Buy Chapter
eBook
EUR 53.49
Price includes VAT (Korea(Rep.))
Available as EPUB and PDF
Read on any device
Instant download
Own it forever
Buy eBook
Softcover Book
EUR 65.99
Price excludes VAT (Korea(Rep.))
Compact, lightweight edition
Dispatched in 3 to 5 business days
Free shipping worldwide -
see info
Buy Softcover Book
Tax calculation will be finalised at checkout
Purchases are for personal use only
Institutional subscriptions
Similar content being viewed by others
The Role of Generative AI in Competency Question Retrofitting
Chapter
© 2025
Navigating Ontology Development with Large Language Models
Chapter
© 2024
Ontogenia: Ontology Generation with Metacognitive Prompting in Large Language Models
Chapter
© 2025
Explore related subjects
Discover the latest articles, books and news in related subjects, suggested using machine learning.
Computational Linguistics
Ontology
Knowledge Management
Machine Translation
Natural Language Processing (NLP)
Open Source
Knowledge Graphs and Semantic Data Integration
Notes
1.
Supplementary material such as datasets, prompts and code is available at
https://github.com/dersuchendee/Onto-Generation
.
2.
E.g. see ESWC
https://2024.eswc-conferences.org/
, EKAW
https://event.cwi.nl/ekaw2024/cfp.html
and ISWC
https://iswc2024.semanticweb.org/
.
3.
https://polifonia-project.eu/
.
4.
https://ontodeside.eu
.
5.
https://cordis.europa.eu/project/id/231527
.
6.
We did not compare to the original Ontogenia paper [
24
] as, given its noted shortcomings, the technique has been revised and used for the decomposed prompting technique.
7.
http://ontologydesignpatterns.org/
.
8.
The “not adequate” assessment combines two judgments by the KE experts, i.e. a clear “no” where the CQ is not modelled, and a “maybe” category where the ontology simply does not allow for accurate assessment of the CQ, for instance, due to usability issues, naming etc.
References
Alharbi, R., de Berardinis, J., Grasso, F., Payne, T., Tamma, V.: Characteristics and desiderata for competency question benchmarks. In: The Semantic Web - ISWC 2024: 23rd International Semantic Web Conference, Baltimore, MD, USA, 11–15 November 2024, Proceedings (2024)
Google Scholar
Ali, R., et al.: Performance of chatgpt, gpt-4, and google bard on a neurosurgery oral boards preparation question bank. Neurosurgery
93
(5), 1090–1098 (2023).
https://doi.org/10.1227/neu.0000000000002551
Article
Google Scholar
Allen, B., Groth, P.: A benchmark for the detection of metalinguistic disagreements between llms and knowledge graphs. In: The Semantic Web - ISWC 2024: 23rd International Semantic Web Conference, Baltimore, MD, USA, 11–15 November 2024, Proceedings (2024)
Google Scholar
Babaei Giglou, H., D’Souza, J., Auer, S.: Llms4ol: large language models for ontology learning. In: Payne, T.R., et al. (eds.) The Semantic Web - ISWC 2023, pp. 408–427. Springer, Cham (2023).
https://doi.org/10.1007/978-3-031-47240-4_22
Chapter
Google Scholar
Balloccu, S., Schmidtová, P., Lango, M., Dusek, O.: Leak, cheat, repeat: data contamination and evaluation malpractices in closed-source LLMs. In: Graham, Y., Purver, M. (eds.) Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics, vol. 1: Long Papers, pp. 67–93. Association for Computational Linguistics, St. Julian’s (2024).
https://aclanthology.org/2024.eacl-long.5
Blomqvist, E., Hammar, K., Presutti, V.: Engineering ontologies with patterns-the extreme design methodology. In: Ontology Engineering with Ontology Design Patterns. IOS Press (2016)
Google Scholar
Blomqvist, E., Presutti, V., Daga, E., Gangemi, A.: Experimenting with eXtreme design. In: Cimiano, P., Pinto, H.S. (eds.) EKAW 2010. LNCS (LNAI), vol. 6317, pp. 120–134. Springer, Heidelberg (2010).
https://doi.org/10.1007/978-3-642-16438-5_9
Chapter
Google Scholar
Blomqvist, E., Sandkuhl, K.: Patterns in ontology engineering: classification of ontology patterns. In: Proceedings of the Seventh International Conference on Enterprise Information Systems, vol. 3: ICEIS, pp. 413–416. INSTICC, SciTePress (2005).
https://doi.org/10.5220/0002518804130416
Blomqvist, E., Seil Sepour, A., Presutti, V.: Ontology testing - methodology and tool. In: ten Teije, A., Völker, J., Handschuh, S., Stuckenschmidt, H., d’Acquin, M., Nikolov, A., Aussenac-Gilles, N., Hernandez, N. (eds.) EKAW 2012. LNCS (LNAI), vol. 7603, pp. 216–226. Springer, Heidelberg (2012).
https://doi.org/10.1007/978-3-642-33876-2_20
Chapter
Google Scholar
Brown, T., et al.: Language models are few-shot learners. In: Larochelle, H., Ranzato, M., Hadsell, R., Balcan, M., Lin, H. (eds.) Advances in Neural Information Processing Systems, vol. 33, pp. 1877–1901. Curran Associates, Inc. (2020).
https://proceedings.neurips.cc/paper_files/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf
Chu, Z., et al.: A survey of chain of thought reasoning: advances, frontiers and future. arXiv preprint
arXiv:2309.15402
(2023)
Fathallah, N., Das, A., Giorgis, S.D., Poltronieri, A., Haase, P., Kovriguina, L.: Neon-gpt: a large language model-powered pipeline for ontology learning. In: European Semantic Web Conference, pp. 36–50. Springer, Heidelberg (2024).
https://doi.org/10.1007/978-3-031-78952-6_4
Fathallah, N., Staab, S., Algergawy, A.: Llms4life: large language models for ontology learning in life sciences (2024)
Google Scholar
Fernández, M., Gómez-Pérez, A., Juristo, N.: Methontology: from ontological art towards ontological engineering. In: Proceedings of the AAAI97 Spring Symposium Series on Ontological Engineering (1997)
Google Scholar
Frey, J., Meyer, L.P., Brei, F., Grunder-Fahrer, S., Martin, M.: Assessing the evolution of llm capabilities for knowledge graph engineering in 2023. In: Proceedings of the ESWC2024 Special Track: Large Language Models for Knowledge Engineering (to appear) (2024)
Google Scholar
Gangemi, A.: Ontology design patterns for semantic web content. In: Gil, Y., Motta, E., Benjamins, V.R., Musen, M.A. (eds.) ISWC 2005. LNCS, vol. 3729, pp. 262–276. Springer, Heidelberg (2005).
https://doi.org/10.1007/11574620_21
Chapter
Google Scholar
Gangemi, A., Nuzzolese, A.G.: Logic augmented generation. J. Web Semant.
85
, 100859 (2025)
Article
Google Scholar
Garcez, A.D., Lamb, L.C.: Neurosymbolic AI: the 3 rd wave. Artif. Intell. Rev.
56
(11), 12387–12406 (2023)
Google Scholar
Garijo, D., Poveda-Villalón, M., Amador-Domínguez, E., Wang, Z., Garía-Castro, R., Corcho, O.: Llms for ontology engineering: a landscape of tasks and benchmarking challenges. In: The Semantic Web - ISWC 2024: 23rd International Semantic Web Conference. Baltimore, MD, USA, 11–15 November 2024, Proceedings of the 23rd International Semantic Web Conference (ISWC 2024)
Google Scholar
He, Y., et al.: Deeponto: a python package for ontology engineering with deep learning. Semant. Web
15
(5), 1991–2004 (2024)
Article
Google Scholar
Hogan, A., et al.: Knowledge Graphs. Morgan & Claypool Publishers (2021)
Google Scholar
Keet, C.M., Khan, Z.C.: On the roles of competency questions in ontology engineering. In: International Conference on Knowledge Engineering and Knowledge Management, pp. 123–132. Springer, Heidelberg (2024).
https://doi.org/10.1007/978-3-031-77792-9_8
Khot, T., et al.: Decomposed prompting: a modular approach for solving complex tasks. In: The Eleventh International Conference on Learning Representations, ICLR 2023, Kigali, Rwanda, 1–5 May 2023 (2023)
Google Scholar
Lippolis, A.S., Ceriani, M., Zuppiroli, S., Nuzzolese, A.G.: Ontogenia: ontology generation with metacognitive prompting in large language models. In: European Semantic Web Conference, pp. 259–265. Springer, Heidelberg (2024).
https://doi.org/10.1007/978-3-031-78952-6_38
Lippolis, A.S., Lodi, G., Nuzzolese, A.G.: The water health open knowledge graph. Sci. Data
12
(1), 274 (2025)
Article
Google Scholar
Mateiu, P., Groza, A.: Ontology engineering with large language models. In: 2023 25th International Symposium on Symbolic and Numeric Algorithms for Scientific Computing (SYNASC), pp. 226–229. IEEE (2023)
Google Scholar
Peroni, S.: A simplified agile methodology for ontology development. In: Dragoni, M., Poveda-Villalón, M., Jimenez-Ruiz, E. (eds.) OWLED/ORE -2016. LNCS, vol. 10161, pp. 55–69. Springer, Cham (2017).
https://doi.org/10.1007/978-3-319-54627-8_5
Chapter
Google Scholar
Plu, J., Escobar, O.M., Trouillez, E., Gapin, A., Troncy, R.: A comprehensive benchmark for evaluating llm-generated ontologies. In: The Semantic Web - ISWC 2024: 23rd International Semantic Web Conference, Baltimore, MD, USA, 11–15 November 2024, Proceedings (2024)
Google Scholar
Poveda-Villalón, M., Gómez-Pérez, A., Suárez-Figueroa, M.C.: OOPS! (OntOlogy Pitfall Scanner!): an on-line tool for ontology evaluation. Int. J. Semant. Web Inf. Syst. (IJSWIS)
10
(2), 7–34 (2014)
Article
Google Scholar
Poveda-Villalón, M., Fernández-Izquierdo, A., Fernández-López, M., García-Castro, R.: Lot: an industrial oriented ontology engineering framework. Eng. Appl. Artif. Intell.
111
, 104755 (2022).
https://doi.org/10.1016/j.engappai.2022.104755
Article
Google Scholar
Presutti, V.,

## 한국어 번역

대규모 언어 모델을 사용한 온톨로지 생성 | 스프링거 네이처 링크
주요 콘텐츠로 건너뛰기
광고
로그인
메뉴
저널 찾기
우리와 함께 출판하세요
연구 추적
검색
저장된 연구
장바구니
홈
시맨틱 웹
컨퍼런스 페이퍼
대규모 언어 모델을 사용한 온톨로지 생성
컨퍼런스 페이퍼
첫 번째 온라인:
2025년 6월 1일
321~341쪽
이 컨퍼런스 논문을 인용하세요
시맨틱 웹
(ESWC 2025)
안나 소피아 리폴리스
16
,
17
,
모하마드 자바드 사에디자데
18
,
로빈 케스키세르카
18
,
사라 주피롤리
17
,
미구엘 세리아니
17
,
알도 간게미
16
,
17
,
에바 블롬크비스트
18
&
…
안드레아 조반니 누졸레세
17
작성자 표시
책 시리즈의 일부:
컴퓨터 과학 강의 노트
((LNCS, 15718권))
다음 컨퍼런스 시리즈에 포함되어 있습니다:
유럽 시맨틱 웹 컨퍼런스
1091
액세스
14
인용
6
알트메트릭
초록
온톨로지 엔지니어링 프로세스는 숙련된 온톨로지 엔지니어에게도 복잡하고 시간이 많이 걸리며 오류가 발생하기 쉽습니다. 이 작업에서 우리는 사용자 스토리와 역량 질문을 사용하여 설명된 존재론적 요구 사항에서 직접 효과적인 OWL 온톨로지 초안을 제공하기 위해 LLM(대형 언어 모델)의 잠재력을 조사합니다. 우리의 주요 기여는 자동화된 온톨로지 개발을 위한 두 가지 새로운 프롬프트 기술인 Memoryless CQbyCQ와 Ontogenia를 제시하고 평가하는 것입니다. 우리는 또한 전문가의 정성적 평가와 함께 온톨로지 평가를 위한 세 가지 구조적 기준의 중요성을 강조하며, 생성된 온톨로지의 품질과 유용성을 포착하기 위한 다차원적 평가의 필요성을 강조합니다. 100개의 고유한 역량 질문(CQ)과 29개의 다양한 사용자 스토리가 포함된 10개의 온톨로지 벤치마크 데이터세트에서 수행된 실험에서는 두 가지 프롬프트 기술을 사용하여 3개의 LLM의 성능을 비교합니다. 결과는 LLM 지원 온톨로지 엔지니어링의 현재 최첨단 기술에 비해 개선되었음을 보여줍니다. 좀 더 구체적으로 말하면, 모델
OpenAI o1-미리보기
Ontogenia를 사용하면 온톨로지 엔지니어의 요구 사항을 충족하기에 충분한 품질의 온톨로지를 생성하여 모델링 능력에서 초보 온톨로지 엔지니어를 훨씬 능가합니다. 그러나 우리는 온톨로지 저작 지원을 위해 LLM을 사용할 때 고려해야 할 몇 가지 일반적인 실수와 결과 품질의 다양성에 여전히 주목합니다. 우리는 이러한 한계를 논의하고 향후 연구 방향을 제안합니다.
A. S. Lippolis 및 M. J. Saeedizade—동등 기여.
구독 콘텐츠 미리보기 입니다,
기관을 통해 로그인
액세스를 확인합니다.
이 장에 액세스
기관을 통해 로그인
구독하고 저장하세요
스프링거+
₩37.37/월부터
매월 10개의 장 또는 기사부터 시작
30만 권 이상의 도서와 2,500개 이상의 저널에서 장과 기사에 액세스하고 다운로드하세요.
언제든지 취소
계획 보기
지금 구매
장
EUR 29.95
가격에는 VAT가 포함되어 있습니다(대한민국)
PDF로 사용 가능
모든 기기에서 읽기
즉시 다운로드
영원히 소유하세요
챕터 구매
전자책
EUR 53.49
가격에는 VAT가 포함되어 있습니다(대한민국)
EPUB 및 PDF로 사용 가능
모든 기기에서 읽기
즉시 다운로드
영원히 소유하세요
eBook 구매
소프트커버 책
EUR 65.99
VAT 별도 가격 (대한민국)
컴팩트하고 가벼운 버전
영업일 기준 3~5일 이내에 발송됩니다.
전 세계 무료 배송 -
정보 보기
소프트커버 도서 구매
세금 계산은 결제 시 완료됩니다.
구매는 개인 용도로만 가능합니다.
기관 구독
다른 사람들이 유사한 콘텐츠를 보고 있음
역량 질문 개조에서 생성적 AI의 역할
장
© 2025
대규모 언어 모델을 사용한 온톨로지 개발 탐색
장
© 2024
Ontogenia: 대규모 언어 모델에서 메타인지 프롬프트를 통한 온톨로지 생성
장
© 2025
관련 주제 탐색
머신러닝을 활용하여 추천되는 관련 주제의 최신 기사, 도서, 뉴스를 찾아보세요.
전산언어학
온톨로지
지식경영
기계 번역
자연어 처리(NLP)
오픈 소스
지식 그래프와 의미론적 데이터 통합
메모
1.
데이터 세트, 프롬프트 및 코드와 같은 보충 자료는 다음에서 확인할 수 있습니다.
https://github.com/dersuchendee/Onto-Generation
.
2.
예: ESWC 참조
https://2024.eswc-conferences.org/
, 이카우
https://event.cwi.nl/ekaw2024/cfp.html
그리고 ISWC
https://iswc2024.semanticweb.org/
.
3.
https://polifonia-project.eu/
.
4.
https://ontodeside.eu
.
5.
https://cordis.europa.eu/project/id/231527
.
6.
원래 Ontogenia 논문과 비교하지 않았습니다. [
24
] 알려진 단점을 고려하여 이 기술은 분해 프롬프트 기술에 대해 개정되어 사용되었습니다.
7.
http://ontologydesignpatterns.org/
.
8.
"적절하지 않음" 평가는 KE 전문가의 두 가지 판단, 즉 CQ가 모델링되지 않은 경우의 명확한 "아니오"와 온톨로지가 사용성 문제, 이름 지정 등으로 인해 CQ의 정확한 평가를 허용하지 않는 "아마도" 범주를 결합합니다.
참고자료
Alharbi, R., de Berardinis, J., Grasso, F., Payne, T., Tamma, V.: 역량 질문 벤치마크의 특성 및 요구 사항. In: 시맨틱 웹 - ISWC 2024: 제23회 국제 시맨틱 웹 컨퍼런스, 미국 메릴랜드주 볼티모어, 2024년 11월 11~15일, Proceedings(2024)
구글 학술검색
Ali, R. 등: 신경외과 구강 보드 준비 문제 은행에서 chatgpt, gpt-4 및 google bard의 성능. 신경외과
93
(5), 1090~1098(2023).
https://doi.org/10.1227/neu.0000000000002551
기사
구글 학술검색
Allen, B., Groth, P.: llms와 지식 그래프 간의 메타언어적 불일치를 탐지하기 위한 벤치마크입니다. In: 시맨틱 웹 - ISWC 2024: 제23회 국제 시맨틱 웹 컨퍼런스, 미국 메릴랜드주 볼티모어, 2024년 11월 11~15일, Proceedings(2024)
구글 학술검색
Babaei Giglou, H., D'Souza, J., Auer, S.: Llms4ol: 온톨로지 학습을 위한 대규모 언어 모델. In: Payne, T.R., et al. (eds.) 시맨틱 웹 - ISWC 2023, pp. 408–427. 스프링어, 참(2023).
https://doi.org/10.1007/978-3-031-47240-4_22
장
구글 학술검색
Balloccu, S., Schmidtová, P., Lango, M., Dusek, O.: 누출, 사기, 반복: 비공개 소스 LLM의 데이터 오염 및 평가 과실. In: Graham, Y., Purver, M. (eds.) 전산 언어학 협회 유럽 지부의 제18차 회의 진행, vol. 1: 긴 논문, 67~93페이지. 전산언어학협회, 세인트 줄리안스(2024).
https://aclanthology.org/2024.eacl-long.5
Blomqvist, E., Hammar, K., Presutti, V.: 패턴을 사용한 엔지니어링 온톨로지 - 극단적인 설계 방법론. In: 온톨로지 디자인 패턴을 사용한 온톨로지 엔지니어링. IOS 프레스(2016)
구글 학술검색
Blomqvist, E., Presutti, V., Daga, E., Gangemi, A.: eXtreme 디자인 실험. In: Cimiano, P., Pinto, H.S. (eds.) EKAW 2010. LNCS (LNAI), vol. 6317, pp. 120–134. 스프링거, 하이델베르그(2010).
https://doi.org/10.1007/978-3-642-16438-5_9
장
구글 학술검색
Blomqvist, E., Sandkuhl, K.: 온톨로지 공학의 패턴: 온톨로지 패턴 분류. In: 기업 정보 시스템에 관한 제7차 국제 회의 진행, vol. 3: ICEIS, 413~416페이지. INSTICC, SciTePress (2005).
https://doi.org/10.5220/0002518804130416
Blomqvist, E., Seil Sepour, A., Presutti, V.: 온톨로지 테스트 - 방법론 및 도구. In: ten Teije, A., Völker, J., Handschuh, S., Stuckenschmidt, H., d'Acquin, M., Nikolov, A., Aussenac-Gilles, N., Hernandez, N. (eds.) EKAW 2012. LNCS (LNAI), vol. 7603, pp. 216–226. 스프링거, 하이델베르그(2012).
https://doi.org/10.1007/978-3-642-33876-2_20
장
구글 학술검색
Brown, T., et al.: 언어 모델은 소수의 학습자입니다. In: Larochelle, H., Ranzato, M., Hadsell, R., Balcan, M., Lin, H. (eds.) 신경 정보 처리 시스템의 발전, vol. 33, 1877~1901페이지. 커란 어소시에이츠, Inc.(2020).
https://proceedings.neurips.cc/paper_files/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf
Chu, Z., et al.: 일련의 사고 추론에 대한 조사: 발전, 개척지 및 미래. arXiv 사전 인쇄
arXiv:2309.15402
(2023)
Fathallah, N., Das, A., Giorgis, S.D., Poltronieri, A., Haase, P., Kovriguina, L.: Neon-gpt: 온톨로지 학습을 위한 대규모 언어 모델 기반 파이프라인. In: European Semantic Web Conference, pp. 36–50. 스프링어, 하이델베르그(2024).
https://doi.org/10.1007/978-3-031-78952-6_4
Fathallah, N., Staab, S., Algergawy, A.: Llms4life: 생명과학에서 온톨로지 학습을 위한 대규모 언어 모델(2024)
구글 학술검색
Fernández, M., Gómez-Pérez, A., Juristo, N.: 방법론: 존재론적 예술에서 존재론적 공학으로. In: 존재론적 공학에 관한 AAAI97 봄 심포지엄 시리즈의 진행(1997)
구글 학술검색
Frey, J., Meyer, L.P., Brei, F., Grunder-Fahrer, S., Martin, M.: 2023년 지식 그래프 엔지니어링을 위한 llm 기능의 진화 평가. In: ESWC2024 특별 트랙의 진행: 지식 엔지니어링을 위한 대규모 언어 모델(출연 예정)(2024)
구글 학술검색
Gangemi, A.: 시맨틱 웹 콘텐츠를 위한 온톨로지 디자인 패턴. In: Gil, Y., Motta, E., Benjamins, V.R., Musen, M.A. (eds.) ISWC 2005. LNCS, vol. 3729, pp. 262–276. 스프링거, 하이델베르그(2005).
https://doi.org/10.1007/11574620_21
장
구글 학술검색
Gangemi, A., Nuzzolese, A.G.: 논리 증강 생성. J. 웹 의미.
85
, 100859 (2025)
기사
구글 학술검색
Garcez, A.D., Lamb, L.C.: 신경기호 AI: 세 번째 물결. Artif. 인텔. 목사님
56
(11), 12387–12406 (2023)
구글 학술검색
Garijo, D., Poveda-Villalon, M., Amador-Domínguez, E., Wang, Z., Garía-Castro, R., Corcho, O.: 온톨로지 엔지니어링을 위한 Llms: 작업 환경 및 벤치마킹 과제. In: 시맨틱 웹 - ISWC 2024: 제23회 국제 시맨틱 웹 컨퍼런스. 미국 메릴랜드주 볼티모어, 2024년 11월 11~15일, 제23차 국제 시맨틱 웹 컨퍼런스(ISWC 2024) 회의록
구글 학술검색
He, Y., et al.: Deeponto: 딥 러닝을 통한 온톨로지 엔지니어링을 위한 Python 패키지입니다. 의미. 웹
15
(5), 1991~2004년(2024년)
기사
구글 학술검색
Hogan, A. 등: 지식 그래프. 모건 앤 클레이풀 출판사(2021)
구글 학술검색
Keet, C.M., Khan, Z.C.: 온톨로지 엔지니어링에서 역량 질문의 역할. In: 지식 공학 및 지식 관리에 관한 국제 회의, pp. 123–132. 스프링어, 하이델베르그(2024).
https://doi.org/10.1007/978-3-031-77792-9_8
Khot, T., et al.: 분해된 프롬프트: 복잡한 작업을 해결하기 위한 모듈식 접근 방식. In: 학습 표현에 관한 제11차 국제 회의, ICLR 2023, 르완다 키갈리, 2023년 5월 1~5일(2023)
구글 학술검색
Lippolis, A.S., Ceriani, M., Zuppiroli, S., Nuzzolese, A.G.: Ontogenia: 대규모 언어 모델에서 메타인지 프롬프트를 통한 온톨로지 생성. In: European Semantic Web Conference, pp. 259–265. 스프링어, 하이델베르그(2024).
https://doi.org/10.1007/978-3-031-78952-6_38
Lippolis, A.S., Lodi, G., Nuzzolese, A.G.: 물 건강 공개 지식 그래프. 과학. 데이터
12
(1), 274(2025년)
기사
구글 학술검색
Mateiu, P., Groza, A.: 대규모 언어 모델을 사용한 온톨로지 엔지니어링. In: 2023년 제25차 과학 컴퓨팅을 위한 기호 및 수치 알고리즘에 관한 국제 심포지엄(SYNASC), pp. 226–229. IEEE(2023)
구글 학술검색
Peroni, S.: 온톨로지 개발을 위한 단순화된 애자일 방법론. In: Dragoni, M., Poveda-Villalon, M., Jimenez-Ruiz, E. (eds.) OWLED/ORE -2016. LNCS, vol. 10161, 55~69페이지. 스프링거, 참(2017).
https://doi.org/10.1007/978-3-319-54627-8_5
장
구글 학술검색
Plu, J., Escobar, O.M., Trouillez, E., Gapin, A., Troncy, R.: llm 생성 온톨로지를 평가하기 위한 포괄적인 벤치마크입니다. In: 시맨틱 웹 - ISWC 2024: 제23회 국제 시맨틱 웹 컨퍼런스, 미국 메릴랜드주 볼티모어, 2024년 11월 11~15일, Proceedings(2024)
구글 학술검색
Poveda-Villalon, M., Gómez-Pérez, A., Suárez-Figueroa, M.C.: 이런! (OntOlogy Pitfall Scanner!): 온톨로지 평가를 위한 온라인 도구입니다. 국제 J. Semant. 웹 정보 시스템. (IJSWIS)
10
(2), 7~34(2014)
기사
구글 학술검색
Poveda-Villalon, M., Fernández-Izquierdo, A., Fernández-López, M., García-Castro, R.: Lot: 산업 지향 온톨로지 엔지니어링 프레임워크. 영어 신청 Artif. 인텔.
111
, 104755(2022).
https://doi.org/10.1016/j.engappai.2022.104755
기사
구글 학술검색
프레수티, V.,
