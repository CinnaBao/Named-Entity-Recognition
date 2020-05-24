# Named-Entity-Recognition

![image](https://github.com/CinnaBao/Named-Entity-Recognition/blob/master/Image/pic1.png)
###### Photo credit : https://www.instagram.com/kevin550d/?igshid=e0szsshr7ter

---

* ### What is Named Entity Recognition ?
NER（Named Entity Recognition 命名實體識別) 視為在信息解析 (entity extraction, IE)、文本語義理解領域發展，具有一定的重要性。
從非結構化/半結構化的文本中提取出結構化信息，而提取出結構化的信息我們稱之為 entity identification, entity chunking, entity extraction。
命名實體識別在部分的應用場景中得到較好的結果，其場景主要辨別named entity 類別大多為人名、地名、機構、專有名詞…etc., 
可以透過 NER 協助我們回答許多現實生活中的問題，可以應用的業務需求場景包含：

#### 1)快速彙整履歷 : 

> 快速瀏覽並評估人才是否適用。

#### 2)醫學臨床病例文本 :

> 識別病患基本資料、疾病專有名詞、病徵、治療方式。

#### 3)優化搜尋引擎結果 : 辨識顧客語意內涵，提供關聯實體做搜尋推薦。

> 透過 Named entity recognition 技術，辨識顧客語意來優化 E-commerce 搜尋引擎結果，相對於大多數的應用場景，其具有相當的困難與複雜程度。

> 大多數搜尋引擎的推薦結果，是基於過去顧客搜尋、購買過的關聯式分析推薦，導致如果過去沒有顧客搜尋過的關鍵字，可能會出現不相關的產品或無結果的這種情況發生，因此這種傳統的搜索關聯需要通過辨識語意，持續優化顧客體驗，以提供更準確的結果。

#### 4)識別客戶投訴和反饋 :
> 投訴或評論特定產品、賣家、機構，將客戶投訴與反饋分類至組織內負責單位。


* ### What is named entity?
顧名思義就是讓電腦可以識別出語意實體。

辨別出在我們應用場景有重要成分、有意義的元素，協助我們了解這段文本的內涵。

命名實體識別技術可以讓電腦將詞彙和實體連接在一起，就好比當我們看到

_Steven Paul Jobs_ ，並非是單純字面上 _'賈伯斯'_

_Core i9–9820x_ ，也並非只包含 _'Core'_ 的意義，而是其背後所隱含的意義

 => **蘋果公司的創辦人** ; **Intel 處理器**
 
 ---

* ### What is the difference between regular and sequence labeling classification ?

#### - Regular classification
![image](https://github.com/CinnaBao/Named-Entity-Recognition/blob/master/Image/RegularClssfication.png)


#### - Sequence labeling classification
![image](https://github.com/CinnaBao/Named-Entity-Recognition/blob/master/Image/SequenceLabelingClassification.png)

在序列標註問題中，當前的預測標籤 (y)不僅與當前的特徵向量 x 相關，還與之前的預測標籤 (y-1) 相關，即預測標籤序列之間是具有相依性關係。

---

* ### What is the most common tagging format for tagging tokens in a chunking task?
#### -BIO encoding (Beginning, Inside, Outside)

> B - for the first token of a named entity

> I - for tokens inside named entity's

> O - for tokens outside any named entity


#### -BIOLU encoding (Last, Unit-length chunks)

> L - for the last tokens of named entity's

> U - for unit length named entity's

---

* ### customized NER by using spaCy

上述程式碼為使用SpaCy構建客製化的命名實體識別器。

在命名實體識別領域中， SpaCy 與 NLTK 是在自然語言處理領域中較常使用的套件包。

SpaCy 除了提供已建置好的命名實體識別器 (person, organization, language, event …etc.)，也可以透過添加新的 named entity類別，訓練符合當前任務需求的實體識別模型。


---

* ### Future developments in the NER field ?

在 deep learning 領域，需要大量的標註資料。

但是在大多數的應用場景沒有已標註的海量資料，如何使用少量標註資料進行 named entity recognition 也是未來研究的重點。

#### - Transfer learning (遷移學習) : 

> 與這個任務直接相關的資料並不多，藉由運用與其應用場景任務相似的資料建立模型。

#### - Semi-supervise learning (半監督學習) : 

> 藉由少部分已標註的資料，通過識別少量已標註資料的特徵進行分類。

---


