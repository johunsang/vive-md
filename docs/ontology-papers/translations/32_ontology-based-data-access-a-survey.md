# [32] 온톨로지 기반 데이터 접근(OBDA) 서베이

- 영문 제목: Ontology-Based Data Access: A Survey
- 연도: 2018
- 원문 링크: https://doi.org/10.24963/ijcai.2018/777
- DOI: 10.24963/ijcai.2018/777
- 원문 저장 상태: pdf_saved
- 원문 파일: /Volumes/SAMSUNG/apps/projects/vive-md/docs/ontology-papers/originals/32_ontology-based-data-access-a-survey.pdf
- 번역 상태: partial_translated

## 원문(추출 텍스트)

Ontology-Based Data Access: A Survey
Guohui Xiao1, Diego Calvanese1, Roman Kontchakov2, Domenico Lembo3,
Antonella Poggi3, Riccardo Rosati3 and Michael Zakharyaschev2
1 KRDB Research Centre for Knowledge and Data, Free University of Bozen-Bolzano, Italy
2 Department of Computer Science and Information Systems, Birkbeck, University of London, UK
3 Dip. di Ing. Informatica Automatica e Gestionale, Sapienza Università di Roma, Italy
Abstract
We present the framework of ontology-based data
access, a semantic paradigm for providing a con-
venient and user-friendly access to data reposito-
ries, which has been actively developed and stud-
ied in the past decade. Focusing on relational
data sources, we discuss the main ingredients of
ontology-based data access, key theoretical results,
techniques, applications and future challenges.
1 Introduction
Ontology-based data access (OBDA, for short) is a seman-
tic technology that has been developed since the mid 2000s
[Poggi et al., 2008] with the aim of facilitating access to vari-
ous types of data sources. It originates in real-world scenarios
such as the one outlined below (seehttp://purl.org/slegge).
Example 1 Statoil (Equinor), a Norwegian multinational
oil&gas company, stores data in a large relational database
(DB) Slegge with about 1500 tables (and 1700 views). Prior
to making decisions on drilling wellbores, geologists at Sta-
toil need to gather relevant information. For instance, geolo-
gists’ information needs may include the following question:
(009) In my area of interest, return all pressure data tagged
with key stratigraphy information with understandable
QC attributes (and suitable for further ﬁltering).
Translating such an information need into the standard
database query language SQL is usually a big challenge for
geologists, who are not supposed to know how Slegge is or-
ganised. In fact, the main table for wellbores has 38 columns;
a four-table join with two additional ﬁlters is needed to ob-
tain formation pressure for a wellbore, and stratigraphic in-
formation requires a join with 5 more tables. Using existing
SQL templates and manipulating the answers is error prone,
and calling an IT expert is time-consuming (it can take days
or even weeks). OBDA offers a different approach to for-
malising and answering (009). Domain experts at Statoil
designed a Subsurface Exploration ontology (SE) that cap-
tures terms of the user information needs such as Wellbore,
hasFormationPressure, etc. IT experts wrote a mapping that
declaratively connects (through SQL queries) the ontology
predicates to the Slegge DB. The task of the geologist now is
to reformulate (009) in the vocabulary of SE—possibly using
a visual query interface such as OptiqueVQS1—as a query in
the W3C standard SPARQL2, which could look as follows:
SELECT ?w ?depth ?strat_unit WHERE {
?w a :Wellbore . ?w :hasMeasurement ?p .
?p a :Pressure . ?p :hasDepth ?depth
OPTIONAL { ?depth :inWellboreInterval ?strat_zone .
?strat_zone :hasUnit ?strat_unit } }.
This query retrieves all assignments to the variables ?w,
?depth, ?strat_unit in the SELECT clause that satisfy the con-
ditions of the WHERE clause. The latter consists of triple pat-
terns ‘subject-predicate-object’ (separated by dots) required
to match the data. The ﬁrst four triple patterns say that?w is an
instance of class Wellbore and has measurements, ?p, which
are instances of Pressure and have their ?depth recorded
by property hasDepth. The two triple patterns in OPTIONAL
return additional information, if available, about the strati-
graphic units ?strat_unit of the wellbore intervals for the
depth measurements. It is optional in the sense that the vari-
able ?strat_unit is assigned no value if the stratigraphic in-
formation is absent for the depth measurement.
An OBDA system would automatically rewrite this
SPARQL query using the ontology and mapping to a SQL
query over the DB, optimise it, and evaluate it by Slegge. q
In general, gathering information even from a company’s
DB is a hard task for non-IT-expert users. One of the main
reasons is that DBs are usually designed to serve applica-
tions: their structure and meaning are obscure for most of
the users; and the stored data is often redundant, mixed with
information only needed to support company processes, and
incomplete with respect to the business domain. Collecting,
integrating, reconciling and efﬁciently extracting information
from heterogeneous and autonomous data sources is regarded
as a major challenge, with ‘most companies [. . . ] capturing
only a fraction of the potential value from data and analytics’ .3
The OBDA paradigm addresses this issue by providing ac-
1http://optique-project.eu/training-programme/module-vqs
2http://www.w3.org/TR/sparql11-query
3“The age of analytics: competing in a data-driven world” , McK-
insey Global Institute, December 2016.
Proceedings of the Twenty-Seventh International Joint Conference on Artiﬁcial Intelligence (IJCAI-18)
5511

cess to the data layer, consisting of autonomous data sources
(e.g., DBs), through the mediation of a conceptual domain
view, given in terms of an ontology, and the use of a declara-
tive mapping between the data layer and the ontology. OBDA
users do not have to know details of the data sources and can
express their information needs as queries over the concep-
tual domain model. By applying knowledge representation
and automated reasoning techniques, an OBDA system uses
the ontology and mapping to reformulate the user queries into
standard DB queries that are executed directly by the database
management systems (DBMSs) of the sources. Thus, OBDA
relies upon both KR&R and DB technologies.
OBDA systems implementing this paradigm include Mas-
tro [Calvanese et al., 2011 ], Morph [Priyatna et al., 2014 ],
Ontop [Calvanese et al., 2017], Stardog4 and Ultrawrap [Se-
queda and Miranker, 2013]. They were adopted in many in-
dustrial projects and use cases, e.g., at Statoil and Siemens 5,
the Italian Ministry of Economy and Finance [Antonioli et
al., 2014], in projects on Smart Cities [López et al., 2015 ],
Electronic Health Records [Rahimi et al., 2014], and Manu-
facturing [Petersen et al., 2017].
Over the past decade, the theory and practice of OBDA
have become a hot topic in the areas of Knowledge Repre-
sentation (Description Logics), Semantic Technologies and
Databases, with numerous papers published in top CS jour-
nals (including AIJ, JACM, JAIR, TODS) and conferences,
and deep connections with such prominent disciplines as
Constraint Satisfaction and Circuit Complexity established.
In this brief survey, we introduce the framework of OBDA
and discuss main results, techniques and challenges. We ﬁrst
describe the classical OBDA framework in Section 2. Then,
in Section 3, we consider the process of query answering in
OBDA. In Section 4, we focus on mapping management and
analysis. In Section 5, we outline extensions of the classical
OBDA framework. Finally, Section 6 discusses some of the
most important research directions.
We assume the reader is familiar with the basics of
databases (at a standard undergraduate DB course level).
2 OBDA Framework
We begin by presenting a formal framework for OBDA,
distinguishing between the extensional (instance) and inten-
sional (schema) levels. The former is given by asource DBD
conforming to the data source schemaS (which typically in-
cludes integrity constraints), and the latter by an OBDA spec-
iﬁcationP = (O;M;S), whereO is an ontology,S a data
source schema and M a mapping from S toO (signatures
of the ontology and schema are disjoint). The role of O is
to provide the users with a high-level conceptual view of the
data and a convenient vocabulary for their queries; it can also
enrich incomplete data with background knowledge.
Example 2 The Subsurface Exploration ontology (SE) in
Example 1 contains, among others, the following axioms,
given in description logic (DL) syntax [Baader et al., 2017]:
4http://www.stardog.com
5http://optique-project.eu/results-downloads
FormationPressurev Pressure;
FormationPressureu HydrostaticPressurev?;
hasFormationPressurev hasMeasurement;
9hasFormationPressure :>v FormationPressure;
FormationPressurev9 hasDepth:Depth:
The ﬁrst three are inclusions between, respectively, unary
predicates (concepts in DL or classes in Semantic Web
parlance) and binary predicates (roles or properties); their
ﬁrst-order (FO) equivalents look as follows:
8x (FormationPressure(x)! Pressure(x));
8x (FormationPressure(x)^HydrostaticPressure(x)!? );
8xy (hasFormationPressure(x;y )! hasMeasurement(x;y )):
The fourth axiom restricts the range of hasFormationPres-
sure, while the ﬁfth involves existential quantiﬁcation:
8xy (hasFormationPressure(y;x )! FormationPressure(x));
8x (FormationPressure(x)!9y(hasDepth(x;y )^Depth(y))):
q
The mappingM inP speciﬁes how the ontology pred-
icates are populated by data from the source DB. In
the SE example, each wellbore, which is identiﬁed by
the column IDENTIFIER in the WELLBORE table, is given
an IRI (Internationalised Resource Identiﬁer) of the form
http://slegger.gitlab.io/data#Wellbore-n to represent the
wellbore in the ontology; in the sequel, we omit the preﬁxes
and shorten such IRIs to Wellbore-n. Then the mapping con-
necting SE to the Slegge database contains the assertion
SELECT IDENTIFIER FROM WELLBORE
WHERE REF_EXISTENCE_KIND = ’actual’
; Wellbore(iri("Wellbore-"; IDENTIFIER))
populating the class Wellbore with the answers to the SQL
query to the left of ;. In general, mapping assertions are
of the form '(x) ;  (x), where '(x) and  (x) are FO-
formulas in the signatures of S andO, respectively. In our
examples, we use SQL queries to conveniently represent the
formulas'(x) (recall that WELLBORE has 38 columns). A spe-
cial function iri (of variable arity) is used in  (x) to con-
struct IRIs for ontology objects: the parameters of iri are
strings and DB columns (variables in x), and the value of an
iri term is the concatenation of its parameter values.
The pair (P;D) of an OBDA speciﬁcationP and a source
DBD is called anOBDA instance. To deﬁne its semantics, let
M(D) be the minimal set of atoms in the signature ofO that
satisﬁes (a), for all '(x) ;  (x) inM and all tuples a
of constants inD such that'(a) holds inD. For example, in
the SE setting, if the table WELLBORE contains
IDENTIFIER REF_EXISTENCE_KIND . . .
16/1-29_S actual . . .
3/zero.alt1/8-5 actual . . .
33/1/zero.alt1-12 planned . . .
then the mapping will produce the following two ground
atoms (corresponding to ABox assertions or RDF triples):
Wellbore(Wellbore-16/1-29_S); Wellbore(Wellbore-3/zero.alt1/8-5):
We call an FO-structureI over the signature ofO a model of
(P;D) and writeIj = (P;D), ifIj =O andIj =M(D).
Thus, the two ground atoms above form an FO-structure that
Proceedings of the Twenty-Seventh International Joint Conference on Artiﬁcial Intelligence (IJCAI-18)
5512

is a model of our example OBDA instance. The additional
mapping assertion
SELECT WELLBORE.IDENTIFIER, PRESSURE.PRESSURE_S
FROM WELLBORE, PRESSURE
WHERE WELLBORE.REF_EXISTENCE_KIND = ’actual’ AND
WELLBORE.WELLBORE_S = PRESSURE.FACILITY_S
; hasFormationPressure(iri("Wellbore-"; IDENTIFIER);
iri("FP-"; PRESSURE_S)),
which, for brevity, represents a join of three tables as a single
‘table’ PRESSURE, can produce the ABox assertion
hasFormationPressure(Wellbore-16/1-29_S; FP-1249):
The ontology will then imply the ground atoms
hasMeasurement(Wellbore-16/1-29_S; FP-1249);
FormationPressure(FP-1249); Pressure(FP-1249);
which will hold in every model of our OBDA instance. Every
model will also have to satisfy atoms hasDepth(FP-1249;a )
and Depth(a), for some (possibly unknown)a.
The most important inference task in OBDA is query an-
swering. Given a query q(x) in the signature of O with
answer variables x, a tuple a of constants in D is called a
certain answer to q(x) over (P;D) ifIj = q(a), for every
modelI of (P;D). In our running example, FP-1249 is a cer-
tai

## 한국어 번역

온톨로지 기반 데이터 액세스: 설문조사
Guohui Xiao1, Diego Calvanese1, Roman Kontchakov2, Domenico Lembo3,
Antonella Poggi3, Riccardo Rosati3 및 Michael Zakharyaschev2
1 이탈리아 보젠-볼차노 자유대학교 KRDB 지식 및 데이터 연구센터
2 영국 런던 대학교 버크벡 컴퓨터 과학 및 정보 시스템학과
3 딥. 디 잉. Informatica Automata e Gestionale, Sapienza Università di Roma, 이탈리아
초록
온톨로지 기반 데이터의 프레임워크를 제시합니다.
액세스, 구성을 제공하기 위한 의미론적 패러다임
데이터 저장소에 대한 편리하고 사용자 친화적인 액세스
활발히 개발되고 연구되어온
지난 10년 동안 그랬어요. 관계형에 집중
데이터 소스의 주요 구성 요소에 대해 논의합니다.
온톨로지 기반 데이터 접근, 주요 이론적 결과,
기술, 응용 및 미래의 과제.
1 소개
온톨로지 기반 데이터 액세스(OBDA, 줄여서)는 의미가 있습니다.
2000년대 중반부터 개발된 tic 기술
[Poggi et al., 2008] 다양한 접근을 촉진하려는 목적으로
다양한 유형의 데이터 소스. 실제 시나리오에서 시작됩니다.
아래에 설명된 것과 같은 것입니다(http://purl.org/slegge 참조).
사례 1 노르웨이 다국적 기업인 Statoil(Equinor)
석유 및 가스 회사는 대규모 관계형 데이터베이스에 데이터를 저장합니다.
(DB) 약 1500개의 테이블(및 1700개의 뷰)을 갖춘 Slegge. 이전
유정 시추에 대한 결정을 내리는 데 있어 Sta-
관련 정보를 수집해야 합니다. 예를 들어, geolo-
요점의 정보 요구 사항에는 다음 질문이 포함될 수 있습니다.
(009) 내 관심 영역에 태그된 모든 압력 데이터를 반환합니다.
이해할 수 있는 주요 층위 정보를 갖춘
QC 속성(추가 필터링에 적합)
그러한 정보 요구를 표준으로 변환
데이터베이스 쿼리 언어 SQL은 일반적으로
Slegge가 어떤지 알면 안되는 지질학자들, 아니면-
조직화되었습니다. 실제로 유정의 기본 테이블에는 38개의 열이 있습니다.
다음을 달성하려면 두 개의 추가 필터가 포함된 4개의 테이블 조인이 필요합니다.
유정 및 층서학적 내부에 대한 형성 압력을 유지합니다.
형성하려면 테이블 5개를 더 조인해야 합니다. 기존 사용
SQL 템플릿과 답변 조작은 오류가 발생하기 쉽습니다.
IT 전문가에게 전화하는 데는 시간이 많이 걸립니다(며칠이 걸릴 수 있음).
또는 심지어 몇 주). OBDA는 다음과 같은 목적에 대해 다른 접근 방식을 제공합니다.
욕하고 대답하기(009). Statoil의 도메인 전문가
다음을 수행하는 지하 탐사 온톨로지(SE)를 설계했습니다.
Wellbore와 같은 사용자 정보 요구 사항에 대한 용어를 제공합니다.
hasFormationPressure 등 IT 전문가는 다음과 같은 매핑을 작성했습니다.
(SQL 쿼리를 통해) 온톨로지를 선언적으로 연결합니다.
Slegge DB에 대한 조건부입니다. 이제 지질학자의 임무는 다음과 같다.
SE의 어휘에서 (009)를 재구성하기 위해 - 아마도 다음을 사용하여
OptiqueVQS1과 같은 시각적 쿼리 인터페이스 -
W3C 표준 SPARQL2는 다음과 같습니다.
SELECT ?w ?깊이 ?strat_unit WHERE {
?w a :웰보어 . ?w :hasMeasurement ?p .
?p a :압력 . ?p :깊이 있음 ?깊이
선택사항 { ?깊이:inWellboreInterval ?strat_zone.
?strat_zone :hasUnit ?strat_unit } }.
이 쿼리는 변수 ?w에 대한 모든 할당을 검색합니다.
구성을 만족하는 SELECT 절의 ?깊이, ?strat_unit
WHERE 절의 버전입니다. 후자는 삼중 패턴으로 구성됩니다.
용어 '주어-술어-객체'(점으로 구분) 필요
데이터를 일치시키려면. 처음 4개의 삼중 패턴은 다음과 같이 말합니다. w는
Wellbore 클래스의 인스턴스이며 측정값 ?p를 가집니다.
압력의 인스턴스이며 해당 깊이가 기록됩니다.
hasDepth 속성으로. OPTIONAL의 두 가지 트리플 패턴
가능한 경우 계층에 대한 추가 정보를 반환합니다.
그래픽 단위 - 유정 간격의 Strat_unit
깊이 측정. 이는 선택 사항입니다.
가능?strat_unit에는 층서학적 내부가 있는 경우 값이 할당되지 않습니다.
깊이 측정에는 형성이 없습니다.
OBDA 시스템은 이를 자동으로 다시 작성합니다.
온톨로지를 사용한 SPARQL 쿼리 및 SQL 매핑
DB에 대해 쿼리하고, 최적화하고, Slege로 평가합니다. q
일반적으로 회사의 정보를 수집하는 경우에도
IT 전문가가 아닌 사용자에게는 DB가 어려운 작업입니다. 주요 내용 중 하나
그 이유는 DB가 일반적으로 애플리케이션을 제공하도록 설계되었기 때문입니다.
설명: 그 구조와 의미는 대부분의 경우 모호합니다.
사용자; 저장된 데이터는 중복되거나 혼합되어 있는 경우가 많습니다.
회사 프로세스를 지원하는 데만 필요한 정보
비즈니스 도메인과 관련하여 불완전합니다. 수집,
정보를 통합하고 조정하며 효율적으로 추출합니다.
이질적이고 자율적인 데이터 소스로부터의 데이터가 간주됩니다.
'대부분의 기업이 [. . . ] 캡처
데이터와 분석의 잠재적 가치는 극히 일부에 불과합니다.' .3
OBDA 패러다임은 다음을 제공함으로써 이 문제를 해결합니다.
1http://optique-project.eu/training-programme/module-vqs
2http://www.w3.org/TR/sparql11-query
3“분석의 시대: 데이터 중심 세계에서 경쟁” , McK-
insey 글로벌 연구소, 2016년 12월.
제27차 인공지능 국제합동회의(IJCAI-18) 간행물
5511

자율적인 데이터 소스로 구성된 데이터 계층에 대한 액세스
(예: DB) 개념 도메인의 중재를 통해
온톨로지 측면에서 주어진 관점과 선언문의 사용
데이터 레이어와 온톨로지 간의 매핑을 활성화합니다. OBDA
사용자는 데이터 소스의 세부 사항을 알 필요가 없으며 다음을 수행할 수 있습니다.
개념에 대한 질문으로 정보 요구 사항을 표현합니다.
Tual 도메인 모델. 지식 표현을 적용하여
및 자동화된 추론 기술을 사용하는 OBDA 시스템
사용자 쿼리를 재구성하기 위한 온톨로지 및 매핑
데이터베이스에서 직접 실행되는 표준 DB 쿼리
소스 관리 시스템(DBMS)입니다. 그래서 OBDA는
KR&R과 DB 기술을 모두 활용합니다.
이 패러다임을 구현하는 OBDA 시스템에는 다음이 포함됩니다.
tro [Calvanese et al., 2011 ], Morph [Priyatna et al., 2014 ],
Ontop [Calvanese et al., 2017], Stardog4 및 Ultrawrap [Se-
queda 및 Miranker, 2013]. 그들은 많은 곳에서 채택되었습니다.
산업 프로젝트 및 사용 사례(예: Statoil 및 Siemens 5)
이탈리아 경제재무부 [Antonioli et al.
al., 2014], 스마트 시티 프로젝트에서 [López et al., 2015 ],
전자 건강 기록[Rahimi et al., 2014] 및 Manu-
팩터링 [Petersen et al., 2017].
지난 10년 동안 OBDA의 이론과 실제
지식재산 분야에서 화제가 되고 있습니다.
문장(설명 논리), 의미론적 기술 및
최고의 CS 저널에 수많은 논문이 게재된 데이터베이스
최종(AIJ, JACM, JAIR, TODS 포함) 및 컨퍼런스,
과 같은 저명한 학문과 깊은 관계를 맺고 있습니다.
제약 조건 만족 및 회로 복잡성이 확립되었습니다.
이 간단한 설문 조사에서 우리는 OBDA의 프레임워크를 소개합니다.
주요 결과, 기술 및 과제에 대해 논의합니다. 우리는 먼저
섹션 2에서 고전적인 OBDA 프레임워크를 설명합니다. 그런 다음,
3장에서는 질의응답 과정을 살펴본다.
OBDA. 섹션 4에서는 매핑 관리와
분석. 5장에서는 고전의 확장에 대해 설명한다.
OBDA 프레임워크. 마지막으로 섹션 6에서는 다음 중 일부를 논의합니다.
가장 중요한 연구방향.
우리는 독자가 기본 사항을 잘 알고 있다고 가정합니다.
데이터베이스(표준 학부 DB 과정 수준).
2 OBDA 프레임워크
우리는 먼저 OBDA의 공식적인 프레임워크를 제시합니다.
확장형(인스턴스)과 의도형을 구별합니다.
sional(스키마) 수준. 전자는 DBD 소스에서 제공됩니다.
데이터 소스 스키마를 준수합니다(일반적으로
무결성 제약 조건 포함), 후자는 OBDA 사양에 따른 것입니다.
ifificationP = (O;M;S), 여기서 O는 온톨로지, S는 데이터
소스 스키마와 M은 S에서 O로의 매핑(서명
온톨로지와 스키마는 서로 분리되어 있습니다. O의 역할은
사용자에게 높은 수준의 개념적 뷰를 제공합니다.
쿼리에 대한 데이터 및 편리한 어휘; 그것은 또한 할 수 있다
배경 지식으로 불완전한 데이터를 풍부하게 합니다.
예제 2 지하 탐사 온톨로지(SE)
예제 1에는 다음과 같은 공리가 포함되어 있습니다.
설명 논리(DL) 구문에 제공됨 [Baader et al., 2017]:
4http://www.stardog.com
5http://optique-project.eu/results-downloads
형성압력v 압력;
형성압력u 정수압력v?;
hasFormationPressurev hasMeasurement;
9hasFormationPressure :>v 형성압력;
FormationPressurev9 hasDepth:깊이:
처음 세 개는 각각 단항 사이에 포함됩니다.
술어(DL의 개념 또는 시맨틱 웹의 클래스
용어) 및 이진 술어(역할 또는 속성); 그들의
1차(FO) 등가물은 다음과 같습니다.
8x(형성 압력(x)! 압력(x));
8x (형성 압력(x)^정수압(x)!? );
8xy (hasFormationPressure(x;y )! hasMeasurement(x;y )):
네 번째 공리는 hasFormationPres의 범위를 제한합니다.
물론입니다. 다섯 번째는 실존적 수량화와 관련이 있습니다.
8xy (hasFormationPressure(y;x)! FormationPressure(x));
8x (형성 압력(x)!9y(has깊이(x;y )^깊이(y))):
q
매핑M inP는 온톨로지가 어떻게 예측하는지 지정합니다.
소스 DB의 데이터로 채워집니다. 에서
SE 예에서 각 유정은 다음과 같이 식별됩니다.
WELLBORE 테이블의 IDENTIFIER 열이 제공됩니다.
다음 형식의 IRI(국제화된 자원 식별자)
http://slegger.gitlab.io/data#Wellbore-n을 나타냅니다.
온톨로지의 유정; 후속편에서는 접두사를 생략합니다.
그러한 IRI를 Wellbore-n으로 단축합니다. 그런 다음 매핑 콘-
SE를 Slegge 데이터베이스에 연결하면 어설션이 포함됩니다.
WELLBORE에서 식별자를 선택하세요
WHERE REF_EXISTENCE_KIND = '실제'
; Wellbore(iri("Wellbore-"; IDENTIFIER))
SQL에 대한 답변으로 Wellbore 클래스 채우기
;의 왼쪽에 있는 쿼리입니다. 일반적으로 매핑 어설션은 다음과 같습니다.
'(x) 형식;  (x), 여기서 '(x)와 (x)는 FO-입니다.
S와 O의 서명에 각각 수식을 입력합니다. 우리의
예를 들어 SQL 쿼리를 사용하여 편리하게 표현합니다.
공식'(x)(WELLBORE에는 38개의 열이 있음을 기억하세요). 특정-
(가변 소수의) 함수 iri는 다음을 위해 (x)에서 사용됩니다.
온톨로지 객체에 대한 구조체 IRI: iri의 매개변수는 다음과 같습니다.
문자열 및 DB 열(x의 변수) 및
iri 항은 매개변수 값을 연결한 것입니다.
OBDA 사양P와 소스의 쌍(P;D)
DBD는OBDA 인스턴스라고 합니다. 의미를 정의하려면 다음과 같이 하십시오.
M(D)는 다음과 같은 O의 기호에 있는 최소 원자 집합입니다.
모든 '(x)에 대해 (a)를 만족합니다.  (x) inM 및 모든 튜플 a
'(a)가 inD를 유지하는 상수 inD입니다. 예를 들어,
WELLBORE 테이블에 다음이 포함된 경우 SE 설정
식별자 REF_EXISTENCE_KIND. . .
16/1-29_S 실제 . . .
3/zero.alt1/8-5 실제 ​​. . .
33/1/zero.alt1-12 예정 . . .
그러면 매핑은 다음 두 가지 접지를 생성합니다.
원자(ABox 주장 또는 RDF 트리플에 해당):
Wellbore(Wellbore-16/1-29_S); 유정(Wellbore-3/zero.alt1/8-5):
우리는 O의 서명에 대해 FO 구조I를 모델로 부릅니다.
(P;D) 및 writeIj = (P;D), if Ij =O 및 Ij =M(D).
따라서 위의 두 접지 원자는 FO 구조를 형성합니다.
제27차 인공지능 국제합동회의(IJCAI-18) 간행물
5512

은 우리의 예제 OBDA 인스턴스의 모델입니다. 추가
매핑 어설션
WELLBORE.IDENTIFIER, PRESSURE.PRESSURE_S를 선택하세요.
WELLBORE의 압력
WHERE WELLBORE.REF_EXISTENCE_KIND = '실제' AND
WELLBORE.WELLBORE_S = 압력.FACILITY_S
; hasFormationPressure(iri("Wellbore-"; IDENTIFIER);
iri("FP-"; 압력_S)),
이는 간략하게 3개의 테이블을 단일 테이블로 조인하는 것을 나타냅니다.
'테이블' 압력, ABox 어설션을 생성할 수 있음
hasFormationPressure(Wellbore-16/1-29_S; FP-1249):
그러면 온톨로지는 기본 원자를 암시합니다.
hasMeasurement(Wellbore-16/1-29_S; FP-1249);
형성압력(FP-1249); 압력(FP-1249);
이는 우리 OBDA 인스턴스의 모든 모델에 적용됩니다. 매
모델은 또한 원자 hasDepth(FP-1249;a )를 충족해야 합니다.
및 깊이(a), 일부(아마도 알려지지 않음)a.
OBDA에서 가장 중요한 추론 작업은 쿼리입니다.
스윙. O의 서명에 있는 쿼리 q(x)가 주어지면
변수 x에 답하고, D의 상수로 구성된 튜플 a를 a라고 합니다.
(P;D)에 대한 q(x)에 대한 특정 답 ifIj = q(a), 모든 경우
(P;D)의 모델I. 실행 중인 예에서 FP-1249는 인증서입니다.
타이
