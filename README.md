# Named-Entity-Recognition

---

### What is named entity?
顧名思義就是讓電腦可以識別出語意實體。
辨別出在我們應用場景有重要成分、有意義的元素，協助我們了解這段文本的內涵。
命名實體識別技術可以讓電腦將詞彙和實體連接在一起，

就好比當我們看到
Steven Paul Jobs，並非是單純字面上 '賈伯斯'

Core i9–9820x，也並非只包含 'Core '的意義，

而是其背後所隱含的意義
 => 蘋果公司的創辦人 ; Intel 處理器


---

NER（Named Entity Recognition 命名實體識別) 在文本語義理解、信息解析 (entity extraction)領域發展，具有一定的重要性。
命名實體識別在部分的應用場景中得到較好的結果，其場景主要辨別named entity 類別大多為 人名、地名、機構、專有名詞…etc.

也可以應用的業務需求場景

#### 1)快速彙整履歷 : 快速瀏覽並評估人才是否適用。

#### 2)醫學臨床病例文本 : 識別病患基本資料、疾病專有名詞、病徵、治療方式。

#### 3)優化搜尋引擎結果 : 辨識顧客語意內涵，提供關聯實體做搜尋推薦。

透過 Named entity recognition 技術，辨識顧客語意來優化 E-commerce 搜尋引擎結果，相對於大多數的應用場景，其具有相當的困難與複雜程度。大多數搜尋引擎的推薦結果，是基於過去顧客搜尋、購買過的關聯式分析推薦，導致如果過去沒有顧客搜尋過的關鍵字，可能會出現不相關的產品或無結果的這種情況發生，因此這種傳統的搜索關聯需要通過辨識語意，持續優化顧客體驗，以提供更準確的結果。

#### 4)識別客戶投訴和反饋 : 將客戶投訴與反饋分類至組織內負責單位。


---

### What is the difference between regular and sequence labeling classification ?
#### -Regular classification
![image](https://github.com/CinnaBao/Named-Entity-Recognition/blob/master/Image/RegularClssfication.png)
#### -Sequence labeling classification
![image](https://github.com/CinnaBao/Named-Entity-Recognition/blob/master/Image/SequenceLabelingClassification.png)

在序列標註問題中，當前的預測標籤 (y)不僅與當前的特徵向量 x 相關，還與之前的預測標籤 (y-1) 相關，即預測標籤序列之間是具有相依性關係。

---

### What is the most common tagging format for tagging tokens in a chunking task?
#### -BIO encoding (Beginning, Inside, Outside)
B - for the first token of a named entity
I - for tokens inside named entity's
O - for tokens outside any named entity

#### -BIOLU encoding (Last, Unit-length chunks)
L - for the last tokens of named entity's
U - for unit length named entity's

---

### Future developments in the NER field ?
在 deep learning 領域，需要大量的標註資料。但是在大多數的應用場景沒有已標註的海量資料，如何使用少量標註資料進行 named entity recognition 也是未來研究的重點。
#### Transfer learning (遷移學習) : 
與這個任務直接相關的資料並不多，藉由運用與其應用場景任務相似的資料建立模型。
#### Semi-supervise learning (半監督學習) : 
藉由少部分已標註的資料，通過識別少量已標註資料的特徵進行分類。

---

### How to construct customized NER by using spaCy
  Coming soon

