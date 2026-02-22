# [46] LLMs4OL 2024 데이터셋

- 영문 제목: LLMs4OL 2024 Datasets: Toward Ontology Learning with Large Language Models
- 연도: 2024
- 원문 링크: https://doi.org/10.52825/ocp.v4i.2480
- DOI: 10.52825/ocp.v4i.2480
- 원문 저장 상태: pdf_saved
- 원문 파일: /Volumes/SAMSUNG/apps/projects/vive-md/docs/ontology-papers/originals/46_llms4ol-2024-datasets-toward-ontology-learning-with-large-language-models.pdf
- 번역 상태: partial_translated

## 원문(추출 텍스트)

L L M s 4 O L  2 0 2 4:  T h e  1 st  L ar g e  L a n g u a g e  M o d el s  f or  O nt ol o g y  L e ar ni n g  C h all e n g e  at  t h e  2 3r d  I S W C 
L L M s 4 O L  2 0 2 4  T a s k  O v er vi e w 
htt p s:// d oi. or g/ 1 0. 5 2 8 2 5/ o c p. v 4i. 2 4 8 0 
©  A ut h or s.  T hi s  w or k  i s  li c e n s e d  u n d er  a  Cr e ati v e  C o m m o n s  Attri b uti o n  4. 0  I nt er n ati o n al  Li c e n s e 
P u bli s h e d: 0 2 O ct. 2 0 2 4 
L L M s 4 O L  2 0 2 4  D at a s et s:  T o w ar d  O nt ol o g y  L e ar ni n g 
wit h  L ar g e  L a n g u a g e  M o d el s 
H a m e d  B a b a ei  Gi gl o u  , J e n nif er  D’ S o u z a  , S a m e er  S a dr u d di n  , a n d  S ¨or e n  A u er 
TI B  L ei b ni z  I nf or m ati o n  C e ntr e  f or  S ci e n c e  a n d  T e c h n ol o g y,  H a n n o v er,  G er m a n y 
{ h a m e d. b a b a ei,  j e n nif er. d s o u z a,  s a m e er. s a dr u d di n,  a u er } @ti b. e u 
* C orr e s p o n d e n c e:  H a m e d  B a b a ei  Gi gl o u,  h a m e d. b a b a ei @ti b. e u 
A b str a ct:  O nt ol o g y  l e ar ni n g  ( O L)  fr o m  u n str u ct ur e d  d at a  h a s  e v ol v e d  si g ni ﬁ c a ntl y,  wit h  
r e c e nt  a d v a n c e m e nt s  i nt e gr ati n g  l ar g e  l a n g u a g e  m o d el s  ( L L M s)  t o  e n h a n c e  v ari o u s  
a s p e ct s  of  t h e  pr o c e s s.  T h e  p a p er  i ntr o d u c e s  t h e  L L M s 4 O L  2 0 2 4  d at a s et s,  d e v el o p e d  
t o  b e n c h m ar k  a n d  a d v a n c e  r e s e ar c h  i n  O L  u si n g  L L M s.  T h e  L L M s 4 O L  2 0 2 4  d at a s et  
a s  a  k e y  c o m p o n e nt  of  t h e  L L M s 4 O L  C h all e n g e,  t ar g et s  t hr e e  pri m ar y  O L  t a s k s:  T er m  
T y pi n g,  T a x o n o m y  Di s c o v er y, a n d  N o n- Ta x o n o mi c  R el ati o n  E xtr a cti o n.  It  e n c o m p a s s e s  
s e v e n  d o m ai n s,  i. e.  l e x o s e m a nti c s  a n d  bi ol o gi c al  f u n cti o n s,  off eri n g  a  c o m pr e h e n si v e  
r e s o ur c e  f or  e v al u ati n g  L L M- b a s e d  O L  a p pr o a c h e s  E a c h  t a s k  wit hi n  t h e  d at a s et  i s  
c ar ef ull y  cr aft e d  t o  f a cilit at e  b ot h  F e w- S h ot  ( F S)  a n d  Z er o- S h ot  ( Z S)  e v al u ati o n  s c e n ar- 
i o s,  all o wi n g  f or  r o b u st  a s s e s s m e nt  of  m o d el  p erf or m a n c e  a cr o s s  diff er e nt  k n o wl e d g e  
d o m ai n s  t o  a d dr e s s  a  criti c al  g a p  i n  t h e  ﬁ el d  b y  off eri n g  st a n d ar di z e d  b e n c h m ar k s  f or  
f air  c o m p ar i s o n  f or  e v al u ati n g  L L M  a p pli c ati o n s  i n  O L. 
K e y w or d s:  O nt ol o g y  L e ar ni n g,  L ar g e  L a n g u a g e  M o d el s,  D at a s et,  L L M s 4 O L  C h al- 
l e n g e 
1  I ntr o d u cti o n 
O nt ol o gi e s  h a v e  g ai n e d  a  l ot  of  p o p ul arit y  a n d  r e c o g niti o n  i n  t h e  s e m a nti c  w e b  b e c a u s e  
of  t h eir  ﬁ n e  s o ur c e  o f  s e m a nti c s  a n d  i nt er o p er a bilit y. T h e  i n cr e a s e  i n  u n str u ct ur e d  
d at a  o n  t h e  w e b  h a s  m a d e  t h e  a ut o m at e d  a c q ui siti o n  of  o nt ol o g y  fr o m  u n str u ct ur e d  
t e xt  a  m o st  pr o mi n e nt  r e s e ar c h  ar e a.  R e c e ntl y,  i n st e a d  of  h a n d cr afti n g  o nt ol o gi e s,  
t h e  r e s e ar c h  tr e n d  i s  n o w  s hifti n g  t o w ar d  a ut o m ati c  o nt ol o g y  l e ar ni n g  ( O L)  [ 1] . O L  
i n v ol v e s  a ut o m ati c all y  i d e ntif yi n g  t er m s,  t y p e s,  r el ati o n s,  a n d  p ot e nti al  a xi o m s  fr o m  
t e xt u al  i nf or m ati o n  t o  c o n str u ct  a n  o nt ol o g y  [ 2]. 
L o o ki n g  b a c k  t o  t h e  hi st or y  of  O L  r e s e ar c h,  u ntil  e arl y  2 0 0 2  [ 3] , m o st  O L  a p pr o a c h e s  
r eli e d  o n  s e e d  w or d s  or  e xi sti n g  b a s e  o nt ol o gi e s  r at h er  t h a n  b uil di n g  n e w  o n e s  fr o m  
s cr at c h.  L at er  i n  2 0 0 3  [ 4]  t h e  n at ur al  l a n g u a g e  pr o c e s si n g  ( N L P)  t e c h ni q u e  s h o w e d  
pr o mi s e  f or  t h e  e xtr a cti o n  of  n e w  c o n c e pt s.  H o w e v er,  r el ati o n  e xtr a cti o n  f or  O L  r e- 
m ai n e d  still  c h all e n gi n g.  Al s o,  t h e  pri or  d o m ai n  k n o wl e d g e  of  t h e  b a s e  o nt ol o gi e s  still  
w a s  i n  t h e  mi d dl e  of  t h e  f o c u s  f or  O L.  Wit h  pr o g r e s s  i n  t h e  ﬁ el d,  i n  2 0 0 6  t h e  c o n c e pt  of  
” o nt ol o g y  l e ar ni n g  l a y er  c a k e”  [ 5]  w a s  i ntr o d u c e d  t o  or g a ni z e  a n d  d e s cri b e  t h e  diff er e nt  
st e p s  i n v ol v e d  i n  t h e  pr o c e s s  of  o nt ol o g y  l e ar ni n g  fr o m  t h e  t e xt  f or  r e al-lif e  a p pli c ati o n 
1 7

B a b a ei Gi gl o u et al. | O p e n C o nf Pr o c 4 ( 2 0 2 4) ” L L M s 4 O L 2 0 2 4: T h e 1 st L ar g e L a n g u a g e M o d el s f or O nt ol o g y L e ar ni n g 
C h all e n g e at t h e 2 3r d I S W C” 
s c e n ari o s. T h e O L l a y er c a k e i n cl u d e s (fr o m t h e b ott o m of t h e c a k e t o t h e t o p), T er m s, 
S y n o n y m s, C o n c e pt s, T a x o n o mi e s, R el ati o n s, R ul e s, a n d A xi o m s. T hi s r e ﬂ e ct s a pr o- 
gr e s si o n fr o m si m pl er t o m or e c o m pl e x a n d a b str a ct f or m s, e a c h st e p b uil di n g o n t h e 
r e s ult s of t h e pr e vi o u s o n e. It pr o vi d e s a str u ct ur e d a p pr o a c h t o u n d er st a n di n g a n d a u- 
t o m ati n g t h e O L pr o c e s s. L at er i n 2 0 1 1, H a z m a n et al.[ 6] st u di e d v ari o u s O L s y st e m s 
a n d c at e g ori z e d t h e m i nt o t w o c at e g ori e s, ( 1) l e ar ni n g fr o m u n str u ct ur e d d at a a n d ( 2) 
l e ar ni n g fr o m s e mi- str u ct ur e d d at a . T h e y al s o p oi nt e d o ut t h at w h e n h u m a n- b a s e d 
e v al u ati o n i s n ot p o s si b l e, c arr yi n g o ut ﬁ v e-l e v el e v al u ati o n s f or O L i s i m p ort a nt, l e v el s 
s u c h a s l e xi c al, hi er ar c hi c al, c o nt e xt u al, s y nt a cti c, a n d str u ct ur al l e v el s. Si n c e 2 0 1 1 
a n d i n 2 0 1 8 s ur v e y of [ 7] s h o w e d t h at a h y bri d a p pr o a c h c o m pri si n g b ot h li n g ui sti c 
a n d st ati sti c al t e c h ni q u e s pr o d u c e s b ett er o nt ol o gi e s. H o w e v er, it i s dif ﬁ c ult t o ﬁ n d t h e 
b e st t e c h ni q u e a m o u nt a p pr o a c h e s d u e t o t h e d o m ai n of t h e st u di e s. T h e tr e n d w a s 
s hift e d t o w ar d st ati sti c al t e c h ni q u e s f or t er m e xtr a cti o n s, h o w e v er f or r el ati o n e xtr a cti o n 
cl u st eri n g m et h o d s w er e t h e m o st u s e d o n e s. M or e o v er, t h e v ari o u s e v al u ati o n s of O L 
s h o w e d t h at h u m a n- b a s e d e v al u ati o n i s t h e m o st r eli a b l e a p pr o a c h f or e v al u ati o n. 
C o n si d eri n g t h at m o st of t h e a p pr o a c h e s i n t h e ﬁ el d w er e b a s e d o n st ati sti c al a p- 
pr o a c h e s or cl u st eri n g m o d el s, t h e e m er g e n c e of l ar g e l a n g u a g e m o d el s ( L L M s), of- 
f er e d a p ar a di g m s hift i n O L si n c e t h eir c h ar a ct eri sti c s j u stif y O L a s a st u di e d f or t h e 
ﬁr st ti m e wit hi n L L M s 4 O L p ar a di g m [ 8]. O n e r e a s o n f or t hi s s hift i s t h e L L M’ s g e n er a- 
ti o n c a p a biliti e s b e c a u s e t h e y ar e b ei n g tr ai n e d o n e xt e n si v e a n d di v er s e t e xt, si mil ar 
t o d o m ai n- s p e ci ﬁ c k n o wl e d g e b a s e s [ 9]. F or t h e ﬁr st ti m e, i n 2 0 2 3 t h e L L M s 4 O L [ 8] 
p ar a di g m w a s i ntr o d u c e d t h at i n c or p or at e s L L M s f or t hr e e i m p ort a nt t a s k s of O L a s 
T er m Ty pi n g, T a x o n o m y Di s c o v er y , a n d N o n- T a x o n o mi c R el ati o n E xtr a cti o n. L at er, 
m or e r e s e ar c h er s w er e i n v ol v e d i n t h e O L t a s k s fr o m diff er e nt p er s p e cti v e s [ 1 0] –[ 1 3]. 
T h e c urr e nt tr e n d i n t h e s e m a nti c w e b r e v e al s a gr o wi n g i nt er e st a m o n g r e s e ar c h er s 
i n utili zi n g L L M s [ 1 4]. A b e n c h m ar k d at a s et i s e s s e nti al t o a s s e s s t h e p erf or m a n c e 
of O L a p pr o a c h e s, p arti c ul arl y t h o s e i n v ol vi n g L L M s, i n a c o n si st e nt a n d c o m p ar a- 
b l e m a n n er. Wit h o ut s u c h b e n c h m ar k s, it b e c o m e s dif ﬁ c ult t o e v al u at e pr o gr e s s a n d 
c o m p ar e v ari o u s m et h o d ol o gi e s eff e cti v el y [ 1 3]. T o a d dr e s s t hi s g a p, i n t hi s w or k, w e 
i ntr o d u c e a n L L M s 4 O L p ar a di g m t a s k s d at a s et t o bri d g e t h e g a p i n b e n c h m ar k e v al- 
u ati o n d at a s et s s p e ci ﬁ c all y wit hi n t h e c o nt e xt of O L u si n g L L M s. O ur k e y c o ntri b uti o n 
i s t h e cr e ati o n of t h e L L M s 4 O L d at a s et, ai m e d at f a cilit ati n g c o n si st e nt e v al u ati o n i n 
t hi s e m er gi n g ﬁ el d. F or t h e ﬁr st ti m e, t hi s d at a s et i s i ntr o d u c e d i n t h e ” 1 st L L M s 4 O L 
C h all e n g e @ I S W C 2 0 2 4” [ 1 5], a c h all e n g e or g a ni z e d at t h e pr e sti gi o u s I nt er n ati o n al 
S e m a nti c W e b C o nf er e n c e (I S W C). T h e pri m ar y g o al of t h e c h all e n g e i s t o pr o vi d e a 
s h ar e d pl atf or m f or r e s e ar c h er s t o b e n c h m ar k t h eir L L M- b a s e d O L a p pr o a c h e s. B y e s- 
t a b li s hi n g t hi s d at a s et a n d l a u n c hi n g t h e L L M s 4 O L C h all e n g e, w e h o p e t o e n c o ur a g e 
f urt h er r e s e ar c h a n d i n n o v ati o n i n O L wit h L L M s, ulti m at el y e n a b li n g a m or e str u ct ur e d 
a n d f air c o m p ari s o n of diff er e nt m et h o d s i n t hi s r a pi dl y e v ol vi n g ar e a. 
T h e L L M s 4 O L 2 0 2 4 d at a s et a d dr e s s e s t hr e e O L t a s k s, w hi c h ar e k n o w n a s pri miti v e 
o nt ol o g y c o n str u cti o n t a s k s [ 1 6]. C o n si d eri n g, L a s a l e xi c al e ntri e s f or c o n c e pt u al 
t y p e T , a n d H T a s a r e pr e s e nt ati o n of t a x o n o m y of t y p e s, a n d R a s a n o n-t a x o n o mi c 
r el ati o n s, t h e L L M s 4 O L t a s k s ar e d e ﬁ n e d a s f oll o w s: 
• T a s k A – T er m T y pi n g: F or a gi v e n l e xi c al t er m L , di s c o v er t h e g e n er ali z e d t y p e 
T .
• T a s k B – T a x o n o m y Di s c o v er y: F or a gi v e n s et of g e n er ali z e d t y p e s T , di s c o v er 
t h e t a x o n o mi c hi er ar c hi c al p air s (T a , T b ) p air s, r e pr e s e nti n g ”i s- a” r el ati o n s. 
• T a s k C – N o n- T a x o n o mi c R el ati o n E xtr a cti o n: F or a gi v e n s et of g e n er ali z e d 
t y p e s T a n d r el ati o n s R , d d e ntif y n o n-t a x o n o mi c, s e m a nti c r el ati o n s b et w e e n 
1 8

B a b a ei Gi gl o u et al. | O p e n C o nf Pr o c 4 ( 2 0 2 4) ” L L M s 4 O L 2 0 2 4: T h e 1 st L ar g e L a n g u a g e M o d el s f or O nt ol o g y L e ar ni n g 
C h all e n g e at t h e 2 3r d I S W C” 
t y p e s t o f or m a (T h , r, T t) tri pl et, w h er e T h a n d T t ar e h e a d a n d t ail t a x o n o mi c 
t y p e s wit h r ∈ R .
T h e L L M s 4 O L d at a s et i s p u b li cl y a v ail a b l e o n Git H u b 1 , pr o vi di n g e a s y a c c e s s f or 
r e s e ar c h er s a n d pr a ctiti o n er s i n t h e ﬁ el d. T h e p a p er i s or g a ni z e d a s f oll o w s: S e cti o n 
2 d e s cri b e s t h e d o m ai n s t h at ar e b ei n g c o n si d er e d f or b e n c h m ar ki n g L L M s 4 Ol a n d 
S e cti o n 3 i n v e sti g at e s h o w o nt ol o gi e s ar e c ur at e d f or O L. I n s e cti o n 4, w e di s c u s s t h e 
c ur at e d d at a s et. Fi n all y , w e c o n cl u d e i n S e cti o

## 한국어 번역

L L M s 4 O L 2 0 2 4: 2 3 d I S W C에서의 학습 과제를 위한 최초의 대규모 언어 모델 
L L M s 4 O L 2 0 2 4 작업 개요 
htt p s:// d oi. 또는 g/ 1 0. 5 2 8 2 5/ o c p. v 4i. 2 4 8 0 
© Aut h 또는 s.  이 작업은 Creative Commons Attribution 4. 0 국제 라이센스에 따라 라이센스가 부여됩니다. 
게시일: 0 10월 2일 2 0 2 4 
L L M s 4 O L 2 0 2 4 D at 자산 세트: 온톨로지 학습을 위한 
대규모 언어 모델 보유 
H a m e d B a b a ei Gi g lou , J en nifer D' So u z a , Sam e er S a drud di n , and d S ¨or e n A u er 
TI B L ei b ni z I nf or mation Center for Science and T e c n o o o g y, Han nover, G er m a n y 
{ 해머디. b a b a ei, j en nifer. d s o u z a, 같은 시간. s a dr u d di n, a u er } @ti b. 너 
* 대응: H amed B a b a ei Gi g lou, ha med. b a b a ei @ti b. 너 
요약: 구조화된 데이터로부터의 온톨로지 학습(OL)은 다음과 같은 방식으로 이루어졌습니다.  
최근에는 대규모 언어 모델(LL M s)을 통합하여 다양한 성능을 향상시켰습니다.  
프로세스의 측면.  이 문서에서는 개발된 L L M s 4 OL 2 0 2 4 d 자산 세트를 소개합니다.  
L L M 을 사용하여 O L을 인증하고 고급 검색을 수행할 수 있습니다.  T the L L M s 4 OL 2 0 2 4 d at a set  
L L M s 4 OL 과제의 핵심 구성 요소는 세 가지 기본 O L 작업을 대상으로 합니다.  
ping, Taxo n o m y Discover y 및 N o n-Taxo n o mi c Reel ati o n Extr action을 입력합니다.  이는 다음과 같습니다.  
7개의 도메인, i. 이자형.  포괄적인 기능을 제공하는 어휘 및 생물학 기능을 제공합니다.  
자산 세트의 데이터에 포함된 각 작업을 L L M 기반 O L 접근 방식을 평가하기 위한 리소스  
F e w-Shot(FS) 및 Zero-Shot(Z S) 평가 시나리오 모두를 엄선하여 세심하게 제작했습니다. 
iOS에서는 다양한 지식을 바탕으로 모델 성능 또는 성능에 대한 강력한 평가를 수행할 수 있습니다.  
도메인은 표준을 제공하고 표준화된 벤치 마크를 제공하여 필드의 중요한 격차를 해소할 수 있습니다.  
O L에서 L L M 애플리케이션을 평가하는 과정을 공정하게 비교합니다. 
핵심 단어: Ontology Learning, Larg e Language Models, D at a set, L L M s 4 O L C h al- 
길이 
1 소개 
온톨로지는 이 의미 있는 웹에서 많은 인기와 인지도를 얻었습니다.  
의미와 고유한 운영 능력의 원천입니다. 구조화의 증가  
이 웹사이트에서는 구조화된 기술로부터 자동화된 기술을 자동으로 수집할 수 있게 되었습니다.  
가장 눈에 띄는 주요 내용이 담긴 텍스트입니다.  최근에는 손으로 직접 만드는 대신,  
현재 검색 추세는 이제 점점 더 자동화된 학습(OL)으로 전환되고 있습니다. [ 1] . 오엘  
여기에는 용어, 유형, 관계 및 잠재적인 원칙을 자동으로 식별하는 작업이 포함됩니다.  
비언어적 구조를 구성하는 데 필요한 정보를 제공하는 텍스트입니다 [ 2]. 
초창기 2 0 0 2 [ 3]까지의 O L 연구 기록을 되돌아보면 대부분의 O L 접근 방식이  
다른 곳에서 새로운 직원을 구축하는 대신 시드 단어나 기존 기본 솔루션에 의존했습니다.  
s cr at ch h.  나중에 2 0 0 3 [ 4]에서 N L P(Natural Language Process) 기술에 대해 설명했습니다.  
새로운 개념의 추출을 약속합니다.  그러나 O L r e- 
여전히 도전에 나섰습니다.  또한 기본 도메인에 대한 주요 지식은 아직 남아 있습니다.  
OL에 대한 초점의 중간에 있었습니다. 필드의 진행이 진행됨에 따라 2 0 0 6에서  
"온라인 학습 레이어 케이크"[ 5]는 조직을 조직하고 다양한 내용을 설명하기 위해 소개되었습니다.  
이 단계는 실제 생활에 적용하기 위해 텍스트를 통해 학습하는 온톨로지 학습 프로세스에 포함됩니다. 
1 7

B a b a ei Gi g ou et al. | Open C o nf Pro c 4 ( 2 0 2 4) ” L L M s 4 O L 2 0 2 4: 온라인 학습을 위한 최초의 대규모 언어 모델 
2 3rd I S W C에 도전하세요” 
시나리오 O L 레이어 케이크에는 다음이 포함됩니다(케이크 하단부터 상단까지). 
동의어, 개념, 분류, 관계, 규칙 및 원칙. 이 보고서는 다음과 같은 프로젝트를 반영합니다. 
simpler에서 m or e c m ple x 및 a abstract for ms에 이르기까지 각 단계에 대한 설명이 포함되어 있습니다. 
이전 결과 중 하나입니다. 이는 표준 및 분석에 대한 구조화된 접근 방식을 제공합니다. 
OL 프로세스를 자동화합니다. 나중에 2 0 1 1에서 H az man et al.[6]은 다양한 O L 시스템을 연구했습니다. 
그리고 그 순간을 두 가지 범주로 분류합니다. (1) a와 d의 구조에서 학습합니다. (2) 
a에서 SEM의 잘못된 구조를 통해 학습합니다. 그들은 또한 인간을 기반으로 한 것이라고 지적했습니다. 
평가는 불가능합니다. O L에 대한 5개 수준의 평가는 매우 중요합니다. 
여기에는 어휘적, 계층적, 내용적, 구문적, 구조적 모든 수준이 포함됩니다. 이후 2 0 1 1 
그리고 [7] 중 2018년 설문조사에서는 두 가지 측면을 모두 포함하는 하이브리드 방식의 접근 방식을 보여주었습니다. 
그리고 통계적인 기술을 통해 더 나은 도구를 생산할 수 있습니다. 그러나 해당 항목을 찾는 것은 어렵습니다. 
best tech ni q u e는 연구 영역에 대한 많은 접근 방식을 취합니다. 그 추세는 다음과 같았습니다. 
단기 추출을 위한 통계적 기술로 전환했지만, 상대적 추출을 위한 기술로 전환했습니다. 
클러스터링 방법은 가장 많이 사용되는 방법이었습니다. 또한 OL에 대한 다양한 평가 
인간 기반의 평가가 가장 신뢰할 수 있는 평가 접근 방식임을 보여주었습니다. 
필드 기반의 접근 방식 중 대부분이 통계적 애플리케이션을 기반으로 한다는 점을 고려해보세요. 
새로운 방식 또는 클러스터링 모델, 대규모 언어 모델(LL M s)의 출현 
기존의 특성에 따라 O L로의 패러다임 전환을 제안했습니다. O L을 연구한 결과로 볼 수 있습니다. 
처음으로 L L M s 4 OL 패러다임을 사용했습니다[8]. 이번 전환의 한 가지 이유는 L L M의 세대 때문입니다. 
이와 유사하게 광범위하고 다양한 텍스트로 교육을 받고 있기 때문에 이러한 기능을 활용할 수 있습니다. 
우리는 구체적으로 알고 있는 기반을 논의할 것입니다[9]. 처음으로 2 0 2 3 L L M s 4 OL [ 8] 
Para Dig M은 O L A의 세 가지 중요한 작업에 대한 L L M의 통합 내용을 소개했습니다. 
용어 입력, 세금 검색, 비과세 관계 추출 등이 있습니다. 엘 에 어, 
더 많은 조사원들이 다양한 관점에서 OL 작업에 참여했습니다. [ 1 0] – [ 1 3]. 
이러한 의미에서 웹의 현재 추세는 연구 조사자들 사이에서 점점 더 커지고 있음을 보여줍니다. 
나는 L L M s [ 1 4]를 활용하고 있습니다. 자산 세트의 벤치 마크 데이터는 성능을 평가하는 데 매우 중요합니다. 
특히 L L M 과 관련된 O L 접근 방식의 일관성과 비교는 다음과 같습니다. 
블레 맨 너. 이러한 벤치마크가 없으면 진행 상황을 평가하기가 어렵습니다. 
다양한 방법론의 효율성을 비교해보세요[1 3]. 이러한 격차를 해소하기 위해 우리는 이 작업을 통해 
마크 평가의 격차를 해소하기 위해 L L M s 4 OL 패러다임 작업을 소개합니다. 
특히 O L L M을 사용하는 O L M의 내용과 관련하여 자산 세트의 활용도가 높습니다. 우리의 핵심 기여 
이는 LLM M s 4 OLD 데이터 세트의 생성으로, 일관적인 평가를 촉진하기 위한 것입니다. 
이 새로운 분야. 처음으로 이 자산 세트의 데이터는 "1 st L L M s 4 OL"에 소개되었습니다. 
당면 과제 @ I S W C 2 0 2 4” [ 1 5], 기존 국제 국제 회의에서 제기된 과제 
Semantic Web Conference(I S W C). 당면 과제의 주요 목표는 다음을 제공하는 것입니다. 
연구 조사자들이 자신의 L L M 기반 O L 접근 방식을 표시할 수 있는 공유 플랫폼입니다. By e s- 
이 데이터를 자산 세트에 게시하고 L L M s 4 OL 챌린지를 시작하여 여러분의 격려를 부탁드립니다. 
더 나아가 L L M을 통해 O L에 대한 연구와 혁신을 통해 궁극적으로 더 많은 구조를 구축할 수 있습니다. 
그리고 최근 급속도로 발전하는 지역 내에서 다양한 방법을 공정하게 비교할 수 있습니다. 
L L M s 4 OL 2 0 2 4 d at a set 주소에는 세 가지 OL 작업이 있으며 이는 기본적으로 알려져 있습니다. 
다양한 구성 작업 [ 1 6]. 개념에 대한 Lexi Calentri e를 고려해보세요. 
유형 T, 및 H T는 유형별 세금에 대한 설명이고, R은 세금이 아닌 유형을 나타냅니다. 
관계에 따라 L L M s 4 O L 작업은 다음과 같이 정의됩니다. 
• 작업 A – 용어 유형 지정: 주어진 용어 m L에 대해 일반적인 용어 유형을 알아보세요. 
티.
• 작업 B – 분류 체계 검색: 주어진 일반화된 유형의 유형 T에 대한 검색 
세금 xo o mi chi er 아키텍처 쌍(T a , T b ) 쌍은 "i-s-a" 관계를 나타냅니다. 
• 작업 C – 비과세 관계 추출: 일반화된 특정 세트용 
유형 및 관계 R 유형, 분류학적이 아닌 식별, 의미 간의 관계를 식별합니다. 
1 8

B a b a ei Gi g ou et al. | Open C o nf Pro c 4 ( 2 0 2 4) ” L L M s 4 O L 2 0 2 4: 온라인 학습을 위한 최초의 대규모 언어 모델 
2 3rd I S W C에 도전하세요” 
m a (T h , r, T t) 트리플렛의 유형, 여기서 T h 및 T는 머리와 꼬리 꼬리 xo mic입니다. 
t y p e 는 h r ∈ R 과 같습니다.
자산 세트의 LLM M s 4 OLD 데이터는 Git Hub 1에서 공개적으로 사용 가능하며 간편한 액세스를 제공합니다. 
현장에는 연구 조사관과 실무자가 있습니다. 이 문서는 다음과 같이 구성되었습니다. 섹션 
2는 L L M s 4 Ol 및 B e n ch 마킹을 위해 고려 중인 도메인을 설명합니다. 
섹션 3 조사에서는 OL에 대해 어떤 도구도 정확하게 정의되지 않았는지 보여줍니다. 섹션 4에서는 다음 사항에 대해 논의했습니다. 
ur at ed at a set. 마지막으로 다음 섹션을 마치겠습니다.
