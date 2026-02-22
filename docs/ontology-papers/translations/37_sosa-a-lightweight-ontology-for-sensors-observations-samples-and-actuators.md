# [37] SOSA: 센서·관측·샘플·액추에이터 경량 온톨로지

- 영문 제목: SOSA: A lightweight ontology for sensors, observations, samples, and actuators
- 연도: 2018
- 원문 링크: https://doi.org/10.1016/j.websem.2018.06.003
- DOI: 10.1016/j.websem.2018.06.003
- 원문 저장 상태: pdf_saved
- 원문 파일: /Volumes/SAMSUNG/apps/projects/vive-md/docs/ontology-papers/originals/37_sosa-a-lightweight-ontology-for-sensors-observations-samples-and-actuators.pdf
- 번역 상태: partial_translated

## 원문(추출 텍스트)

SOSA: A Lightweight Ontology for Sensors, Observations, Samples, and Actuators
Krzysztof Janowicza,, Armin Hallerb, Simon J D Coxc, Danh Le Phuocd, Maxime Lefranc ¸oise
aDepartment of Geography, University of California, Santa Barbara, USA
bResearch School of Computer Science, Australian National University, Canberra, Australia
cLand and Water , CSIRO, Melbourne, Australia
dDepartment of Telecommunication Systems, Technische Universit¨ at, Berlin, Germany
eConnected-Intelligence team, Ecole des Mines de Saint-Etienne, France
Abstract
The Sensor, Observation, Sample, and Actuator (SOSA) ontology provides a formal but lightweight general-purpose speciﬁca-
tion for modeling the interaction between the entities involved in the acts of observation, actuation, and sampling. SOSA is
the result of rethinking the W3C-XG Semantic Sensor Network (SSN) ontology based on changes in scope and target audience,
technical developments, and lessons learned over the past years. SOSA also acts as a replacement of SSN’s Stimulus Sensor
Observation (SSO) core. It has been developed by the ﬁrst joint working group of the Open Geospatial Consortium (OGC) and
the World Wide Web Consortium (W3C) on Spatial Data on the Web . In this work, we motivate the need for SOSA, provide
an overview of the main classes and properties, and brieﬂy discuss its integration with the new release of the SSN ontology as
well as various other alignments to speciﬁcations such as OGC’s Observations and Measurements (O&M), Dolce-Ultralite (DUL),
and other prominent ontologies. We will also touch upon common modeling problems and application areas related to publish-
ing and searching observation, sampling, and actuation data on the Web. The SOSA ontology and standard can be accessed at
https://www.w3.org/TR/vocab-ssn/.
Keywords: Ontology, Sensor, Observation, Actuator, Linked Data, Web of Things, Internet of Things, Schema.org
1. Introduction and Motivation
In their broadest deﬁnition sensors detect and react to
changes in the environment that directly or indirectly reveal the
value of a property. The process of determining this, not nec-
essarily numeric, value is called an observation. Observation
procedures provide a sequence of instructions to ensure that the
observations are reproducible and representative, whereby an
individual assessment characterizes a feature (i.e., entity) of in-
terest. Typically, observations are not carried out on the en-
tire feature but on samples of it, or on an immediately sensed
spatiotemporal region. The process of sampling may itself be
speciﬁed by a procedure that determines how to obtain samples.
Some observation procedures can contain sampling procedures
as their parts. Actions triggered by observations are called ac-
tuations and the entities that perform them are actuators. Fi-
nally, actuators, sensors, and samplers are typically mounted
on a platform. These platforms serve a wide range of needs,
including carrying systems along a deﬁned trajectory, protect-
ing them from external inﬂuences that may distort the results,
or spatially positioning multiple systems following a particular
layout.
In the context of smart homes, for instance, a temperature
sensor can be mounted to a wall and take repeated observations
Email addresses: janowicz@ucsb.edu (Krzysztof Janowicz),
armin.haller@anu.edu.au (Armin Haller), simon.cox@csiro.au
(Simon J D Cox), danh.lephuoc@tu-berlin.de (Danh Le Phuoc),
maxime.Lefrancois@emse.fr (Maxime Lefranc ¸ois)
at some time interval. Each of these observations returns the
temperature of a sample, namely the surrounding body of air.
In cases where the sensor is placed correctly, the temperature is
said to be characteristic (representative) for the entire feature of
interest, e.g., a bedroom. For example, a decrease in room tem-
perature may trigger an actuator to close the windows. While
each individual observation results in a new value and is taken
from a new sample, all observations are based on the same pro-
cedure, observe the same property, and reveal the same char-
acteristic of the same feature of interest. Ignoring some aspect
of the observation procedure - e.g., by placing the sensor next
to the window so that the sampled body of air is no longer a
suitable proxy for the entire room - may cause the observation
results to become unrepresentative of the room’s temperature,
and may lead to the actuator closing the window unexpectedly.
Note that if one would place all sensors in such way, the result-
ing observations may not be representative for the room though
they still may be reproducible. Finally, if some sensors would
be placed near windows while others would not, it would no
longer be possible to establish a relationship between the be-
havior of individual actuators. Finally, procedures are speciﬁc
for certain types of observations. Hence, one can follow a spe-
ciﬁc procedure and thereby arrive at reproducible results that is
not representative or suitable for the task at hand.
With a rapid increase in data from sensors being published
on the Web, there is an increasing interest in the re-use and
combination of that data. However, raw observation results do
not provide the context required to interpret them properly and
Preprint submitted to Elsevier December 27, 2018
arXiv:1805.09979v2  [cs.AI]  25 Dec 2018

to make sense of these data. Searching, reusing, integrating,
and interpreting data requires more information about the stud-
ied feature of interest, such as a room, the observed property,
such as temperature, the utilized sampling strategy, such as the
speciﬁc locations and times at which the temperature was mea-
sured, and a variety of other information. With the rise of smart
cities and smart homes as well as the Web of Things more
generally, actuators and the data that is produced by their in-
built sensors also become ﬁrst-class citizens of the Web. Given
their close relation to sensors, observations, procedures, and
features of interest, outlined above it is desirable to provide a
common framework and vocabulary that also includes actua-
tors and actuation. Finally, with today’s diversity of data and
data providers, notions that restrict the view of sensors to being
technical devices need to be broadened. One example would
be social sensing techniques such as semantic signatures [14]
to study humans and the data traces they actively and passively
emit from within a sensor-observation framework. Simulations
and forecasts are other examples showcasing why ‘sensors’ that
produce estimates of properties in the world are not necessarily
physical entities.
The Sensor Web Enablement standards such as the Obser-
vations and Measurements (O&M) [4] model and the Sen-
sor Model Language (SensorML) [1] speciﬁed by the Open
Geospatial Consortium (OGC) provide means to annotate sen-
sors and their observations. However, these standards are not
integrated and aligned with Semantic Web technologies, Linked
Data, and other parts of the World Wide Web Consortium’s
(W3C) technology stack that aims at creating and maintain-
ing a global and densely interconnected graph of data. The
W3C Semantic Sensor Network Incubator Group (SSN-XG)
tried to address this issue by ﬁrst surveying the landscape of
semantically-enabled sensor speciﬁcations [3] and then devel-
oping the Semantic Sensor Network (SSN) ontology [2] as
a human and machine readable speciﬁcation that covers net-
works of sensors and their deployment on top of sensors and
observations. To provide an axiomatization beyond mere sur-
face semantics, SSN made use of the foundational Dolce Ul-
traLight (DUL) ontology, e.g., to state that platforms are phys-
ical objects. At the same time, SSN also provided the Sensor-
Stimulus-Observation (SSO) [16] ontology design pattern [6]
as a simple core vocabulary targeted towards lightweight appli-
cations and reuse-by-extension.
The broad success of the initial SSN led to a follow-up stan-
dardization process by the ﬁrst joint working group of the OGC
and the W3C. One of the tasks of this Spatial Data on the Web
working group was to rework the SSN ontology based on the
lessons learned over the past years and more speciﬁcally to ad-
dress changes in scope and audience, shortcomings of the ini-
tial SSN, as well as technical developments and trends in rele-
vant communities. The resulting ontology, published as a W3C
Recommendation and OGC Standard [10], is not only an up-
date but has been re-envisioned completely from the beginning.
Most notably, and as depicted in Fig. 1 the revised ontology
is based on a novel modular design which introduces a hori-
zontal and vertical segmentation. Vertical modules add addi-
tional depth to the axiomatization by directly importing lower
modules and deﬁning new axioms, while horizontal modules
broaden the ontology’s scope, e.g., by introducing classes and
relations to specify system capabilities or sample relationships,
but do not otherwise enrich the semantics of existing terms. The
modularization addresses an often voiced concern about the ini-
tial SSN release, that the DUL alignment introduced too strong
ontological commitments, and the full ontology was too heavy-
weight for smart devices in the context of the Web of Things,
and was running against the trend towards lightweight vocabu-
laries preferred by the Linked Data and Schema.org communi-
ties. The proposed modularization allowed us to keep the DUL
alignment for those who want to use it, and introduce additional
alignments to Prov-O [20], O&M [4], and OBOE [23], while
keeping the overall target audience broad, ranging from web
developers and scientists that want to publish their data on the
Web, to Web of Things industry players.
Figure 1: SOSA and its vertical and horizontal modules with the arcs indicating
the direction of the import statement. Horizontal modularization is shown by
arcuate modules at the same radius while vertical modularization is shown by
modules at a larger radius.
The resulting collection of modules, including SSN, all build
upon a common core: the Sensor, Observation, Sample, and
Actuator ontology (SOSA). SOSA does not merely replace the
former SSO ontology design pattern but provides a ﬂexible yet
coherent framework for representing the entities, relations, and
activities involved in sensing, sampling, and actuation. It is
intended to be used as a lightweight, easy to use, and highly
extendable vocabulary that appeals to a broad audience beyond
the Semantic Web community but can be combined with other
ontologies, such as SSN to provide a more rigorous axiomati-
zation where needed. At the same time, SOSA acts as minimal
interoperability fall-back level, i.e., it deﬁnes those common
classes and properties for which data can be safely exchanged
across all uses of SSN, its modules, and SOSA.
2

In the following, we will focus on providing an overview of
the main classes and properties of SOSA. We will also brieﬂy
discuss their integration with the new SSN ontology. We will
motivate some of the core design decisions and provide mod-
eling examples that will arise in practice. For the sake of
readability, we will focus on an examples-driven description
of these classes. The formal and normative SOSA ontology
and standard can be accessed at https://www.w3.org/TR/
vocab-ssn/. Finally, we will discuss selected modeling prob-
lems and how to approach them and will give examples for the
usage of SOSA classes and relationships in diﬀerent application
areas.
2. SOSA in a Nutshell
Here, we will highlight the most important classes and re-
lationships that make up the SOSA ontology. In contrast to
the original SSN, SOSA takes an event-centric perspective and
revolves around observations, sampling, actuations, and proce-
dures. The last is a set of instructions specifying how to carry
out one of the three aforementioned acts. This event-centric
modelling is aligned with community expectations, in particu-
lar the Schema.org community that only cares abo

## 한국어 번역

SOSA: 센서, 관찰, 샘플 및 액추에이터를 위한 경량 온톨로지
Krzysztof Janowicza, Armin Hallerb, Simon J D Coxc, Danh Le Phuocd, Maxime Lefranc ¸oise
미국 캘리포니아대학교 산타바바라 지리학과
b호주 캔버라 호주국립대학교 컴퓨터과학 연구대학원
cLand and Water , CSIRO, 멜버른, 호주
독일 베를린 Technische Universit¨ 통신 시스템학과
eConnected-Intelligence 팀, 프랑스 Ecole des Mines de Saint-Etienne
초록
SOSA(센서, 관찰, 샘플 및 액추에이터) 온톨로지는 형식적이지만 가벼운 범용 사양을 제공합니다.
관찰, 작동 및 샘플링 활동에 관련된 엔터티 간의 상호 작용을 모델링하기 위한 기능입니다. SOSA는
범위와 대상 고객의 변화를 기반으로 W3C-XG SSN(의미 센서 네트워크) 온톨로지를 다시 생각한 결과,
기술 개발 및 지난 몇 년 동안 배운 교훈. SOSA는 SSN의 자극 센서를 대체하는 역할도 합니다.
관찰(SSO) 코어. OGC(Open Geospatial Consortium)의 첫 번째 공동 작업 그룹에 의해 개발되었으며,
웹상의 공간 데이터에 관한 월드 와이드 웹 컨소시엄(W3C). 이 작업에서 우리는 SOSA의 필요성에 동기를 부여하고
주요 클래스와 속성에 대한 개요를 설명하고 SSN 온톨로지의 새 릴리스와의 통합에 대해 간략하게 설명합니다.
OGC의 O&M(Observations and Measurements), DUL(Dolce-Ultralite)과 같은 사양에 대한 다양한 기타 정렬,
및 기타 주요 온톨로지. 또한 출판과 관련된 일반적인 모델링 문제와 응용 분야에 대해서도 다룰 것입니다.
웹에서 관찰, 샘플링, 작동 데이터를 수집하고 검색합니다. SOSA 온톨로지 및 표준은 다음에서 액세스할 수 있습니다.
https://www.w3.org/TR/vocab-ssn/.
키워드: 온톨로지, 센서, 관찰, 액추에이터, 연결된 데이터, 사물 웹, 사물 인터넷, Schema.org
1. 서론 및 동기
가장 넓은 정의에서 센서는 다음을 감지하고 반응합니다.
직간접적으로 드러나는 환경의 변화
재산의 가치. 이를 결정하는 과정은 필요하지 않습니다.
본질적으로 숫자인 값을 관찰이라고 합니다. 관찰
절차는 다음을 보장하기 위한 일련의 지침을 제공합니다.
관찰은 재현 가능하고 대표적입니다.
개별 평가는 다음의 특징(즉, 실체)을 특징짓습니다.
관심. 일반적으로 관찰은 현장에서 수행되지 않습니다.
타이어 특징은 샘플에 있거나 즉시 감지된 것입니다.
시공간 영역. 샘플링 과정 자체가
샘플을 얻는 방법을 결정하는 절차에 따라 지정됩니다.
일부 관찰 절차에는 샘플링 절차가 포함될 수 있습니다.
그들의 부분으로. 관찰에 의해 촉발된 행동을 행동이라고 부른다.
작동과 이를 수행하는 개체는 액추에이터입니다. Fi-
마지막으로 액추에이터, 센서 및 샘플러가 일반적으로 장착됩니다.
플랫폼에서. 이러한 플랫폼은 다양한 요구 사항을 충족합니다.
정의된 궤적을 따라 운반 시스템을 포함하여 다음을 보호합니다.
결과를 왜곡할 수 있는 외부 영향으로 인해
또는 특정 시스템을 따라 여러 시스템을 공간적으로 배치
레이아웃.
예를 들어 스마트 홈의 맥락에서 온도
센서를 벽에 장착하여 반복적으로 관찰할 수 있습니다.
이메일 주소: janowicz@ucsb.edu (Krzysztof Janowicz),
armin.haller@anu.edu.au (아르민 할러), simon.cox@csiro.au
(Simon J D Cox), danh.lephuoc@tu-berlin.de (Danh Le Phuoc),
maxime.Lefrancois@emse.fr (Maxime Lefranc ¸ois)
어떤 시간 간격으로. 이러한 각 관측값은 다음을 반환합니다.
샘플의 온도, 즉 주변 공기체.
센서가 올바르게 배치된 경우 온도는 다음과 같습니다.
의 전체 특징을 특징적(대표적)이라고 합니다.
관심, 예를 들어 침실. 예를 들어 실내 온도가 낮아지면
상황에 따라 액추에이터가 작동하여 창문을 닫을 수도 있습니다. 동안
각각의 개별 관찰 결과는 새로운 값을 가져오고
새로운 표본의 모든 관찰은 동일한 프로를 기반으로 합니다.
동일한 속성을 관찰하고 동일한 특성을 드러냅니다.
동일한 관심 특징을 지닌 배우. 일부 측면을 무시함
관찰 절차 - 예를 들어 센서를 다음 위치에 배치
샘플링된 공기가 더 이상
방 전체에 적합한 프록시 - 관찰이 발생할 수 있음
결과적으로 실내 온도를 대표하지 않게 됩니다.
액추에이터가 예기치 않게 창을 닫을 수도 있습니다.
모든 센서를 이러한 방식으로 배치하면 결과는 다음과 같습니다.
관찰한 내용이 방을 대표하지 못할 수도 있지만
여전히 재현 가능할 수 있습니다. 마지막으로, 일부 센서가
다른 사람들은 그렇지 않은 반면 창문 근처에 배치하면 안됩니다.
더 이상 두 사람 사이의 관계를 확립하는 것이 가능해집니다.
개별 액추에이터의 특성. 마지막으로 절차는 구체적이다.
특정 유형의 관찰에 대해. 따라서 특정 특정을 따를 수 있습니다.
cific 절차를 거쳐 재현 가능한 결과에 도달합니다.
대표성이 없거나 당면한 작업에 적합하지 않습니다.
게시되는 센서의 데이터가 급격히 증가함에 따라
웹 상에서 재사용에 대한 관심이 증가하고 있으며,
그 데이터의 조합. 그러나 원시 관찰 결과는
적절하게 해석하는 데 필요한 맥락을 제공하지 않고
2018년 12월 27일 Elsevier에 사전 인쇄 제출됨
arXiv:1805.09979v2 [cs.AI] 2018년 12월 25일

이러한 데이터를 이해하기 위해. 검색, 재사용, 통합,
데이터를 해석하려면 연구에 대한 더 많은 정보가 필요합니다.
방, 관찰된 재산과 같은 관심 있는 특징,
온도, 활용된 샘플링 전략,
온도가 측정된 특정 위치와 시간
확실하고 다양한 정보를 제공합니다. 스마트의 등장으로
도시, 스마트 홈, 사물 웹(Web of Things)
일반적으로 액츄에이터와 그 내부에서 생성되는 데이터는 다음과 같습니다.
내장된 센서는 또한 웹의 일류 시민이 됩니다. 주어진
센서, 관찰, 절차 및
위에서 설명한 관심 기능을 제공하는 것이 바람직합니다.
실제 내용도 포함하는 공통 프레임워크 및 어휘
토르와 작동. 마지막으로 오늘날의 다양한 데이터와
데이터 제공자, 센서의 시야를 제한하는 개념
기술적인 장치를 확대해야 합니다. 한 가지 예는
의미적 서명과 같은 사회적 감지 기술이 되어야 합니다. [14]
인간과 그들이 능동적이고 수동적으로 추적하는 데이터를 연구합니다.
센서 관찰 프레임워크 내에서 방출됩니다. 시뮬레이션
예측은 왜 '센서'가
세계의 재산에 대한 추정치를 산출하는 것이 반드시 필요한 것은 아닙니다.
물리적 실체.
Observation과 같은 센서 웹 활성화 표준은
Vations and Measurements(O&M) [4] 모델과 Sen-
Open에서 지정하는 모델 언어(SensorML) [1]
지리공간 컨소시엄(OGC)은
Sors와 그들의 관찰. 그러나 이러한 표준은 그렇지 않습니다.
Semantic Web 기술과 통합 및 정렬, Linked
World Wide Web Consortium의 데이터 및 기타 부분
(W3C) 기술 스택은 다음을 생성하고 유지하는 것을 목표로 합니다.
전체적이고 촘촘하게 상호 연결된 데이터 그래프를 생성합니다. 는
W3C 시맨틱 센서 네트워크 인큐베이터 그룹(SSN-XG)
먼저 주변 환경을 조사하여 이 문제를 해결하려고 했습니다.
의미론적으로 활성화된 센서 사양[3]을 개발한 후
의미 센서 네트워크(SSN) 온톨로지 [2]를 다음과 같이 작동합니다.
네트워크를 포괄하는 인간과 기계가 읽을 수 있는 사양
센서 작업 및 센서 위에 배치
관찰. 단순한 추정을 넘어 공리화를 제공하기 위해
얼굴 의미론, SSN은 기본 Dolce Ul-
traLight(DUL) 온톨로지, 예를 들어 플랫폼이 물리적이라고 명시합니다.
ical 개체. 동시에 SSN은 센서-
자극 관찰(SSO) [16] 온톨로지 디자인 패턴 [6]
경량 애플리케이션을 대상으로 하는 간단한 핵심 어휘로
양이온 및 확장에 의한 재사용.
초기 SSN의 광범위한 성공은 후속 조치로 이어졌습니다.
OGC의 첫 번째 공동 실무 그룹에 의한 다분화 프로세스
그리고 W3C. 웹상의 공간정보의 업무 중 하나
워킹 그룹은 다음을 기반으로 SSN 온톨로지를 재작업하는 것이 었습니다.
지난 몇 년간 배운 교훈, 특히 광고에 대한 교훈
범위와 청중의 복장 변화, 초기의 단점
SSN 관련 기술 발전 및 동향
반트 커뮤니티. W3C로 게시된 결과 온톨로지
권장사항 및 OGC 표준[10]은
날짜는 처음부터 완전히 다시 구상되었습니다.
가장 주목할 만한 점은 그림 1에 묘사된 바와 같이 수정된 온톨로지가
수평을 도입하는 새로운 모듈식 디자인을 기반으로 합니다.
구역 및 수직 분할. 수직 모듈 추가
하위 항목을 직접 가져와서 공리화에 대한 깊이를 더했습니다.
모듈을 만들고 새로운 공리를 정의하는 동시에 수평 모듈을
예를 들어 클래스를 도입하여 온톨로지의 범위를 확장합니다.
시스템 기능 또는 샘플 관계를 지정하는 관계,
그러나 기존 용어의 의미를 풍부하게 하지는 않습니다. 는
모듈화는 초기 단계에 대해 자주 제기되는 우려를 해결합니다.
DUL 정렬이 너무 강력하게 도입된 최초 SSN 릴리스
존재론적 약속이 있었고, 전체 온톨로지는 너무 무거웠습니다.
사물 웹의 맥락에서 스마트 장치의 무게,
가벼운 어휘를 지향하는 추세에 맞서고 있었습니다.
Linked Data 및 Schema.org 커뮤니티에서 선호하는 항목
관계. 제안된 모듈화를 통해 우리는 DUL을 유지할 수 있었습니다.
사용하고 싶은 분들을 위해 정렬하고, 추가로 소개해드립니다.
Prov-O [20], O&M [4] 및 OBOE [23]에 대한 정렬입니다.
웹에서부터 전체 대상 고객을 광범위하게 유지
자신의 데이터를 웹사이트에 게시하려는 개발자와 과학자
Web, Web of Things 업계 플레이어에게.
그림 1: SOSA와 수직 및 수평 모듈(원호 포함)
수입 명세서의 방향. 수평적 모듈화는 다음과 같이 표시됩니다.
동일한 반경의 아치형 모듈과 수직 모듈화는 다음과 같이 표시됩니다.
더 큰 반경의 모듈.
SSN을 포함한 결과 모듈 모음은 모두 빌드됩니다.
공통 핵심: 센서, 관찰, 샘플 및
SOSA(액추에이터 온톨로지). SOSA는 단순히
이전 SSO 온톨로지 디자인 패턴이지만 유연성을 제공합니다.
엔터티, 관계 및 개체를 표현하기 위한 일관된 프레임워크
감지, 샘플링, 작동과 관련된 활동입니다. 그것은
가볍고 사용하기 쉬우며 고도로 사용하기 위한 것입니다.
광범위한 청중에게 호소력을 발휘하는 확장 가능한 어휘
시맨틱 웹 커뮤니티이지만 다른 커뮤니티와 결합될 수도 있습니다.
SSN과 같은 온톨로지는 보다 엄격한 공리를 제공합니다.
필요한 곳에 배치. 동시에 SOSA는 최소한의 역할을 합니다.
상호 운용성 폴백 수준, 즉 공통적인 사항을 정의합니다.
데이터를 안전하게 교환할 수 있는 클래스 및 속성
SSN, 해당 모듈 및 SOSA의 모든 사용에 걸쳐.
2

다음에서는 개요를 제공하는 데 중점을 둘 것입니다.
SOSA의 주요 클래스와 속성. 우리도 간략하게
새로운 SSN 온톨로지와의 통합에 대해 논의합니다. 우리는
일부 핵심 설계 결정에 동기를 부여하고 모드를 제공합니다.
실제로 발생할 수 있는 예입니다. 위해
가독성을 높이기 위해 예시 중심의 설명에 중점을 둘 것입니다.
이 수업 중. 공식적이고 규범적인 SOSA 온톨로지
표준은 https://www.w3.org/TR/에서 액세스할 수 있습니다.
어휘-ssn/. 마지막으로 선택된 모델링 문제에 대해 논의하겠습니다.
렘과 이에 접근하는 방법에 대한 예를 제시할 것입니다.
다양한 애플리케이션에서 SOSA 클래스 및 관계 사용
지역.
2. 간단히 말해서 SOSA
여기서는 가장 중요한 수업을 강조하고 다시 설명하겠습니다.
SOSA 온톨로지를 구성하는 관계. 대조적으로
원래 SSN인 SOSA는 이벤트 중심의 관점을 취하고
관찰, 샘플링, 작동 및 절차를 중심으로 진행됩니다.
강압. 마지막은 휴대 방법을 지정하는 일련의 지침입니다.
앞서 언급한 세 가지 행위 중 하나입니다. 이 이벤트 중심
모델링은 특히 커뮤니티의 기대에 부합합니다.
abo에만 관심을 갖는 Schema.org 커뮤니티
